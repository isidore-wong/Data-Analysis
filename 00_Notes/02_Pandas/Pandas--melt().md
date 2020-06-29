### pandas的melt函数
---

在pandas函数中，df.melt() 是 df.pivot() 逆转操作函数。

在做数据分析时，使用df.pivot()是将长数据集转换成宽数据集，进行透视分析，而使用df.melt() 则是将宽数据集变成长数据集，进行逆透视分析。

**melt()函数的参数**

pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)

其中：
- frame:要处理的数据集
- id_vars:不需要被转换的列名
- value_vars:需要转换的列名，如果剩下的列全部都要转换，就不用写了
- var_name和value_name是自定义设置对应的列名
- col_level :如果列是MultiIndex，则使用此级别。


```
>>> import pandas as pd
>>> df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
...                    'B': {0: 1, 1: 3, 2: 5},
...                    'C': {0: 2, 1: 4, 2: 6}})
>>> df
   A  B  C
0  a  1  2
1  b  3  4
2  c  5  6
 
#保留 B 列
>>> df.melt(id_vars=['A'], value_vars=['B'])
   A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
 
#保留 B C 列
>>> df.melt(id_vars=['A'], value_vars=['B', 'C'])
   A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
3  a        C      2
4  b        C      4
5  c        C      6
 
#自定义列名
>>> df.melt(id_vars=['A'], value_vars=['B'],var_name='myVarname', value_name='myValname')
   A myVarname  myValname
0  a         B          1
1  b         B          3
2  c         B          5
 
#如果 columns 是MultiIndex
>>> df.columns = [list('ABC'), list('DEF')]
>>> df
   A  B  C
   D  E  F
0  a  1  2
1  b  3  4
2  c  5  6
 
>>> df.melt(col_level=0, id_vars=['A'], value_vars=['B'])
   A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
 
>>> df.melt(id_vars=[('A', 'D')], value_vars=[('B', 'E')])
  (A, D) variable_0 variable_1  value
0      a          B          E      1
1      b          B          E      3
2      c          B          E      5
```


**参考资料：**
1. [pandas.melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html)
2. [Pandas 的melt的使用](https://blog.csdn.net/maymay_/article/details/80039677)
3. [Pandas_规整数据_转换数据_melt()](https://blog.csdn.net/mingkoukou/article/details/82867218)
4. [pandas melt 与pivot 函数](https://www.cnblogs.com/sakura3/p/11979041.html)