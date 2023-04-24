'''
Author: kashjack kashjack@163.com
Date: 2023-04-23 19:01:09
LastEditors: kashjack kashjack@163.com
LastEditTime: 2023-04-24 18:17:07
FilePath: /eth/DIY/gpu.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

def getGpuInfo(url):

    # 发送GET请求
    response = requests.get(url)
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 获取所需数据
    title = soup.find('title').text.strip().split(' Specs')[0]
    dl = soup.find_all('dl', {'class': 'clearfix'})
    gpu_name = dl[0].find('a').text.strip()
    gpu_variant = dl[1].find('dd').text.strip()
    architecture = dl[2].find('a').text.strip()
    foundry = dl[3].find('dd').text.strip()
    process_size = dl[4].find('dd').text.strip()
    transistors = dl[5].find('dd').text.strip()
    density = dl[6].find('dd').text.strip()
    die_size = dl[7].find('dd').text.strip()
    release_date = dl[8].find('dd').text.strip()
    availability = dl[9].find('dd').text.strip()
    generation = dl[10].find('dd').text.strip()
    predecessor = dl[11].find('a').text.strip()
    production = dl[12].find('dd').text.strip()
    launch_price = dl[13].find('dd').text.strip()
    bus_interface = dl[15].find('dd').text.strip()
    base_clock = dl[17].find('dd').text.strip()
    boost_clock = dl[18].find('dd').text.strip()
    memory_clock = dl[19].find('dd').text.strip()
    memory_size = dl[20].find('dd').text.strip()
    memory_type = dl[21].find('dd').text.strip()
    memory_bus = dl[22].find('dd').text.strip()
    bandwidth = dl[23].find('dd').text.strip()
    shading_units = dl[24].find('dd').text.strip()
    tmus = dl[25].find('dd').text.strip()
    rops = dl[26].find('dd').text.strip()
    sm_count = dl[27].find('dd').text.strip()
    tensor_cores = dl[28].find('dd').text.strip()
    rt_cores = dl[29].find('dd').text.strip()
    l1_cache = dl[30].find('dd').text.strip()
    l2_cache = dl[31].find('dd').text.strip()
    pixel_rate = dl[32].find('dd').text.strip()
    texture_rate = dl[33].find('dd').text.strip()
    fp16 = dl[34].find('dd').text.strip()
    fp32 = dl[35].find('dd').text.strip()
    fp64 = dl[36].find('dd').text.strip()
    slot_width = dl[37].find('dd').text.strip()
    length = dl[38].find('dd').text.strip()
    width = dl[39].find('dd').text.strip()
    height = dl[40].find('dd').text.strip()
    tdp = dl[41].find('dd').text.strip()
    suggested_psu = dl[42].find('dd').text.strip()
    outputs = dl[43].find('dd').text.strip()
    power_connectors = dl[44].find('dd').text.strip()
    directX = dl[46].find('dd').text.strip()
    openGL = dl[47].find('dd').text.strip()
    openCL = dl[48].find('dd').text.strip()
    vulkan = dl[49].find('dd').text.strip()
    cuda = dl[50].find('dd').text.strip()
    # shader_model = dl[51].find('dd').text.strip()
    print(dl[13])

    td = soup.find('td', {'class': 'p'})
    text = td.text.split('\r\n')
    english_info = [x for x in text if x != '' and x != '\r']

    # 创建数据框
    df = pd.DataFrame({
        'title': [title],
        'gpu_name': [gpu_name],
        'gpu_variant': [gpu_variant],
        'architecture': [architecture],
        'foundry': [foundry],
        'process_size': [process_size],
        'transistors': [transistors],
        'density': [density],
        'die_size': [die_size],
        'release_date': [release_date],
        'availability': [availability],
        'generation': [generation],
        'predecessor': [predecessor],
        'production': [production],
        'launch_price': [launch_price],
        'bus_interface': [bus_interface],
        'base_clock': [base_clock],
        'boost_clock': [boost_clock],
        'memory_clock': [memory_clock],
        'memory_size': [memory_size],
        'memory_type': [memory_type],
        'memory_bus': [memory_bus],
        'bandwidth': [bandwidth],
        'shading_units': [shading_units],
        'tmus': [tmus],
        'rops': [rops],
        'sm_count': [sm_count],
        'tensor_cores': [tensor_cores],
        'rt_cores': [rt_cores],
        'l1_cache': [l1_cache],
        'l2_cache': [l2_cache],
        'slot_width': [slot_width],
        'length': [length],
        'width': [width],
        'height': [height],
        'tdp': [tdp],
        'suggested_psu': [suggested_psu],
        'outputs': [outputs],
        'power_connectors': [power_connectors],
        'directX': [directX],
        'openGL': [openGL],
        'openCL': [openCL],
        'vulkan': [vulkan],
        'cuda': [cuda],
        'shader_model': [shader_model],
        'pixel_rate': [pixel_rate],
        'texture_rate': [texture_rate],
        'fp16': [fp16],
        'fp32': [fp32],
        'fp64': [fp64],
    })
    # 覆盖Excel文件


    # 读取原有Excel数据
    try:
        df_old = pd.read_excel('/Users/mac/Desktop/GitHub/eth/DIY/gpu_specs.xlsx')
    except FileNotFoundError:
        df_old = pd.DataFrame()

    # 追加新数据到原有数据框
    df_new = df
    df_all = pd.concat([df_old, df_new], ignore_index=True)

    # 写入Excel
    with pd.ExcelWriter('/Users/mac/Desktop/GitHub/eth/DIY/gpu_specs.xlsx', mode='w') as writer:
        df_all.to_excel(writer, index=False)


urls = [
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-4090.c3889",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-7900-xtx.c3941",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-4080.c3888",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-7900-xt.c3912",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-3090-ti.c3829",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-4070-ti.c3950",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-3090.c3622",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6950-xt.c3875",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-3080-ti.c3735",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6900-xt.c3481",
        "https://www.techpowerup.com/gpu-specs/geforce-rtx-4070.c3924",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-3080.c3621",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6800-xt.c3694"
        ]

for url in urls:
    getGpuInfo(url)
    time.sleep(5)

