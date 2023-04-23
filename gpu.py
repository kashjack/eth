'''
Author: kashjack kashjack@163.com
Date: 2023-04-23 19:01:09
LastEditors: kashjack kashjack@163.com
LastEditTime: 2023-04-23 19:21:30
FilePath: /eth/gpu.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.techpowerup.com/gpu-specs/geforce-rtx-4090.c3889"

# 发送GET请求
response = requests.get(url)

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(response.content, 'html.parser')

# 获取所需数据
card_name = soup.find('h1', {'class': 'specs__name'})
# core_clock = soup.find('div', {'class': 'specs__block--gpu'}
#                        ).find_all('tr')[1].find_all('td')[1].text.strip()
# mem_capacity = soup.find('div', {
#                          'class': 'specs__block--memory'}).find_all('tr')[1].find_all('td')[1].text.strip()
# mem_clock = soup.find('div', {'class': 'specs__block--memory'}
#                       ).find_all('tr')[2].find_all('td')[1].text.strip()

# 检查元素是否存在
if card_name is not None:
    card_name = card_name.text.strip()
    print(card_name)  # 调试语句
else:
    print("Card name not found")  # 调试语句

# # 创建数据框
# df = pd.DataFrame({
#     # 'Card Name': [card_name],
#     'Core Clock': [core_clock],
#     'Memory Capacity': [mem_capacity],
#     'Memory Clock': [mem_clock]
# })

# # 导出到Excel文件
# df.to_excel('gpu_specs.xlsx', index=False)
