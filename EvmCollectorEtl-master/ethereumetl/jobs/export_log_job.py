# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import json

from blockchainetl.jobs.base_job import BaseJob
from constants.topic_constant import TOPICS
from ethereumetl.executors.batch_work_executor import BatchWorkExecutor
from ethereumetl.json_rpc_requests import generate_get_receipt_json_rpc
from ethereumetl.mappers.receipt_log_mapper import EthReceiptLogMapper
from ethereumetl.mappers.receipt_mapper import EthReceiptMapper
from ethereumetl.utils import rpc_response_batch_to_results, validate_range


# Exports receipts and logs
class ExportLogsJob(BaseJob):
    def __init__(
            self,
            start_block,
            end_block,
            batch_size,
            batch_web3_provider,
            max_workers,
            item_importer,
            item_exporter,
            rpc_batch=1000,
            export_receipts=True,
            export_logs=True,
            enrich_txs=True
    ):
        self.rpc_batch = rpc_batch
        self.enrich_txs = enrich_txs
        self.item_importer = item_importer
        validate_range(start_block, end_block)
        self.end_block = end_block
        self.start_block = start_block
        self.batch_web3_provider = batch_web3_provider
        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)
        self.item_exporter = item_exporter
        self.export_receipts = export_receipts
        self.export_logs = export_logs
        if not self.export_receipts and not self.export_logs:
            raise ValueError('At least one of export_receipts or export_logs must be True')

        self.receipt_mapper = EthReceiptMapper()
        self.receipt_log_mapper = EthReceiptLogMapper()

    def _start(self):
        self.item_exporter.open()

    def _export(self):
        self.batch_work_executor.execute(
            range(self.start_block, self.end_block + 1),
            self._export_receipts,
            total_items=self.end_block - self.start_block + 1
        )

    def _export_receipts(self, block_number_batch):
        transaction_hashes = self.item_importer.get_transaction_hashes(block_number_batch)
        receipts_rpc = list(generate_get_receipt_json_rpc(transaction_hashes))
        for idx in range(0, len(receipts_rpc), self.rpc_batch):
            response = self.batch_web3_provider.make_batch_request(
                json.dumps(receipts_rpc[idx: idx + self.rpc_batch]))
            results = rpc_response_batch_to_results(response)
            receipts = [self.receipt_mapper.json_dict_to_receipt(result) for result in results]
            for receipt in receipts:
                self._export_receipt(receipt)

    def _export_receipt(self, receipt):
        if self.export_receipts:
            self.item_exporter.export_item(self.receipt_mapper.receipt_to_dict(receipt))
        if self.export_logs:
            for log in receipt.logs:
                if not log.topics or log.topics[0] not in TOPICS:
                    continue
                self.item_exporter.export_item(self.receipt_log_mapper.receipt_log_to_dict(log))

        if self.enrich_txs:
            self.item_exporter.export_item(self.enrich_transactions(receipt))

    def _end(self):
        self.batch_work_executor.shutdown()
        self.item_exporter.close()

    def enrich_transactions(self, receipt):
        transaction = {
            'hash': receipt.transaction_hash,
            'block_number': receipt.block_number,
            'type': 'transaction',
            'receipt_cumulative_gas_used': receipt.cumulative_gas_used,
            'receipt_gas_used': receipt.gas_used,
            'receipt_contract_address': receipt.contract_address,
            'receipt_root': receipt.root,
            'receipt_status': receipt.status

        }

        return transaction
