# _*_ coding:utf-8 _*_
import numpy as np

"""
@author: Isidore
@email:616132717@qq.com
@file: numpy_array_sorting.py
@time: 2019/01/17  16:15
@version:
"""

"""
程序目的：对数组进行排序
"""

names = np.array(['bob', 'sue', 'jan', 'ad'])
weights = np.array([20.8, 93.2, 53.4, 61.8])

# sort()和argsort()为numpy的函数，函数不会改变原数组的值
print(np.sort(weights))     # numpy的sort函数返回的结果是从小到大排列的
print(np.argsort(weights))  # numpy的argsort函数返回从小到大的排列在数组中的索引位置
print(weights[np.argsort(weights)])  # 输出效果与sort函数等同
print(names[np.argsort(weights)])


# 数组本身具备sort()和argsort()方法，
# argsort方法与argsort函数的使用没什么区别，也不会改变数组的值
# sort方法会改变数组的值
print(weights)
weights.argsort()
print(weights)


weights.sort()
print(weights)

# 二维数组的排序，对于多维数组，sort方法默认沿着最后一维开始排，对于二维数组，默认相当于对每一行进行排序
arr1 = np.array([[0.2, 0.1, 0.5],
                 [0.4, 0.8, 0.3],
                 [0.9, 0.6, 0.7]])

print(np.sort(arr1))
print(np.sort(arr1, axis=0))

# searchsorted函数,searchsorted(sorted_array, values),searchsorted 接受两个参数，其中，第一个必需是已排序的数组
# searchsorted返回的值相当于保持第一个数组的排序性质不变，将第二个数组中的值插入第一个数组中的位置,返回的是插入位置的索引
sorted_array = np.linspace(0, 1, 5)
print(sorted_array)

values = np.array([0.1, 0.8, 0.3, 0.12, 0.5, 0.25])
print(np.searchsorted(sorted_array, values))

arr2 = np.arange(9).reshape(3, 3)
arr3 = np.dstack([arr1, arr2])

print(arr3)
print(arr3.shape)
