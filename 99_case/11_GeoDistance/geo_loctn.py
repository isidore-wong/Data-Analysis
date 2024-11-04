# -*- coding: utf-8 -*-
"""
@author: Hayes Wong
@file: geo_loctn.py
@time: 2024/10/29 16:19
@version: 1.0
"""

"""
Description:调用高德API，通过经纬度定位地理位置信息，计算两点间距离
"""

import requests
import pandas as pd
from geopy.distance import geodesic
import time

def get_key(file_path):
    """
        : function description:获取高德地图API的key
        : param file_path:key文件的存储位置
        : return :key
    """
    with open(file_path, 'r') as f:
        key = f.read()
        return key

def basic_process(file_path):
    """
        : function description:读取数据，并对数据做基础处理
        : param file_path:data文件的存储位置
        : return :处理后的数据
    """
    basic_data = pd.read_excel(file_path)
    # 数据类型转为字符串格式
    for column in basic_data.columns:
        basic_data[column] = basic_data[column].astype('string')
        # basic_data[column] = basic_data[column].str.strip()

    # 坐标点的经纬度
    basic_data['coord1'] = pd.DataFrame(basic_data['LONG1'] + ',' + basic_data['LAT1'])
    basic_data['coord2'] = pd.DataFrame(basic_data['LONG2'] + ',' + basic_data['LAT2'])
    return basic_data

def coord_location(api_key, coord_data):
    """
        : function description:通过经纬度获取地理位置信息
        : param api_key:高德开放平台API的应用key
        : param coord_data:地理经纬度坐标
        : return :逆地理编码后的地址信息
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    # coord_info存储经过逆地理编码后的地址信息
    coord_info = list()
    data_len = len(coord_data['coord1'])
    
    for i in range(data_len):
        loctn_coord = coord_data['coord1'][i]
        req_url = f"https://restapi.amap.com/v3/geocode/regeo?key={api_key}&location={loctn_coord}&extensions=base&roadlevel=0"
        resp_json = requests.get(req_url)
    
        if resp_json.status_code == 200:
             loctn_json = resp_json.json()
             if loctn_json['status'] == '1':
                 adrs = loctn_json['regeocode']['formatted_address']
                 coord_info.append(adrs)
                 # print(i, adrs)
             else:
                print(f"Error: {loctn_json['info']}")
        else:
            print(f"HTTP Error: {resp_json.status_code}")
    
        # 免费API每秒并发量为3，日配额5000，故对线程做1秒的休眠，后期可根据实际情况调整
        time.sleep(1)

    coord_data['adrs'] = pd.DataFrame(coord_info)
    return coord_data

def calcut_dist(coord_data):
    """
    : function description:通过经纬度计算两点间的距离
    : param coord1:地点1的经纬度
    : param coord2:地点2的经纬度
    : return :两点间的距离
    """
    dist = list()
    data_len = len(coord_data)
    # 计算两点之间的距离
    for i in range(data_len):
        # print(i, coord_data['LAT1'][i], coord_data['LONG1'][i], coord_data['LAT2'][i], coord_data['LONG2'][i])
        distance = geodesic((coord_data['LAT1'][i], coord_data['LONG1'][i]), (coord_data['LAT2'][i], coord_data['LONG2'][i])).kilometers
        # 保留两位小数
        distance = round(distance, 2)
        # print("两点之间的距离为: {}千米".format(distance))
        dist.append(distance)
    coord_data['dist_km'] = pd.DataFrame(dist)
    return coord_data


if __name__ == "__main__":
    key_path = ('./rawdata/key.txt')
    api_key = get_key(key_path)
    data_path = ('./rawdata/py_test.xlsx')
    basic_procsd = basic_process(data_path)
    coord_adrs = coord_location(api_key, basic_procsd)
    coord_adrs.to_excel('./output/coord_adrs.xlsx')
    coord_dist = calcut_dist(coord_adrs)
    coord_dist.to_excel('./output/coord_dist.xlsx')
