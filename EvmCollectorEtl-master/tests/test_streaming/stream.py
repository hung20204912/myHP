import logging
import random

import click

from blockchainetl.streaming.streaming_utils import configure_signals, configure_logging
from ethereumetl.enumeration.entity_type import EntityType
from ethereumetl.providers.auto import get_provider_from_uri
from ethereumetl.thread_local_proxy import ThreadLocalProxy


def stream(last_synced_block_file, lag, provider_uri, output, start_block, entity_types,
           period_seconds=10, batch_size=2, block_batch_size=10, max_workers=5, log_file=None, pid_file=None):
    """Streams all data types to console or Google Pub/Sub."""
    configure_logging(log_file)
    configure_signals()
    entity_types = parse_entity_types(entity_types)
    validate_entity_types(entity_types, output)

    from ethereumetl.streaming.item_exporter_creator import create_item_exporter
    from ethereumetl.streaming.eth_streamer_adapter import EthStreamerAdapter
    from blockchainetl.streaming.streamer import Streamer

    # TODO: Implement fallback mechanism for provider uris instead of picking randomly
    provider_uri = pick_random_provider_uri(provider_uri)
    logging.info('Using ' + provider_uri)
    stream_id = "streaming_collector"
    streamer_adapter = EthStreamerAdapter(
        batch_web3_provider=ThreadLocalProxy(lambda: get_provider_from_uri(provider_uri, batch=True)),
        item_exporter=create_item_exporter(output),
        batch_size=batch_size,
        block_batch_size= block_batch_size,
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
        pid_file=pid_file,
        stream_id=stream_id,
        output=output
    )
    streamer.stream()


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


if __name__ == '__main__':
    # provider_uri = "https://speedy-nodes-nyc.moralis.io/cd00f2fddfd96dc8ed17bf2a/eth/ropsten/archive"
    # provider_uri = "https://speedy-nodes-nyc.moralis.io/cd00f2fddfd96dc8ed17bf2a/bsc/mainnet/archive"
    provider_uri = "http://25.9.223.246:8545"
    # provider_uri = "https://speedy-nodes-nyc.moralis.io/cd00f2fddfd96dc8ed17bf2a/bsc/testnet"
    last_synced_block_file = "../../.data/last_synced_block.txt"
    lag = 0
    # output = None
    output = "mongodb://just_for_dev:password_for_dev@localhost:27027/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false"
    # start_block = 4378378
    start_block = None
    entity_types = "block,transaction,log,token_transfer,trace,contract,token"
    stream(last_synced_block_file=last_synced_block_file, lag=lag, provider_uri=provider_uri, output=output,
           start_block=start_block, entity_types=entity_types)
