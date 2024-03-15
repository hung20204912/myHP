import os
import pathlib

from web3 import Web3
from web3.middleware import geth_poa_middleware
from ethereumetl.jobs.export_token_transfers_job import ExportTokenTransfersJob


class EthTokenTransferStreamerAdapter:
    def __init__(
            self,
            tokens,
            batch_web3_provider,
            item_exporter,
            batch_size=96,
            max_workers=8,
            transaction_collector_id="transaction_collector"):
        self.tokens = tokens
        self.batch_web3_provider= batch_web3_provider
        self.w3 = Web3(batch_web3_provider)
        # self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.item_exporter = item_exporter
        self.batch_size = batch_size
        self.max_workers = max_workers
        self.tx_collector = transaction_collector_id
        """
        log performance realtime for mr.dat
        """
        root_path = str(pathlib.Path(__file__).parent.resolve()) + "/../../"
        self.log_performance_file = root_path + "log_performance_file.csv"
        if not os.path.exists(self.log_performance_file):
            with open(self.log_performance_file, 'w+')as f:
                f.write("start_block,end_block,start,end\n")

    def open(self):
        self.item_exporter.open()

    def get_current_block_number(self):
        collector = self.item_exporter.get_collector(collector_id=self.tx_collector)
        print(self.tx_collector)
        block_number = collector.get('last_updated_at_block_number')
        print(block_number)
        return int(block_number)

    def export_all(self, start_block, end_block):
        # Extract token transfers
        self._export_token_transfers(start_block, end_block, self.tokens)

    def _export_token_transfers(self, start_block, end_block, tokens):
        job = ExportTokenTransfersJob(
            start_block=start_block,
            end_block=end_block,
            batch_size=self.batch_size,
            web3=self.w3,
            batch_web3_provider= self.batch_web3_provider,
            item_exporter=self.item_exporter,
            max_workers=self.max_workers,
            tokens=tokens
            )
        job.run()

    def close(self):
        self.item_exporter.close()
