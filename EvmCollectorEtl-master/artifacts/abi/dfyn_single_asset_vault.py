"""
 the addresses for single asset vault here:
https://github.com/dfyn/dfyn-farms-info/blob/main/single-asset-vault.js

All contracts interface are same, you can get ABI from here:
https://polygonscan.com/address/0xc5574645f618ee9a3b5d8c4f69b1983d7d226290#code

To deposit: stake()
To withdraw: claim()

"""

DFYN_SINGLE_VAULT_ABI = [{"inputs": [{"internalType": "address", "name": "_vaultToken", "type": "address"},
                                     {"internalType": "uint256", "name": "_vestingPeriod", "type": "uint256"},
                                     {"internalType": "uint256", "name": "_interestRate", "type": "uint256"},
                                     {"internalType": "uint256", "name": "_vaultLimit", "type": "uint256"}],
                          "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [
    {"indexed": True, "internalType": "address", "name": "user", "type": "address"},
    {"indexed": False, "internalType": "uint256", "name": "reward", "type": "uint256"}], "name": "Claimed",
                                                                                    "type": "event"},
                         {"anonymous": False, "inputs": [
                             {"indexed": False, "internalType": "address", "name": "userAddress", "type": "address"},
                             {"indexed": False, "internalType": "address payable", "name": "relayerAddress",
                              "type": "address"},
                             {"indexed": False, "internalType": "bytes", "name": "functionSignature", "type": "bytes"}],
                          "name": "MetaTransactionExecuted", "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "user", "type": "address"},
        {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "Staked",
                                                                                "type": "event"},
                         {"inputs": [], "name": "ERC712_VERSION",
                          "outputs": [{"internalType": "string", "name": "", "type": "string"}],
                          "stateMutability": "view", "type": "function"},
                         {"inputs": [{"internalType": "address", "name": "account", "type": "address"}],
                          "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                          "stateMutability": "view", "type": "function"},
                         {"inputs": [], "name": "claim", "outputs": [], "stateMutability": "nonpayable",
                          "type": "function"},
                         {"inputs": [{"internalType": "address", "name": "account", "type": "address"}],
                          "name": "earned", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                          "stateMutability": "view", "type": "function"}, {
                             "inputs": [{"internalType": "address", "name": "userAddress", "type": "address"},
                                        {"internalType": "bytes", "name": "functionSignature", "type": "bytes"},
                                        {"internalType": "bytes32", "name": "sigR", "type": "bytes32"},
                                        {"internalType": "bytes32", "name": "sigS", "type": "bytes32"},
                                        {"internalType": "uint8", "name": "sigV", "type": "uint8"}],
                             "name": "executeMetaTransaction",
                             "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
                             "stateMutability": "payable", "type": "function"}, {"inputs": [], "name": "getChainId",
                                                                                 "outputs": [{"internalType": "uint256",
                                                                                              "name": "",
                                                                                              "type": "uint256"}],
                                                                                 "stateMutability": "pure",
                                                                                 "type": "function"},
                         {"inputs": [], "name": "getDomainSeperator",
                          "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
                          "stateMutability": "view", "type": "function"},
                         {"inputs": [{"internalType": "address", "name": "user", "type": "address"}],
                          "name": "getNonce",
                          "outputs": [{"internalType": "uint256", "name": "nonce", "type": "uint256"}],
                          "stateMutability": "view", "type": "function"},
                         {"inputs": [{"internalType": "address", "name": "account", "type": "address"}],
                          "name": "getUserVaultInfo", "outputs": [{"components": [
                             {"internalType": "uint256", "name": "amount", "type": "uint256"},
                             {"internalType": "uint256", "name": "depositTime", "type": "uint256"},
                             {"internalType": "uint256", "name": "vestingPeriodEnds", "type": "uint256"},
                             {"internalType": "uint256", "name": "lastUpdated", "type": "uint256"},
                             {"internalType": "uint256", "name": "claimedAmount", "type": "uint256"},
                             {"internalType": "uint256", "name": "totalEarned", "type": "uint256"}],
                                                                   "internalType": "struct Vault.UserVault[]",
                                                                   "name": "", "type": "tuple[]"}],
                          "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "interestRate",
                                                                           "outputs": [
                                                                               {"internalType": "uint256", "name": "",
                                                                                "type": "uint256"}],
                                                                           "stateMutability": "view",
                                                                           "type": "function"},
                         {"inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "stake",
                          "outputs": [], "stateMutability": "nonpayable", "type": "function"},
                         {"inputs": [], "name": "totalDeposits",
                          "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                          "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "totalSupply",
                                                                           "outputs": [
                                                                               {"internalType": "uint256", "name": "",
                                                                                "type": "uint256"}],
                                                                           "stateMutability": "view",
                                                                           "type": "function"}, {
                             "inputs": [{"internalType": "address", "name": "", "type": "address"},
                                        {"internalType": "uint256", "name": "", "type": "uint256"}],
                             "name": "userVault",
                             "outputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"},
                                         {"internalType": "uint256", "name": "depositTime", "type": "uint256"},
                                         {"internalType": "uint256", "name": "vestingPeriodEnds", "type": "uint256"},
                                         {"internalType": "uint256", "name": "lastUpdated", "type": "uint256"},
                                         {"internalType": "uint256", "name": "claimedAmount", "type": "uint256"},
                                         {"internalType": "uint256", "name": "totalEarned", "type": "uint256"}],
                             "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "vaultLimit",
                                                                              "outputs": [{"internalType": "uint256",
                                                                                           "name": "",
                                                                                           "type": "uint256"}],
                                                                              "stateMutability": "view",
                                                                              "type": "function"},
                         {"inputs": [], "name": "vaultToken",
                          "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}],
                          "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "vestingPeriod",
                                                                           "outputs": [
                                                                               {"internalType": "uint256", "name": "",
                                                                                "type": "uint256"}],
                                                                           "stateMutability": "view",
                                                                           "type": "function"}]
