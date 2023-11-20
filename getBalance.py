'''
Author: kashjack kashjack@163.com
Date: 2023-04-07 16:40:39
LastEditors: kashjack kashjack@163.com
LastEditTime: 2023-11-20 14:28:37
FilePath: /eth/getBalance.py
Description: 获取余额
'''


# 连接以太坊节点

# https://cloudflare-eth.com （Cloudflare 提供的免费节点）
# https://rpc.maticvigil.com （Polygon/Matic 网络的节点）
# https://bsc-dataseed1.ninicoin.io （Binance Smart Chain 网络的节点）
# https://bsc-dataseed.binance.org/
# https://bsc-dataseed1.defibit.io/
# https://bsc-dataseed1.ninicoin.io/

from web3 import Web3


# web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org"))  # 连接到BSC客户端节点


def get_eth_balance_on_erc(key):
    address1 = 'https://cloudflare-eth.com'
    address2 = 'https://web3.mytokenpocket.vip'
    w3 = Web3(Web3.HTTPProvider(address1))  # 连接到以太坊客户端节点
    balance_wei = w3.eth.get_balance(w3.to_checksum_address(key))
    balance = w3.from_wei(balance_wei, "ether")
    print(f"Balance of {key} is {balance} ETH")


def get_bnb_balance_on_bsc(key):
    address1 = 'https://bsc-dataseed.binance.org'
    address2 = 'https://bsc-dataseed1.ninicoin.io'
    w3 = Web3(Web3.HTTPProvider(address1))  # 连接到以太坊客户端节点
    balance_wei = w3.eth.get_balance(w3.to_checksum_address(key))
    balance = w3.from_wei(balance_wei, "ether")
    print(f"Balance of {key} is {balance} BNB")


def get_eth_balance_on_bsc(key):
    address1 = 'https://bsc-dataseed.binance.org'
    address2 = 'https://bsc-dataseed1.ninicoin.io'
    w3 = Web3(Web3.HTTPProvider(address1))  # 连接到节点

    # BETH 在 BSC 上的合约地址，需要确认这个地址是正确的
    beth_contract_address = "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"

    # 创建合约对象
    beth_contract = w3.eth.contract(address=beth_contract_address, abi=[{
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    }])
    balance_wei = beth_contract.functions.balanceOf(
        w3.to_checksum_address(key)).call()
    balance = w3.from_wei(balance_wei, "ether")
    print(f"Balance of {key} is {balance} ETH")


def get_okb_balance_on_x1test(key):
    address1 = 'https://testrpc.x1.tech'
    w3 = Web3(Web3.HTTPProvider(address1))  # 连接到节点
    balance_wei = w3.eth.get_balance(w3.to_checksum_address(key))
    balance = w3.from_wei(balance_wei, "ether")
    print(f"Balance of {key} is {balance} OKB")


def get_okb_balance_on_sepolia(key):
    address1 = 'https://api.sepolia.kroma.network'
    w3 = Web3(Web3.HTTPProvider(address1))  # 连接到节点
    balance_wei = w3.eth.get_balance(w3.to_checksum_address(key))
    balance = w3.from_wei(balance_wei, "ether")
    print(f"Balance of {key} is {balance} okb")


publicKey1 = '0xF45CD08e006De5257064887319a83115506c4E6F'  # 老地址
publicKey2 = '0x35cd08f1b3212cc7e664e89a9a3f718c2c31bae5'  # ok
publicKey3 = '0xb8b36245c635b65a2f2e226b0d6424ac0c75aac6'
publicKey4 = '0x7F5c764cBc14f9669B88837ca1490cCa17c31607'


# get_eth_balance_on_erc(publicKey1)
# get_bnb_balance_on_bsc(publicKey3)
get_okb_balance_on_sepolia(publicKey2)
# getBalance(publicKey2)
