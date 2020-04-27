# _*_ coding:utf-8 _*_
import numpy as np

"""
@author: Isidore
@email:616132717@qq.com
@file: numpy_tutorial2.py
@time: 2019/01/16  18:45
@version: 
"""

"""
程序目的：make some exercises of numpy module
"""

# 19 import the iris dataset keeping the text intact.  Extract the text column species from the 1D iris
iris_data = np.genfromtxt('iris_data.txt', delimiter=',', dtype=object)
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris_data[:3])

print(iris_data.shape)
spciecs = np.array([row[4] for row in iris_data])
# print(spciecs)
print(spciecs[:5])
print(np.unique(spciecs, return_counts=True))

# 20 Convert the 1D iris to 2D array iris_2d by omitting the species text field
# method1 Convert each row to a list and get the first 4 items
iris_data = np.genfromtxt('iris_data.txt', delimiter=',', dtype=float)
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
iris_2d_1 = np.array([row.tolist()[:4] for row in iris_data])
print(iris_2d_1[:4])

# method2 Import only the first 4 columns from iris_data
iris_2d_2 = np.genfromtxt('iris_data.txt', delimiter=',', dtype=float, usecols=[0, 1, 2, 3])
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris_2d_2[:4])

# 21 Create a normalized form of iris's sepallength whose values range exactly between 0 and 1 so that the minimum has
# value 0 and maximum has value 1.
sepallength = np.genfromtxt('iris_data.txt', delimiter=',', dtype=float, usecols=[0])
Smax, Smin = sepallength.max(), sepallength.min()
S1 = (sepallength - Smin) / (Smax - Smin)
# or
S2 = (sepallength - Smin) / sepallength.ptp()
print(S1)
print(S2)
print(sepallength.ptp())

# 22 Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
iris_data = np.genfromtxt('iris_data.txt', delimiter=',', dtype=float, usecols=[0, 1, 2, 3])
condition = (iris_data[:, 2] > 1.5) & (iris_data[:, 0] < 5.0)
print(iris_data[condition])
print(np.isnan(iris_data).any())



