import logging
import time

from web3 import Web3
from web3.middleware import geth_poa_middleware

from blockchainetl.jobs.exporters.in_memory_item_exporter import InMemoryItemExporter
from data_storage.contract_filter import ContractFilterMemoryStorage
from ethereumetl.enumeration.entity_type import EntityType
from ethereumetl.jobs.export_blocks_job import ExportBlocksJob
from ethereumetl.jobs.export_log_job import ExportLogsJob
from ethereumetl.streaming.eth_item_id_calculator import EthItemIdCalculator
from ethereumetl.streaming.eth_item_timestamp_calculator import EthItemTimestampCalculator

logger = logging.getLogger("EthLogsStreamerAdapter")


class EthLogsStreamerAdapter:
    def __init__(
            self,
            batch_web3_provider,
            item_importer,
            item_exporter,
            batch_size=100,
            block_batch_size=96,
            rpc_batch=100,
            max_workers=5,
            entity_types=tuple(EntityType.ALL_FOR_STREAMING),
            stream_id='default-collector',
            stream_name=None
    ):
        self.rpc_batch = rpc_batch
        self.stream_name = stream_name
        self.item_importer = item_importer
        self.batch_web3_provider = batch_web3_provider
        self.w3 = Web3(batch_web3_provider)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.item_exporter = item_exporter
        self.batch_size = batch_size
        self.batch_size_block = min(batch_size, int(block_batch_size / max_workers))
        self.max_workers = max_workers
        self.entity_types = entity_types
        self.item_id_calculator = EthItemIdCalculator()
        self.item_timestamp_calculator = EthItemTimestampCalculator()
        self.contract_filter = ContractFilterMemoryStorage.getInstance()
        self.stream_id = stream_id

    def open(self):
        self.item_exporter.open()

    def get_current_block_number(self):
        if self.stream_name:
            stream_data = self.item_importer.get_stream_id(self.stream_name)
            return stream_data.get("last_updated_at_block_number")
        return int(self.w3.eth.block_number)

    def export_all(self, start_block, end_block):
        start = time.time()
        # reset temp wallet
        self.contract_filter.clear_temp()
        transactions, blocks, logs, receipts = [], [], [], []
        # Export blocks and transactions
        if EntityType.BLOCK in self.entity_types or EntityType.TRANSACTION in self.entity_types:
            blocks, transactions = self._export_blocks_and_transactions(start_block, end_block)

        # Export receipts and logs
        if EntityType.RECEIPT in self.entity_types or EntityType.LOG in self.entity_types:
            receipts, logs, transactions = self._export_receipts_and_logs(start_block, end_block)

        logging.info('Exporting with ' + type(self.item_exporter).__name__)

        self.item_exporter.upsert_blocks(blocks)
        self.item_exporter.upsert_logs(logs)
        self.item_exporter.upsert_transactions(transactions)
        self.item_exporter.upsert_receipts(receipts)
        end = time.time()
        logger.info(f"Success write items to collections take {end - start}")

    def _export_blocks_and_transactions(self, start_block, end_block):
        blocks_and_transactions_item_exporter = InMemoryItemExporter(item_types=['block', 'transaction'])
        blocks_and_transactions_job = ExportBlocksJob(
            start_block=start_block,
            end_block=end_block,
            batch_size=self.batch_size_block,
            batch_web3_provider=self.batch_web3_provider,
            max_workers=self.max_workers,
            item_exporter=blocks_and_transactions_item_exporter,
            export_blocks=EntityType.BLOCK in self.entity_types,
            export_transactions=EntityType.TRANSACTION in self.entity_types
        )
        blocks_and_transactions_job.run()
        blocks = blocks_and_transactions_item_exporter.get_items('block')
        transactions = blocks_and_transactions_item_exporter.get_items('transaction')
        return blocks, transactions

    def _export_receipts_and_logs(self, start_block, end_block):
        exporter = InMemoryItemExporter(item_types=['receipt', 'log', 'transaction'])
        job = ExportLogsJob(
            start_block=start_block,
            end_block=end_block,
            batch_size=self.batch_size,
            batch_web3_provider=self.batch_web3_provider,
            rpc_batch=self.rpc_batch,
            max_workers=self.max_workers,
            item_importer=self.item_importer,
            item_exporter=exporter,
            export_receipts=EntityType.RECEIPT in self.entity_types,
            export_logs=EntityType.LOG in self.entity_types,
            enrich_txs=EntityType.ENRICH_TXS in self.entity_types
        )
        job.run()
        receipts = exporter.get_items('receipt')
        logs = exporter.get_items('log')
        transactions = exporter.get_items('transaction')
        return receipts, logs, transactions

    def close(self):
        self.item_exporter.close()
