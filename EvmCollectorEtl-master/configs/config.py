import os
import random


class Config:
    HOST = '0.0.0.0'
    PORT = 8000


class MongoDBConfig:
    NAME = os.environ.get("MONGO_USERNAME") or "just_for_dev"
    PASSWORD = os.environ.get("MONGO_PASSWORD") or "password_for_dev"
    HOST = os.environ.get("MONGO_HOST") or "localhost"
    PORT = os.environ.get("MONGO_PORT") or "27027"
    DATABASE = "blockchain_etl"
    BLOCKS = "blocks"
    TRANSACTIONS = "transactions"
    TOKEN_TRANSFERS = "token_transfers"
    CONTRACTS = "contracts"
    TOKENS = "tokens"
    RECEIPTS = "receipts"
    LOGS = "logs"
    COLLECTORS = "collectors"
    WALLETS = "wallets"
    LENDING_EVENTS = 'lending_events'
    TRAVADAO_EVENTS = "travadao_events"
    EVENTS = ['lending_events', "travadao_events"]

class Providers:
    # full nodes
    # archive nodes
    BSC_PUBLIC_ARCHIVE_NODE = ['https://bsc-dataseed1.binance.org/', 'https://bsc-dataseed.binance.org/',
                               'https://bsc-dataseed1.defibit.io/', 'https://bsc-dataseed1.ninicoin.io/',
                               'https://speedy-nodes-nyc.moralis.io/d50cdc2c637838fcf416892c/bsc/mainnet/archive']
    # BSC_PUBLIC_ARCHIVE_NODE = ['https://speedy-nodes-nyc.moralis.io/892851844778bc31eb9f6b6e/bsc/mainnet/archive']
    # Free moralis
    # BSC_MORALIS_ARCHIVE_NODE = ['https://speedy-nodes-nyc.moralis.io/c1bd46ded7f4386e6977d12b/bsc/mainnet/archive']
    # Pro moralis
    BSC_MORALIS_ARCHIVE_NODE = ['https://speedy-nodes-nyc.moralis.io/d50cdc2c637838fcf416892c/bsc/mainnet/archive']

    BSC_PRIVATE_ARCHIVE_NODE = ['https://nd-521-402-221.p2pify.com/ee664ddae220517339d465993956f79f']

    def get_other_provider_uri(self):
        return random.choice(self.BSC_PUBLIC_ARCHIVE_NODE)


class SIZES:
    UPDATE_SIZE = 10000
    BALANCE_BATCH_SIZE = 100
    ETL_JOB_BATCH_SIZE = 1000
    MAX_RETRIES_COUNT = 5
    DAY_ASYNC = 20
    HOLDERS_BATCH_SIZE_MORALIS = 1000
    HOLDERS_BATCH_SIZE_PRIVATE = 1000
    TIME_SLEEP = 0
    SYNC_TIME = UPDATE_SIZE*3 + 6000
    # SYNC_TIME = 10


class MonitoringConfig:
    MONITOR_ROOT_PATH = "/home/monitor/.log/"
