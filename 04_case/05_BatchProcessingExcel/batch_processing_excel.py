# _*_ coding:utf-8 _*_
import pandas as pd
import time
import os

"""
@author: Hayes Wong
@email: 616132717@qq.com
@file: batch_processing_excel
@time: 2020/05/22 23:46
"""

"""
Description: Python batch processing Excel table
"""

def batch_processing(list):

    start_time = time.time()
    result = pd.DataFrame()

    # loop through table to process data
    for i in range(2, len(list)):
        name = list[i]
        df = pd.read_excel(name)
        df['销售额'] = df['转化率'] * df['访客数'] * df['客单价']
        df_sum = df.groupby('品牌')['销售额'].sum().reset_index()
        df_sum['类目'] = name.replace('.xlsx', '')
        result = pd.concat([result, df_sum])

    result_final = result.groupby('品牌')['销售额'].sum().reset_index().sort_values(by='销售额', ascending=False)
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    os.chdir('H:/mycode/Python/Data-Analysis/04_case/05_BatchProcessingExcel')
    writer = pd.ExcelWriter('Integration_data.xlsx')
    result.to_excel(excel_writer=writer, sheet_name='classification_data', index=0)
    result_final.to_excel(excel_writer=writer, sheet_name='brand_data', index=0)
    writer.save()
    writer.close()

    end_time = time.time()
    print('用Python操作所花费时间：{} s'.format(end_time - start_time))

if __name__ == '__main__':
    os.chdir('H:/mycode/Python/Data-Analysis/00_dataset/raw_excel_data_128')
    list_dir = os.listdir()
    batch_processing(list_dir)
