# _*_ coding:utf-8 _*_
import numpy as np

"""
@author: Isidore
@email:616132717@qq.com
@file: numpy_array_calculation.py
@time: 2019/01/17  14:30
@version:
"""

"""
程序目的：numpy数组的计算
"""

arr1 = np.arange(9).reshape(3, 3)
print(arr1)

print(arr1.sum())   # 求数组中全部元素的和

# 指定求和的维度：
print(arr1.sum(axis=0))  # 沿着第一维求和，axis=0时，求列的和
print(arr1.sum(axis=1))  # 沿着第二维度求和，axis=1时，求行的和
print(arr1.sum(axis=-1))    # 沿着最后一维求和

# 乘法
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(arr2.prod())
print(np.prod(arr2, axis=0))    # 沿着第一维求积，axis=0时，求列的积
print(np.prod(arr2, axis=1))    # 沿着第二维求积，axis=1时，求行的积

# 求最大最小值
arr_rand = np.random.rand(3, 4)
print(arr_rand)

print(arr_rand.min())   # 全局最小
print(arr_rand.min(axis=0))
print(arr_rand.max())
print(arr_rand.max(axis=-1))

# argmax(),argmin()输出最大值和最小值的索引
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.argmax())
print(a.argmin())
print(a.argmin(axis=1))

# 常用的函数 均值，平均数，标准差，
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(a.mean())     # 均值
print(np.mean(a, axis=0))
print(np.average(arr4))
print(np.average(arr4, axis=0, weights=[1, 2]))     # numpy的average函数求加权平均值

print(arr4.std())    # 用std方法计算标准差
print(arr4.std(axis=0))
print(arr4.var())   # 用var方法计算标准差
print(arr4.clip(3, 5))  # 采用clip将数值限制在某个范围
print(arr4.ptp())   # 采用ptp计算最大值和最小值之差

# 采用round方法近似，默认到整数
arr5 = np.array([1.35, 2.45, 1.58])
print(arr5.round())
print(arr5.round(decimals=1))  # 近似到x位小数




