# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np

"""
@author: Hayes Wong
@email: 616132717@qq.com
@file: TGI_index
@time: 2020/05/20 15:15
"""

"""
Description: This program is to get what is the TGI index and how to use Python 
to achieve basic TGI based on case data

TGI(Target Group Index) =  [目标群体中具有某一特征的群体所占比例/总体中具有相同特征的群体所占比例]*标准数100

"""

def get_tgi(data):
    # determine user category based on the amount paid by the user
    gp_user = data.groupby('买家昵称')['实付金额'].mean().reset_index()
    gp_user['客单类别'] = gp_user['实付金额'].apply(lambda x: '高客单' if x > 50 else '低客单')

    # combining customer data and regional data
    data_dup = data.loc[data.duplicated('买家昵称') == False, :]
    data_user_regional = pd.merge(gp_user, data_dup, left_on='买家昵称', right_on='买家昵称', how='left')

    # count the number of low and high user orders in each province and city
    data_merge = data_user_regional[['买家昵称', '客单类别', '省份', '城市']]
    stat_result = pd.pivot_table(data_merge, index=['省份', '城市'], columns='客单类别', aggfunc='count')

    # the proportion of high users per city
    tgi = pd.merge(stat_result['买家昵称']['高客单'].reset_index(), stat_result['买家昵称']['低客单'].reset_index(),
                   left_on=['省份', '城市'], right_on=['省份', '城市'], how='inner')
    tgi['总人数'] = tgi['高客单'] + tgi['低客单']
    tgi['高客单占比'] = tgi['高客单'] / tgi['总人数']

    # the proportion of the total number of high passenger orders
    total_percentage = tgi['高客单'].sum() / tgi['总人数'].sum()

    # calculate the TGI index for each city
    tgi['高客单TGI指数'] = tgi['高客单占比'] / total_percentage * 100
    tgi = tgi.sort_values('高客单TGI指数', ascending=False)

    return tgi

if __name__ == '__main__':
    df = pd.read_excel('../00_dataset/TGI index data.xlsx')
    tgi_result = get_tgi(df)
    tgi_result.to_excel('TGI.xlsx', index=0)




