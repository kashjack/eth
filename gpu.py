'''
Author: kashjack kashjack@163.com
Date: 2023-04-23 19:01:09
LastEditors: kashjack kashjack@163.com
LastEditTime: 2023-04-24 00:39:08
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
GPU_Name = soup.find('dl', {'class': 'clearfix'}).find('a').text.strip()
GPU_Variant = soup.find_all(
    'dl', {'class': 'clearfix'})[1].find('dd').text.strip()


# 检查元素是否存在
# if GPU_Variant is not None:
#     print(GPU_Variant)  # 调试语句
# else:
#     print("not found")  # 调试语句

# 创建数据框
df = pd.DataFrame({
    'GPU Name': [GPU_Name],
    'GPU Variant': [GPU_Variant],
})

# 导出到Excel文件
df.to_excel('gpu_specs.xlsx', index=False)
