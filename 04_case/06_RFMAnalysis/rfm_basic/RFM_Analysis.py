# _*_ coding:utf-8 _*_
import pandas as pd

"""
@author: Hayes Wong
@email: 616132717@qq.com
@file: RFM_Analysis
@time: 2020/05/24 22:17
"""

"""
Description: Construct RFM based on user consumption data for user grouping
"""

def get_rfm(df):
    df = df.loc[df['订单状态'] == '交易成功', :]

    # 构造R/F/M值
    # 构造R
    df_r = df[['买家昵称', '付款日期', '实付金额']]
    r = df_r.groupby('买家昵称')['付款日期'].max().reset_index()
    r['R'] = (pd.to_datetime('2019-07-30') - r['付款日期']).dt.days
    r = r[['买家昵称', 'R']]

    # 构造F
    # 引入日期标签作为辅助
    df_date = df.copy()
    df_date.loc[:, '日期标签'] = df_date.loc[:, '付款日期'].astype(str).str[:10]
    # df_date = df_date.set_index('日期标签')
    df['日期标签'] = df_date['日期标签']
    dup_f = df.groupby(['买家昵称', '日期标签'])['付款日期'].count().reset_index()
    f = dup_f.groupby('买家昵称')['付款日期'].count().reset_index()
    f.columns = ['买家昵称', 'F']

    # 构造M
    sum_m = df.groupby('买家昵称')['实付金额'].sum().reset_index()
    sum_m.columns = ['买家昵称', '总支付金额']
    combine_fm = pd.merge(sum_m, f, left_on='买家昵称', right_on='买家昵称', how='inner')
    combine_fm['M'] = combine_fm['总支付金额'] / combine_fm['F']

    # 合并RFM
    rfm = pd.merge(r, combine_fm, left_on='买家昵称', right_on='买家昵称', how='inner')
    rfm = rfm[['买家昵称', 'R', 'F', 'M']]

    # 计算rfm的score值
    rfm['R-Score'] = pd.cut(rfm['R'], bins=[0, 30, 60, 90, 120, 10000], labels=[5, 4, 3, 2, 1], right=False).astype(
        float)
    rfm['F-Score'] = pd.cut(rfm['F'], bins=[1, 2, 3, 4, 5, 10000], labels=[1, 2, 3, 4, 5], right=False).astype(float)
    rfm['M-Score'] = pd.cut(rfm['M'], bins=[0, 50, 100, 150, 200, 100000], labels=[1, 2, 3, 4, 5], right=False).astype(
        float)

    # 将rfm的分数值与各自平均值作对比，对客户进行分层，将客户分为8个类别
    rfm['R是否大于均值'] = (rfm['R-Score'] > rfm['R-Score'].mean()) * 1
    rfm['F是否大于均值'] = (rfm['F-Score'] > rfm['F-Score'].mean()) * 1
    rfm['M是否大于均值'] = (rfm['M-Score'] > rfm['M-Score'].mean()) * 1

    # 构建合并指标，为客户类别打标签
    rfm['客户数值'] = rfm['R是否大于均值'] * 100 + rfm['F是否大于均值'] * 10 + rfm['M是否大于均值'] * 1
    rfm['客户类型'] = rfm['客户数值'].apply(transform_label)

    label_count = rfm['客户类型'].value_counts().reset_index()
    label_count.columns = ['客户类型', '人数']
    label_count['人数占比'] = label_count['人数'] / label_count['人数'].sum()

    rfm['付款总金额'] = rfm['F'] * rfm['M']
    rfm_money = rfm.groupby('客户类型')['付款总金额'].sum().reset_index()
    rfm_money.columns = ['客户类型', '消费金额']
    rfm_money['金额占比'] = rfm_money['消费金额'] / rfm_money['消费金额'].sum()

    label_result = label_count.merge(rfm_money)
    writer = pd.ExcelWriter('RFM_Analysis_Result.xlsx')
    label_result.to_excel(excel_writer=writer, sheet_name='RFM-result2', index=0)
    writer.save()
    writer.close()


def transform_label(x):
    if x == 111:
        label = '重要价值客户'
    elif x == 110:
        label = '消费潜力客户'
    elif x == 101:
        label = '频次深耕客户'
    elif x == 100:
        label = '新客户'
    elif x == 11:
        label = '重要价值流失预警客户'
    elif x == 10:
        label = '一般客户'
    elif x == 1:
        label = '高消费唤回客户'
    elif x == 0:
        label = '流失客户'
    return label


if __name__ == '__main__':
    df_raw = pd.read_excel('../00_dataset/RFM data.xlsx')
    get_rfm(df_raw)