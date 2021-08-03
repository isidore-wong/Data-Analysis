# _*_ coding:utf-8 _*_
import numpy as np
import pandas as pd

"""
@author: Hayes Wong
@email: 616132717@qq.com
@file: cohort_analysis
@time: 2020/05/21 18:43
"""

"""
Description: using Python to realize cohort analysis.
"""

def cohort_analysis(df_data):
    '''
    Calculate retention and retention rate over the same period。
    :param df_data: raw data
    :param df_f: retention over the same period
    :param df_l: retention rate over the same period
    :return:
    '''

    df_data.drop(index=df_data[df_data['订单状态'] == '交易失败'].index, axis=1, inplace=True)
    # get the time of first order time per customer
    df_f = df_data.groupby(by='客户昵称')['付款时间'].min().to_frame(name='首单时间')
    df_f.reset_index(inplace=True)

    df_f = df_data[['客户昵称', '付款时间']].merge(df_f)

    # group by the first order time and payment time to get the number of unique customers in each time period
    df_f = df_f.groupby(by=[pd.Grouper(key='首单时间', freq='m'),
                            pd.Grouper(key='付款时间', freq='m')])['客户昵称'].nunique()

    # transpose composite indexed series into dataframe
    df_f = df_f.unstack()

    # align the number of customers in the first month
    for i in range(len(df_f.index)):
        df_f.iloc[i] = df_f.iloc[i].shift(periods=-i)

    # reset columns
    df_f.columns = ['本月新增', '+1月', '+2月', '+3月', '+4月', '+5月']

    # calculate retention rate
    df_l = df_f.apply(count_per, axis=0, args=(df_f['本月新增'],))
    df_l['本月新增'] = df_f['本月新增']

    return df_f, df_l

def count_per(s, dx):
    a = [f'{i}%' if str(i) != 'nan' else 0 for i in round((s / dx) * 100, 2)]
    return a

if __name__ == '__main__':
    df = pd.read_excel('../00_dataset/cohort analysis data.xlsx')
    retention_num, retention_rate = cohort_analysis(df)
    retention_num.to_excel('留存量分析表.xlsx')
    retention_rate.to_excel('留存率分析表.xlsx')

