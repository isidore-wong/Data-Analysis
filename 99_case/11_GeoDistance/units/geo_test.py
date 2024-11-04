# -*- coding: utf-8 -*-
"""
@author: Hayes Wong
@file: geo_test.py
@time: 2024/10/29 16:35
@version:
"""

"""
Description:测试使用
"""

import requests
import os
import pandas as pd
import time

# file_path = os.path.dirname(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath('../rawdata/key.txt')))
key_path = os.path.abspath('../rawdata/key.txt')
##print(key_path)
with open(key_path, 'r') as f:
    api_key = f.read()
    print(api_key)

data_path = os.path.abspath('../rawdata/py_test.xlsx')
raw_data = pd.read_excel(data_path)
raw_data['coord1'] = pd.DataFrame(raw_data['LONG1'].astype('string') + ',' + raw_data['LAT1'].astype('string'))
data_len = len(raw_data['coord1'])

for i in range (data_len):
    print(i, raw_data['coord1'][i])
    loctn_coord = raw_data['coord1'][i]
    req_url = f"https://restapi.amap.com/v3/geocode/regeo?key={api_key}&location={loctn_coord}&extensions=base&roadlevel=0"
    resp_json = requests.get(req_url)

    if resp_json.status_code == 200:
         loctn_json = resp_json.json()
         if loctn_json['status'] == '1':
             print(i ,loctn_json['regeocode']['formatted_address'])
         else:
            print(f"Error: {loctn_json['info']}")
    else:
        print(f"HTTP Error: {resp_json.status_code}")

    # 免费API每秒并发量为3，对线程做1秒的休眠
    time.sleep(1)

# print(loctn_adrs)

