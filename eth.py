"""
Author: kashjack kashjack@163.com
Date: 2023-04-07 15:19:35
LastEditors: kashjack kashjack@163.com
LastEditTime: 2023-04-07 16:00:17
FilePath: /eth/eth.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""
from web3 import Web3
from eth_account import Account


# 实例化Web3对象
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))  # 连接到本地的以太坊客户端节点
account = Account.create()
print("Account address:", account.address)
print("Private key:", account.key.hex())
