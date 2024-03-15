sourimport os
import random
import sys
from os import path

import click
from web3 import Web3


TOP_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(TOP_DIR, './'))

from utils.logging_utils import config_log
from utils.none_utils import remove_none_string
from blockchainetl.streaming.streamer import Streamer
from configs.blockchain_etl_config import BlockchainEtlConfig
from ethereumetl.enumeration.entity_type import EntityType
from ethereumetl.providers.auto import get_provider_from_uri
from ethereumetl.streaming.eth_streamer_adapter import EthStreamerAdapter
from ethereumetl.streaming.item_exporter_creator import create_item_exporter
from ethereumetl.thread_local_proxy import ThreadLocalProxy


config_log()
def parse_entity_types(entity_types):
    entity_types = [c.strip() for c in entity_types.split(',')]

    # validate passed types
    for entity_type in entity_types:
        if entity_type not in EntityType.ALL_FOR_STREAMING:
            raise click.BadOptionUsage(
                '--entity-type', '{} is not an available entity type. Supply a comma separated list of types from {}'
                    .format(entity_type, ','.join(EntityType.ALL_FOR_STREAMING)))

    return entity_types


def validate_entity_types(entity_types, output):
    from ethereumetl.streaming.item_exporter_creator import determine_item_exporter_type, ItemExporterType
    item_exporter_type = determine_item_exporter_type(output)
    if item_exporter_type == ItemExporterType.POSTGRES \
            and (EntityType.CONTRACT in entity_types or EntityType.TOKEN in entity_types):
        raise ValueError('contract and token are not yet supported entity types for postgres item exporter.')


def pick_random_provider_uri(provider_uri):
    provider_uris = [uri.strip() for uri in provider_uri.split(',')]
    return random.choice(provider_uris)

def get_latest_block(provider_uri):
    batch_web3_provider = ThreadLocalProxy(lambda: get_provider_from_uri(provider_uri, batch=True))
    w3 = Web3(batch_web3_provider)
    # w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return int(w3.eth.blockNumber)

if __name__ == '__main__':
    ### get environment variables

    log_file = remove_none_string(BlockchainEtlConfig.LOG_FILE)
    provider_uri = remove_none_string(BlockchainEtlConfig.PROVIDER_URI)
    lag = int(BlockchainEtlConfig.LAG)
    batch_size = int(BlockchainEtlConfig.BATCH_SIZE)
    max_workers = int(BlockchainEtlConfig.MAX_WORKERS)
    start_block = int(BlockchainEtlConfig.START_BLOCK)
    period_seconds = int(BlockchainEtlConfig.PERIOD_SECONDS)
    pid_file = remove_none_string(BlockchainEtlConfig.PID_FILE)
    block_batch_size = int(BlockchainEtlConfig.BLOCK_BATCH_SIZE)
    output = remove_none_string(BlockchainEtlConfig.OUTPUT)
    entity_types = remove_none_string(BlockchainEtlConfig.ENTITY_TYPES)

    last_synced_block_file = "../.data/last_synced_block.txt"
    if path.exists(last_synced_block_file):
        start_block = None
    elif not start_block:
        start_block = get_latest_block(provider_uri)

    streamer_adapter = EthStreamerAdapter(
        batch_web3_provider=ThreadLocalProxy(lambda: get_provider_from_uri(provider_uri, batch=True)),
        item_exporter=create_item_exporter(output),
        batch_size=batch_size,
        max_workers=max_workers,
        entity_types=entity_types
    )
    streamer = Streamer(
        blockchain_streamer_adapter=streamer_adapter,
        last_synced_block_file=last_synced_block_file,
        lag=lag,
        start_block=start_block,
        period_seconds=period_seconds,
        block_batch_size=block_batch_size,
        pid_file=pid_file
    )
    streamer.stream()