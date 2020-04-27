# _*_ coding:utf-8 _*_
import numpy as np

"""
@author: Isidore
@email:616132717@qq.com
@file: numpy_tutorial1.py
@time: 2019/01/16  14:29
@version:
"""

"""
程序目的：make some exercises of numpy module
"""
# 1 Create a 1D array of numbers from 0 to 9
arr1 = np.arange(10)
print(arr1)

# 2 Create a 3×3 numpy array of all True’s
arr2 = np.full((3, 3), True, dtype=bool)
print(arr2)

# 3 Extract all odd numbers from arr
arr3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr3 = arr3[arr3 % 2 == 1]
print(arr3)

# 4 Replace all odd numbers in arr with -1
arr4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr4[arr4 % 2 == 1] = -1
print(arr4)

# 5 Replace all odd numbers in arr with -1 without changing arr
arr5 = np.arange(10)
out = np.where(arr5 % 2 == 1, -1, arr5)
print(arr5)
print(out)

# 6 Convert a 1D array to a 2D array with 2 rows
arr6 = np.arange(10)
arr6 = arr6.reshape(2, -1)
print(arr6)

# 7 Stack arrays a and b vertically
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# method 1
a_b_1 = np.concatenate([a, b], axis=0)
print(a_b_1)

# method 2
a_b_2 = np.vstack([b, a])
print(a_b_2)

# method 3
a_b_3 = np.r_[a, b]
print(a_b_3)

# 8 Stack the arrays a and b horizontally.
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# method 1
a_b_1 = np.concatenate([a, b], axis=1)
print(a_b_1)

# method 2
a_b_2 = np.hstack([b, a])
print(a_b_2)

# method 3
a_b_3 = np.c_[a, b]
print(a_b_3)

# 9 Create the following pattern without hardcoding. Use only numpy functions and the below input array a
# a = np.array([1,2,3])  #> array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1,
# 2, 3, 1, 2, 3])
a1 = np.array([1, 2, 3])
# b1 = np.r_[a1.repeat(3)]
# b1 = np.r_[np.tile(a1, 3)]
b1 = np.r_[np.repeat(a1, 3), np.tile(a1, 3)]
print(b1)

# 10 Get the common items between a and b
a2 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6, 9])
b2 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(np.intersect1d(a2, b2))

# 11 From array a remove all items present in array b
a3 = np.array([1, 2, 3, 4, 5, 6])
b3 = np.array([4, 5, 6, 7, 8, 9])
print(np.setdiff1d(a3, b3))
print(np.setdiff1d(b3, a3))

# 12 Get the positions where elements of a and b match,the same elements
a4 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b4 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print(np.where(a4 == b4, -1, a4))
print(np.where(a4 == b4))

# 13 Get all items between 5 and 10 from a
a5 = np.array([2, 6, 1, 9, 10, 3, 27])

# method 1
print(a5[np.where((a5 >= 5) & (a5 <= 10))])

# method 2
print(a5[(a5 >= 5) & (a5 <= 10)])

# method 3
print(a5[np.where(np.logical_and(a5 >= 5, a5 <= 10))])


# 14 Convert the function maxx that works on two scalars, to work on two
# arrays.
a6 = np.array([5, 7, 9, 8, 6, 4, 5])
b6 = np.array([6, 3, 4, 8, 9, 7, 1])


def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a6, b6))


# 15 Swap columns 1 and 2 in the array arr, Swap rows 1 and 2 in the array arr:
arr7 = np.arange(9).reshape(3, 3)
print(arr7)

# Swap columns 1 and 2 in the array arr7
arr8 = arr7[:,  [1, 0, 2]]
print(arr8)

# Swap rows 1 and 2 in the array arr7
arr9 = arr7[[1, 0, 2], :]
print(arr9)

# 16 Reverse the rows of a 2D array arr, Reverse the columns of a 2D array arr.
arr10 = np.arange(9).reshape(3, 3)
print(arr10)

# Reverse the rows of a 2D array arr,
arr11 = arr10[::-1, :]
print(arr11)

# Reverse the columns of a 2D array arr
arr12 = arr10[:, ::-1]
print(arr12)


# 17 Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.
# method1  randint outputs the integer numbers between 5 and 10, random outputs decimal numbers between 0 and 1
rand_arr1 = np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
print(rand_arr1)

# method 2
rand_arr2 = np.random.uniform(5, 10, size=(5, 3))
print(rand_arr2)

# Print or show only 3 decimal places of the numpy array rand_arr
rand_arr3 = np.random.uniform(5, 10, size=(5, 3))
np.set_printoptions(precision=3)
print(rand_arr3)


# 18 Limit the number of items printed in python numpy array a to a maximum of 6 elements
arr13 = np.arange(15)
np.set_printoptions(threshold=6)
print(arr13)


