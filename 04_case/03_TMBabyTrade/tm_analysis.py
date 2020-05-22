# _*_ coding:utf-8 _*_
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
import seaborn as sns

"""
@author: Hayes Wong
@email: 616132717@qq.com
@file: tm_analysis
@time: 2020/05/22 16:33
"""

"""
Description: Analysis of sales data of Tmall mum_baby products
"""

# clean data
def data_clean():
    df_baby = pd.read_csv('../00_dataset/tm_baby_trade/(sample)sam_tianchi_mum_baby.csv')
    df_trade = pd.read_csv('../00_dataset/tm_baby_trade/(sample)sam_tianchi_mum_baby_trade_history.csv')
    df = df_trade.merge(df_baby, how='outer', on='user_id')
    df['day'] = df['day'].astype('str')
    df['day'] = pd.to_datetime(df['day'], errors='ignore')

    print(df.info())
    # df.describe()
    # View quartile and standard of df['buy_mount']
    print(df['buy_mount'].describe())

    # clean the outlier of df['buy_mount'] which is higher than 30
    df.drop(index=df[df['buy_mount'] > 30].index, inplace=True)
    print(df['buy_mount'].describe())
    return df

def YOY_2014(df):
    '''
    Calculate year-on-year growth rate in 2014
    :param df:
    :return:
    '''
    df['time_label'] = df['day'].dt.year
    df = df.groupby(pd.Grouper(key='time_label')).sum().sort_values(by='time_label')
    df['yoy_growth_rate'] = df['buy_mount'].pct_change()
    print(df[['buy_mount', 'yoy_growth_rate']])

def annual_sales_trend(df):
    '''
    Observe the monthly sales trend of each year
    :param df:
    :return:
    '''
    df = df.groupby(pd.Grouper(key='day', freq='m')).sum()
    df['month'] = df.index.month
    df['year'] = df.index.year
    df = df[['year', 'month', 'buy_mount']]

    # extract monthly sales
    _x = df[df['year'] == 2014]['month']
    _x_2012 = df[df['year'] == 2012]['month']
    # _x_2013 = df[df['year'] == 2013]['month']
    _x_2015 = df[df['year'] == 2015]['month']
    _y_2012 = df[df['year'] == 2012]['buy_mount']
    _y_2013 = df[df['year'] == 2013]['buy_mount']
    _y_2014 = df[df['year'] == 2014]['buy_mount']
    _y_2015 = df[df['year'] == 2015]['buy_mount']
    print(_y_2014.sum() / _y_2013.sum() - 1)

    # extract monthly growth rate
    df_YOY = pd.DataFrame(
        {
            '2013': _y_2013.tolist(),
            '2014': _y_2014.tolist(),
        },
        index=_x
    )
    _y_2012.index = _x_2012
    _y_2015.index = _x_2015
    df_YOY = df_YOY.join(_y_2012)
    df_YOY = df_YOY.join(_y_2015, lsuffix='2012', rsuffix='2015')
    df_YOY.columns = ['2013', '2014', '2012', '2015']
    df_YOY = df_YOY.loc[:, ['2012', '2013', '2014', '2015']]
    df_YOY = df_YOY.pct_change(axis=1) * 100

    # plot figure
    plt.figure(figsize=(32, 9), dpi=160)
    # monthly figure
    ax1 = plt.subplot(1, 2, 1)

    plt.plot(_x_2012, _y_2012, label='2012年')
    plt.plot(_x, _y_2013, label='2013年')
    plt.plot(_x, _y_2014, label='2014年')
    plt.plot(_x_2015, _y_2015, label='2015年')
    plt.title('月度销量情况')
    plt.grid(alpha=0.6)
    plt.xticks(_x, _x)
    plt.xlabel('月份')
    plt.ylabel('销量（件）')
    plt.legend(loc='upper left')

    # monthly growth line chart
    ax1 = plt.subplot(1, 2, 2)
    _y_2015 = df_YOY[df_YOY['2015'] != 0]['2015']
    _x_2015 = _x[:len(_y_2015.values)]
    plt.plot(_x, df_YOY['2013'], label='2013年')
    plt.plot(_x, df_YOY['2014'], label='2014年')
    plt.plot(_x_2015, _y_2015, label='2015年')
    plt.title('月度同比增速')
    plt.xticks(_x)
    plt.xlabel('月份')
    plt.ylabel('同比增速（百分比）')
    plt.legend()
    plt.grid(alpha=0.6)
    plt.show()
    plt.savefig('images/01_月度情况.svg')

def annual_trend_before_sf(df):
    '''
    the sales trends of the 30 days before the Spring Festival in each year
    :param df:
    :return:
    '''
    df = df.groupby(by=pd.Grouper(key='day', freq='D')).sum()['buy_mount']
    _y_2013 = df['2013-1-10':'2013-2-15']
    _y_2014 = df['2014-1-1':'2014-2-6']
    _y_2015 = df['2015-1':'2015-2'][:-17:-1][::-1]
    _x = [i for i in range(len(_y_2013))]
    _x_label = ['闰月初一', '闰月初二', '闰月初三', '闰月初四', '闰月初五', '闰月初六', '闰月初七', '闰月初八', '闰月初九', '闰月初十', '闰月十一', '闰月十二', '闰月十三',
                '闰月十四', '闰月十五', '闰月十六', '闰月十七', '闰月十八', '闰月十九', '闰月二十', '闰月廿一', '闰月廿二', '闰月廿三', '闰月廿四', '闰月廿五', '闰月廿六',
                '闰月廿七', '闰月廿八', '闰月廿九', '闰月三十', '正月初一', '正月初二', '正月初三', '正月初四', '正月初五', '正月初六', '正月初七', '正月初八']

    # Line chart-comparison of daily sales on the 30th day before the Spring Festival
    plt.figure(figsize=(32, 9), dpi=160)
    ax1 = plt.subplot(1, 2, 2)
    plt.plot(_x, _y_2013, label='2013年')
    plt.plot(_x, _y_2014, label='2014年')
    plt.plot(_x[:len(_y_2015)], _y_2015, label='2015年')
    plt.xticks(_x, _x_label, rotation=45)
    plt.legend()
    plt.title('2013-2015年春节前30日每日销量情况比较')
    plt.grid(alpha=0.5)

    df_1 = pd.DataFrame(
        {
            '2013': _y_2013[:16].sum(),
            '2014': _y_2014[:16].sum(),
            '2015': _y_2015.sum(),
        },
        index=[0]
    )
    df_1 = pd.concat([df_1, df_1.pct_change(axis=1)])
    df_1.index = ['销量', '同比增速']
    _x = df_1.columns

    # Comparison of sales from the 30th to the 13th before the Spring Festival
    ax2 = plt.subplot(1, 2, 1)
    plt.bar(_x, df_1.loc['销量'], width=0.3, color='#ffaaa5', label='销量（左轴）')
    for x, y_2 in zip(_x, df_1.loc['销量']):
        plt.text(x, y_2 + 10, y_2, ha='center')
    ax2.set_ylabel('销量')
    ax2.set_xlabel('年份')
    plt.title('2013-2015年闰月初一到十五销量同比情况')
    plt.legend(loc='upper left')
    ax3 = ax2.twinx()
    _y_YOY = round((df_1.loc['同比增速'] * 100), 1)
    plt.plot(_x, _y_YOY, color='#a8e6cf', label='同比增速（右轴）')
    _y_YOY = _y_YOY.dropna()
    for x, y in zip(_y_YOY.index, _y_YOY):
        plt.text(x, y + 0.1, f'{y}%', ha='left')
    ax3.set_ylabel('同比增速')
    plt.legend(bbox_to_anchor=(0, 0.96), loc='upper left')
    plt.show()
    plt.savefig('images/02_2013-2015年春节前30日销量情况比较.svg')

def find_reason(df):
    df = df.groupby([pd.Grouper(key='day',freq='D'),'cat1']).sum()['buy_mount']
    df_2014 = df.loc['2014-1-1':'2014-1-16'].unstack()
    df_2015 = df.loc['2015-1-21':].unstack()
    df = pd.DataFrame({'2014':df_2014.sum(),'2015': df_2015.sum()},index=df_2015.columns)
    df['yoy'] = df.pct_change(axis=1)['2015']*100

    _x=np.arange(len(df.index))
    width=0.35
    color=sns.color_palette('Blues',3)
    plt.figure(figsize=(16,9),dpi=160)
    ax=plt.subplot()
    rects1=plt.bar(_x-width/2,df['2014'],width,label='2014年销量（左轴）',color=color[0])
    rects2=plt.bar(_x+width/2,df['2015'],width,label='2015年销量（左轴）',color=color[1])
    ax.set_ylabel('销量')
    ax.set_xlabel('产品大类')
    plt.title('2014-2015年春节前30-14日各分类销量情况')
    plt.legend(loc='upper right')
    ax2=ax.twinx()
    plt.plot(_x, df['yoy'], label='同比增速（右轴）', color=color[2])
    ax2.set_ylabel('同比增速（%）')
    for x,y in zip(_x,round(df['yoy'],2)):
        plt.text(x, y+1, f'{y}%',ha='left')
    plt.legend(bbox_to_anchor=(1,0.9375), loc='upper right')
    plt.xticks(_x,df.index)
    plt.savefig('images/03_春节前各大类同比变化.svg')
    plt.show()

def marketing_plan_2015(df):
    df = df.groupby(by=[pd.Grouper(key=('day'), freq='D'), 'cat1']).sum()['buy_mount']
    # .unstack()方法将复合索引的series转化为dataframe
    # 此方法也可以用于dataframe的行列转换
    df_2013 = df.loc['2013-1-10':'2013-2-15'].unstack()
    df_2014 = df.loc['2014-1-1':'2014-2-6'].unstack()
    df_2015 = df.loc['2015-1-21':].unstack()

    _x_label = ['闰月初一', '闰月初二', '闰月初三', '闰月初四', '闰月初五', '闰月初六', '闰月初七', '闰月初八', '闰月初九', '闰月初十', '闰月十一', '闰月十二', '闰月十三',
                '闰月十四', '闰月十五', '闰月十六', '闰月十七', '闰月十八', '闰月十九', '闰月二十', '闰月廿一', '闰月廿二', '闰月廿三', '闰月廿四', '闰月廿五', '闰月廿六',
                '闰月廿七', '闰月廿八', '闰月廿九', '闰月三十', '正月初一', '正月初二', '正月初三', '正月初四', '正月初五', '正月初六', '正月初七', '正月初八']
    _x = range(df_2013.shape[0])
    _x_1 = range(df_2015.shape[0])
    plt.figure(figsize=(32, 27), dpi=160)
    for i in range(df_2015.shape[1]):
        ax = plt.subplot(3, 2, i + 1)
        plt.plot(_x_1, df_2015.iloc[:, i], label='2015')
        plt.plot(_x, df_2014.iloc[:, i], label='2014')
        plt.plot(_x, df_2013.iloc[:, i], label='2013')
        plt.xticks(_x, _x_label, rotation=45)
        plt.legend()
        plt.grid(alpha=0.6)
        plt.title(f'{df_2015.columns[i]}大类销量情况')
    plt.show()
    plt.savefig('images/04_各类产品销量.svg')

def main():
    # 打开文件，做基本数据清洗
    df = data_clean()

    # 统计14年同比增速
    YOY_2014(df)

    # 观察以年为维度的
    annual_sales_trend(df)

    # 查看2015年2月数据状况
    annual_trend_before_sf(df)

    # 对比产品增长情况，确定销量低的问题点
    find_reason(df)

    # 提取春节前指定日期，配置品类营销结构
    marketing_plan_2015(df)

if __name__ == '__main__':
    main()