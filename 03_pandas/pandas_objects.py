# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np

"""
@author: Isidore
@email:616132717@qq.com
@file: pandas_objects.py
@time: 2019/01/21  18:01
@version:
"""

"""
程序目的：
pandas 中有三种基本结构：
Series：1D labeled homogeneously-typed array
DataFrame：General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed columns
Panel：General 3D labeled, also size-mutable array

通过DataFrame生成pandas对象

虽然 DataFrame 支持 Python/Numpy 的索引语法，但是推荐使用 .at, .iat, .loc, .iloc 和 .ix 方法进行索引
"""

dates = pd.date_range('20190115', periods=6)
df1 = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))
print(df1)
print(df1.head())   # head默认是5行
print(df1.tail())   # head默认是5行
print(df1.values)   # 数据值使用values查看
print(df1.describe())   # 查看简单的统计数据
print(df1.T)    # 转置

# sort_values(by, axis=0, ascending=True) 方法按照by的值的大小进行排序
# sort_index(axis=0, ascending=True)方法按照下标大小进行排序，axis=0表示按第0维进行排序
print(df1.sort_index(axis=0, ascending=True))
print(df1.A)

# DataFrame.loc[index:, column]
print(df1.at[dates[0], 'B'])



# 向DataFrame中传入字典数据
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)


# 采用merge方法实现数据库中的join操作
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
df3 = pd.merge(left, right, on='key')
print(df3)

