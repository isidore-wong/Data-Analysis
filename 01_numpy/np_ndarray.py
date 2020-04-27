# _*_ coding:utf-8 _*_
import numpy as np

"""
@author: Isidore
@email:616132717@qq.com
@file: np_ndarray.py
@time: 2019/01/15  23:11
@version: 
"""

"""
程序目的：numpy库的学习与使用
"""

def npSum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])
    c = a**2 + b**2
    return c

print(npSum())
np_num = np.array([[0, 1, 2, 3, 4],
                  [9, 8, 7, 6, 5]])


'''
numpy库ndarray对象的属性
.ndim:秩，即轴的数量或维度的数量
.shape:ndarray对象的尺度，对于矩阵，n行m列
.size:ndarray对象元素的个数，相当于.shape中n*m的值
.dtype:ndarray对象的元素类型
.itemsize:ndarray对象中每个元素的大小，以字节为单位
'''

ndim = npSum().ndim
shape = npSum().shape
size = npSum().size
dtype = npSum().dtype
itemsize = npSum().itemsize

print(np_num.ndim)
print(np_num.shape)
print(np_num.size)
print(np_num.dtype)
print(np_num.itemsizeaq)
