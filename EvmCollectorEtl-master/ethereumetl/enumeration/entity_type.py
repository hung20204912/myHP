class EntityType:
    BLOCK = 'block'
    TRANSACTION = 'transaction'
    RECEIPT = 'receipt'
    LOG = 'log'
    TOKEN_TRANSFER = 'token_transfer'
    TRACE = 'trace'
    CONTRACT = 'contract'
    TOKEN = 'token'
    ENRICH_TXS = 'enrich_txs'

    ALL_FOR_STREAMING = [BLOCK, TRANSACTION, LOG, TOKEN_TRANSFER, TRACE, CONTRACT, TOKEN, ENRICH_TXS]
    ALL_FOR_INFURA = [BLOCK, TRANSACTION, LOG, TOKEN_TRANSFER]
