from artifacts.abi.lending_pool_abi import LENDING_POOL_ABI
from artifacts.abi.lending_pool_aave_v2_abi import LENDING_POOL_AAVE_V2_ABI


class PoolConstant:
    mapping = {
        'trava-bsc': {
            'name': 'trava-bsc',
            'chain_name': 'bsc',
            'decimals': 8,
            'address': '0x75de5f7c91a89c16714017c7443eca20c7a8c295',
            'abi': LENDING_POOL_ABI
        },
        'geist': {
            'name': 'geist',
            'chain_name': 'ftm',
            'decimals': 18,
            'address': '0x9fad24f572045c7869117160a571b2e50b10d068',
            'abi': LENDING_POOL_AAVE_V2_ABI
        },
        'trava-ftm': {
            'name': 'trava_ftm',
            'chain_name': 'ftm',
            'decimals': 8,
            'address': '0xd98bb590bdfabf18c164056c185fbb6be5ee643f',
            'abi': LENDING_POOL_ABI
        },
        'trava-eth': {
            'name': 'trava-eth',
            'chain_name': 'eth',
            'decimals': 8,
            'address': '',
            'abi': LENDING_POOL_ABI,
        },
        'aave_v2': {
            'name': 'aave_v2',
            'chain_name': 'eth',
            'decimals': 8,
            'address': '0x7d2768de32b0b80b7a3454c06bdac94a69ddc7a9',
            'abi': LENDING_POOL_ABI,
        },
    }
    token_type = ['reserve', 'debtAsset', 'collateralAsset']
    event_type = ['DEPOSIT', 'WITHDRAW']
