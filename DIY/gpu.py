'''
Author: kashjack kashjack@163.com
Date: 2023-04-23 19:01:09
LastEditors: kashjack kashjack@163.com
LastEditTime: 2023-04-27 15:23:03
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
    videoName = soup.find('title').text.strip().split(' Specs')[0]
    dls = soup.find_all('dl', {'class': 'clearfix'})

    sm_count = ''
    tensor_cores = ''
    cuda = ''
    nvenc = ''
    nvdec = ''
    purevideo = ''
    vdpau = ''
    score = ''
    availability = ''
    height = ''
    rayTracingCores = ''
    length = ''
    rt_cores = ''
    l1_cache = ''

    for dl in dls:
        if('GPU Name' in dl.text.strip()):
            gpu_name = dl.find('a').text.strip()
        if('GPU Variant' in dl.text.strip()):
            gpu_variant = dl.find('dd').text.strip()
        if('Architecture' in dl.text.strip()):
            architecture = dl.find('dd').text.strip()
        if('Foundry' in dl.text.strip()):
            foundry = dl.find('dd').text.strip()
        if('Process Size' in dl.text.strip()):
            process_size = dl.find('dd').text.strip()
        if('Transistors' in dl.text.strip()):
            transistors = dl.find('dd').text.strip()
        if('Density' in dl.text.strip()):
            density = dl.find('dd').text.strip()
        if('Die Size' in dl.text.strip()):
            die_size = dl.find('dd').text.strip()
        if('Release Date' in dl.text.strip()):
            release_date = dl.find('dd').text.strip()
        if('Availability' in dl.text.strip()):
            availability = dl.find('dd').text.strip()
        if('Generation' in dl.text.strip()):
            generation = dl.find('a').text.strip()
        if('Production' in dl.text.strip()):
            production = dl.find('dd').text.strip()
        if('Launch Price' in dl.text.strip()):
            launch_price = dl.find('dd').text.strip()
        if('Bus Interface' in dl.text.strip()):
            bus_interface = dl.find('dd').text.strip()
        if('Base Clock' in dl.text.strip()):
            base_clock = dl.find('dd').text.strip()
        if('Boost Clock' in dl.text.strip()):
            boost_clock = dl.find('dd').text.strip()
        if('Memory Clock' in dl.text.strip()):
            memory_clock = dl.find('dd').text.strip()
        if('Memory Size' in dl.text.strip()):
            memory_size = dl.find('dd').text.strip()
        if('Memory Type' in dl.text.strip()):
            memory_type = dl.find('dd').text.strip()
        if('Memory Bus' in dl.text.strip()):
            memory_bus = dl.find('dd').text.strip()
        if('Bandwidth' in dl.text.strip()):
            bandwidth = dl.find('dd').text.strip()
        if('Shading Units' in dl.text.strip()):
            shading_units = dl.find('dd').text.strip()
        if('TMUs' in dl.text.strip()):
            tmus = dl.find('dd').text.strip()
        if('ROPs' in dl.text.strip()):
            rops = dl.find('dd').text.strip()
        if('SM Count' in dl.text.strip()):
            sm_count = dl.find('dd').text.strip()
        if('Tensor Cores' in dl.text.strip()):
            tensor_cores = dl.find('dd').text.strip()
        if('RT Cores' in dl.text.strip()):
            rt_cores = dl.find('dd').text.strip()
        if('L1 Cache' in dl.text.strip()):
            l1_cache = dl.find('dd').text.strip()
        if('L2 Cache' in dl.text.strip()):
            l2_cache = dl.find('dd').text.strip()
        if('Slot Width' in dl.text.strip()):
            slot_width = dl.find('dd').text.strip()
        if('Length' in dl.text.strip()):
            length = dl.find('dd').text.strip()
        if('Width' in dl.text.strip()):
            width = dl.find('dd').text.strip()
        if('Height' in dl.text.strip()):
            height = dl.find('dd').text.strip()
        if('TDP' in dl.text.strip()):
            tdp = dl.find('dd').text.strip()
        if('Suggested PSU' in dl.text.strip()):
            suggested_psu = dl.find('dd').text.strip()
        if('Outputs' in dl.text.strip()):
            outputs = dl.find('dd').text.strip()
        if('Power Connectors' in dl.text.strip()):
            power_connectors = dl.find('dd').text.strip()
        if('DirectX' in dl.text.strip()):
            directX = dl.find('dd').text.strip()
        if('OpenGL' in dl.text.strip()):
            openGL = dl.find('dd').text.strip()
        if('OpenCL' in dl.text.strip()):
            openCL = dl.find('dd').text.strip()
        if('Vulkan' in dl.text.strip()):
            vulkan = dl.find('dd').text.strip()
        if('CUDA' in dl.text.strip()):
            cuda = dl.find('dd').text.strip()
        if('Shader Model' in dl.text.strip()):
            shader_model = dl.find('dd').text.strip()
        if('Pixel Rate' in dl.text.strip()):
            pixel_rate = dl.find('dd').text.strip()
        if('Texture Rate' in dl.text.strip()):
            texture_rate = dl.find('dd').text.strip()
        if('FP16' in dl.text.strip()):
            fp16 = dl.find('dd').text.strip()
        if('FP32' in dl.text.strip()):
            fp32 = dl.find('dd').text.strip()
        if('FP64' in dl.text.strip()):
            fp64 = dl.find('dd').text.strip()

    td = soup.find('td', {'class': 'p'})
    # print(td)
    text = td.text.split('\r\n')
    infos = [x for x in text if x != '' and x != '\r']
    for info in infos:
        if ('NVENC' in info):
            nvenc = info.split(':')[-1]
        if ('NVDEC' in info):
            nvdec = info.split(':')[-1]
        if ('PureVideo' in info):
            purevideo = info.split(':')[-1]
        if ('VDPAU' in info):
            vdpau = info.split(':')[-1]
        if ('Ray Tracing Cores' in info):
            rayTracingCores = info.split(':')[-1]
        if ('Tensor Cores' in info):
            score = info.split(':')[-1]


    # 创建数据框
    df = pd.DataFrame({
        'videoName': [videoName],
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
        'nvenc': [nvenc],
        'nvdec': [nvdec],
        'purevideo': [purevideo],
        'vdpau': [vdpau],
        'rayTracingCores': [rayTracingCores],
        'score': [score],
    })


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
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-4070.c3924",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-3080.c3621",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6800-xt.c3694",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6800.c3713",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-3070-ti.c3675",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-3070.c3674",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6750-xt.c3879",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-2080-ti.c3305",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6700-xt.c3695",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-3060-ti.c3681",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-2080-super.c3439",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-2080.c3224",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6650-xt.c3898",
        # "https://www.techpowerup.com/gpu-specs/radeon-rx-6600-xt.c3774",
        # "https://www.techpowerup.com/gpu-specs/geforce-rtx-2070-super.c3440",
        # "https://www.techpowerup.com/gpu-specs/geforce-gtx-1080-ti.c2877",
        # "https://www.techpowerup.com/gpu-specs/titan-x-pascal.c2863",
        # "https://www.techpowerup.com/gpu-specs/radeon-vii.c3358",
        "https://www.techpowerup.com/gpu-specs/radeon-rx-5700-xt.c3339",
        "https://www.techpowerup.com/gpu-specs/geforce-rtx-3060-12-gb.c3682",
        "https://www.techpowerup.com/gpu-specs/geforce-rtx-2070.c3252",
        "https://www.techpowerup.com/gpu-specs/geforce-rtx-2060-super.c3441",
        "https://www.techpowerup.com/gpu-specs/radeon-rx-6600.c3696",
        "https://www.techpowerup.com/gpu-specs/radeon-rx-5700.c3437",
        "https://www.techpowerup.com/gpu-specs/geforce-rtx-2060.c3310",
        "https://www.techpowerup.com/gpu-specs/geforce-gtx-1080.c2839",
        "https://www.techpowerup.com/gpu-specs/radeon-rx-vega-64.c2871",
        "https://www.techpowerup.com/gpu-specs/radeon-rx-5600-xt.c3474",
        "https://www.techpowerup.com/gpu-specs/geforce-gtx-1070-ti.c3010",
        "https://www.techpowerup.com/gpu-specs/radeon-rx-vega-56.c2993",
        "https://www.techpowerup.com/gpu-specs/geforce-rtx-3050-8-gb.c3858",
        "https://www.techpowerup.com/gpu-specs/geforce-gtx-1070.c2840",
        "https://www.techpowerup.com/gpu-specs/geforce-gtx-1660-ti.c3364",
        "https://www.techpowerup.com/gpu-specs/geforce-gtx-1660-super.c3458",
        ]

for url in urls:
    getGpuInfo(url)
    # time.sleep(10)

