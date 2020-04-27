# _*_ coding:utf-8 _*_
import numpy as np
import csv

"""
@author: Isidore
@email:616132717@qq.com
@file: numpy_array_funcs.py
@time: 2019/01/20  21:34
@version:
"""

"""
程序目的：numpy数组的函数
"""
# choose函数实现对数组的条件筛选

# choose函数将0,1,2 对应的值映射为10,11,12，这里的 0,1,2 表示对应的下标
control = np.array([[1, 0, 1],
                    [2, 1, 0],
                    [1, 2, 2]])
arr1 = np.choose(control, [10, 11, 12])
print(arr1)

# choose函数不仅能接受下标参数，还可以接受下标所在的位置
i0 = np.array([[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]])
i2 = np.array([[20, 21, 22],
               [23, 24, 25],
               [26, 27, 28]])
control = np.array([[1, 0, 1],
                    [2, 1, 0],
                    [1, 2, 2]])

arr2 = np.choose(control, [i0, 10, i2])
print(arr2)

# 将数组中所有小于10的值变成了10
arr3 = np.array([[0, 1, 2],
                 [10, 11, 12],
                 [20, 21, 22]])
print(arr3 <= 10)
print(np.choose(arr3 < 10, (arr3, 10)))

# 将数组中所有小于10的值变成了10，大于15的值变成了15
arr4 = np.array([[0, 1, 2],
                 [10, 11, 12],
                 [20, 21, 22]])

lt = arr4 < 10
gt = arr4 > 15
choice = lt + 2 * gt
print(choice)
print(np.choose(choice, (arr4, 10, 15)))


# 使用loadtxt函数和savetxt函数读取和保存数组
arr5 = np.loadtxt('myfile.txt')
print(arr5)

arr6 = np.random.rand(5, 5)
np.savetxt('test.txt', arr6, fmt='%0.4f')

