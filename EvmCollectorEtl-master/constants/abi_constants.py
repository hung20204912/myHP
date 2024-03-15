from artifacts.abi.bep20_abi import BEP20_ABI
from artifacts.abi.lending_pool_abi import LENDING_POOL_ABI
from artifacts.abi.lending_pool_aave_v2_abi import LENDING_POOL_AAVE_V2_ABI
from artifacts.abi.erc20_abi import ERC20_ABI
from artifacts.abi.trava_oracle_abi import TRAVA_ORACLE_ABI
from artifacts.abi.lending_pool_geist_abi import LENDING_POOL_GEIST_ABI
from artifacts.abi.lending_pool_aave_v1_abi import LENDING_POOL_AAVE_V1_ABI
from artifacts.abi.bonding_tradao import BONDING_TRADAO_ABI
from artifacts.abi.chainlink_abi import CHAINLINK_ABI
from artifacts.abi.ve_abi import VE_ABI
from artifacts.abi.debt_token_base_abi import DEBT_TOKEN_ABI
from artifacts.abi.eth_aave_gateway_lending import ETH_AAVE_GATEWAY_LENDING
from artifacts.abi.fmt_gateway_lending import FTM_GATEWAY_LENDING
from artifacts.abi.trava_bnb_vault_abi import TRAVA_BNB_VAULT_ABI
from artifacts.abi.tToken_abi import TTOKEN_ABI
from artifacts.abi.dfyn_dual_stake import DFYN_DUAL_STAKE_ABI
from artifacts.abi.dfyn_single_asset_vault import DFYN_SINGLE_VAULT_ABI
from artifacts.abi.v_native_token_abi import V_NATIVE_TOKEN_ABI
from artifacts.abi.wbnb_abi import WBNB_ABI
from artifacts.abi.vToken_abi import VTOKEN_ABI
from artifacts.abi.trava_vault_abi import TRAVA_VAULT_ABI


class ABI:
    mapping = {
        "bep20_abi": BEP20_ABI,
        "trava_lending_abi": LENDING_POOL_ABI,
        "aave_v1_abi": LENDING_POOL_AAVE_V1_ABI,
        "aave_v2_abi": LENDING_POOL_AAVE_V2_ABI,
        "erc20_abi": ERC20_ABI,
        "oracle_abi": TRAVA_ORACLE_ABI,
        "geist_abi": LENDING_POOL_GEIST_ABI,
        "bonding_tradao": BONDING_TRADAO_ABI,
        "chainlink_abi": CHAINLINK_ABI,
        "ve_abi": VE_ABI,
        "debt_token_base_abi": DEBT_TOKEN_ABI,
        "eth_aave_gateway_lending": ETH_AAVE_GATEWAY_LENDING,
        "fmt_gateway_lending": FTM_GATEWAY_LENDING,
        "trava_bnb_vault_abi": TRAVA_BNB_VAULT_ABI,
        "tToken_abi": TTOKEN_ABI,
        "dfyn_dual_stake": DFYN_DUAL_STAKE_ABI,
        "dfyn_single_asset_vault": DFYN_SINGLE_VAULT_ABI,
        "v_native_token_abi": V_NATIVE_TOKEN_ABI,
        "wbnb_abi": WBNB_ABI,
        "vToken_abi": VTOKEN_ABI,
        "trava_vault_abi": TRAVA_VAULT_ABI
    }