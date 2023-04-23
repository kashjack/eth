"""
Author: kashjack kashjack@163.com
Date: 2023-04-07 16:40:39
LastEditors: kashjack kashjack@163.com
LastEditTime: 2023-04-07 16:40:51
FilePath: /eth/getBalance.py
Description: 获取余额
"""
from web3 import Web3

# 连接以太坊节点

# https://cloudflare-eth.com （Cloudflare 提供的免费节点）
# https://rpc.maticvigil.com （Polygon/Matic 网络的节点）
# https://bsc-dataseed1.ninicoin.io （Binance Smart Chain 网络的节点）
# https://bsc-dataseed.binance.org/
# https://bsc-dataseed1.defibit.io/
# https://bsc-dataseed1.ninicoin.io/

web3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com"))  # 连接到以太坊客户端节点
# web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org"))  # 连接到BSC客户端节点

# 公钥地址
address = "0xF45CD08e006De5257064887319a83115506c4E6F"

# 获取余额
balance = web3.BNB.get_balance(address)

# 将余额从 Wei 转换为 Ether
# balance_in_eth = web3.eth.fromWei(balance, "ether")

print(f"Balance of {address} is {balance} BNB")
