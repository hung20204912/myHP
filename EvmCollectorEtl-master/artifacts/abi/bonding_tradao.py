BONDING_TRADAO_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "approved",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "bonder",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "price",
                "type": "uint256"
            }
        ],
        "name": "Bond",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "BondDebted",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "BondLiquidated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "BondRepaid",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "CloseMarket",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "baseToken",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "quoteToken",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "initialPrice",
                "type": "uint256"
            }
        ],
        "name": "CreateMarket",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "controlVariable",
                "type": "uint256"
            }
        ],
        "name": "Tuned",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "approved",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_id",
                "type": "uint256"
            }
        ],
        "name": "close",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_trust",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_reputation",
                "type": "address"
            }
        ],
        "name": "configPartialAuthorities",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint32",
                "name": "_basepart",
                "type": "uint32"
            },
            {
                "internalType": "uint32",
                "name": "_scorepartstep",
                "type": "uint32"
            },
            {
                "internalType": "uint128",
                "name": "_baselimit",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "_scorelimitstep",
                "type": "uint128"
            }
        ],
        "name": "configPartialLimits",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint32",
                "name": "_excesspart",
                "type": "uint32"
            },
            {
                "internalType": "uint32",
                "name": "_rate",
                "type": "uint32"
            },
            {
                "internalType": "uint32",
                "name": "_interest",
                "type": "uint32"
            },
            {
                "internalType": "uint32",
                "name": "_discount",
                "type": "uint32"
            }
        ],
        "name": "configPartialRates",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_dao",
                "type": "address"
            },
            {
                "internalType": "uint32",
                "name": "_daoRate",
                "type": "uint32"
            },
            {
                "internalType": "uint32",
                "name": "_feoRate",
                "type": "uint32"
            }
        ],
        "name": "configReward",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "quoteToken",
                        "type": "address"
                    },
                    {
                        "internalType": "bool",
                        "name": "capacityInQuote",
                        "type": "bool"
                    },
                    {
                        "internalType": "bool",
                        "name": "flexTerm",
                        "type": "bool"
                    },
                    {
                        "internalType": "bool",
                        "name": "allowPartial",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint256",
                        "name": "capacity",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "initialPrice",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "debtBuffer",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "vesting",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "conclusion",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "depositInt",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "tuneInt",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IBondDepository.CreateInfo",
                "name": "info",
                "type": "tuple"
            }
        ],
        "name": "create",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_id",
                "type": "uint256"
            }
        ],
        "name": "currentControlVariable",
        "outputs": [
            {
                "internalType": "uint64",
                "name": "cv",
                "type": "uint64"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_id",
                "type": "uint256"
            }
        ],
        "name": "currentDebt",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_id",
                "type": "uint256"
            }
        ],
        "name": "debtDecay",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_id",
                "type": "uint256"
            }
        ],
        "name": "debtRatio",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_id",
                "type": "uint256"
            }
        ],
        "name": "decayTune",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "market",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "price",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address",
                        "name": "user",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "referral",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "unpaidAdvance",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IBondDepository.DepositInfo",
                "name": "info",
                "type": "tuple"
            },
            {
                "internalType": "bytes",
                "name": "_rtTrustScore",
                "type": "bytes"
            }
        ],
        "name": "deposit",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "payout",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "getApproved",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_treasury",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_staking",
                "type": "address"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_quote",
                "type": "address"
            }
        ],
        "name": "liveMarkets",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256",
                "name": "total",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_id",
                "type": "uint256"
            }
        ],
        "name": "marketPrice",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_quote",
                "type": "address"
            }
        ],
        "name": "marketsFor",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256[]",
                "name": "_ids",
                "type": "uint256[]"
            }
        ],
        "name": "marketsInfo",
        "outputs": [
            {
                "internalType": "bytes32[6][]",
                "name": "stores",
                "type": "bytes32[6][]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_user",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_payout",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_part",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "_scoreData",
                "type": "bytes"
            }
        ],
        "name": "maxUnpaidHandler",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "part",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_note",
                "type": "uint256"
            }
        ],
        "name": "noteValues",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "expired",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "quote",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "remaining",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256[]",
                "name": "_ids",
                "type": "uint256[]"
            }
        ],
        "name": "notesInfo",
        "outputs": [
            {
                "internalType": "bytes32[2][]",
                "name": "stores",
                "type": "bytes32[2][]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_user",
                "type": "address"
            }
        ],
        "name": "notesOf",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ownerOf",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "partialpaidingInfo",
        "outputs": [
            {
                "internalType": "bytes32[5]",
                "name": "store",
                "type": "bytes32[5]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_note",
                "type": "uint256"
            },
            {
                "internalType": "bool",
                "name": "_rebasing",
                "type": "bool"
            }
        ],
        "name": "redeem",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "payout",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_user",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "_rebasing",
                "type": "bool"
            }
        ],
        "name": "redeemAll",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "payout",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_user",
                "type": "address"
            }
        ],
        "name": "redeemablesFor",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256",
                "name": "total",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_note",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "_user",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "_redeem",
                "type": "bool"
            }
        ],
        "name": "repay",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "paid",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_address",
                "type": "address"
            }
        ],
        "name": "sendReward",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "_approved",
                "type": "bool"
            }
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_approved",
                "type": "address"
            }
        ],
        "name": "setApproved",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "toggleUseBacking",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "tokenOfOwnerByIndex",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "total",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "treasury",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "staking",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "useBacking",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_address",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "_enabled",
                "type": "bool"
            }
        ],
        "name": "whitelistOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
