"""
Author: kashjack kashjack@163.com
Date: 2023-04-07 15:19:35
LastEditors: kashjack kashjack@163.com
LastEditTime: 2023-04-07 16:25:55
FilePath: /eth/creatAccount.py
Description: 生成地址
"""

from web3 import Web3
from eth_account import Account


# 实例化Web3对象
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))  # 连接到本地的以太坊客户端节点
account = Account.create()
# 打开一个文件用于写入
f = open("account.txt", "a")
# 写入数据
f.write("-------------------------------------\n")
f.write(account.address + "\n")
f.write(account.key.hex() + "\n")
f.write("-------------------------------------\n")
