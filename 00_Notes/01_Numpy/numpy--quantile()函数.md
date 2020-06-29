### 分位数

#### quantile()函数
quantitle()是numpy中的分位函数，其参数为

numpy.quantile(a, q, axis=None, out=None, overwrite_input=False, interpolation='linear', keepdims=False)，该函数将沿着指定的轴计算第q个分位数

**Parameters**
- a：输入的数组或可以被转为数组的对象
- q：要计算的分位数，q位于[0，1]之间
- axis：计算分位数的轴，默认axis=0，沿列方向进行计算；axis=1沿行方向计算
- out：存放计算结果的替代输出数组
- overwrite_input：如果为True，则允许通过中间计算修改输入的数组a，以节省内存
- interpolation：指定当所需的分位数位于[i, j]间时使用的插值方法
- keepdims：如果设置为True，则缩小的轴将作为尺寸为1的尺寸留在结果中

```
>>> a = np.array([[10, 7, 4], [3, 2, 1]])
>>> np.quantile(a, 0.5)
3.5

>>> np.quantile(a, 0.5, axis=0)
array([6.5, 4.5, 2.5])

>>> np.quantile(a, 0.5, axis=1)
array([7.,  2.])
```



**参考资料**
1. [numpy官方文档-quantile](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html)
2. [分位函数（四分位数）概念与pandas中的quantile函数](https://www.cnblogs.com/zhaohuanhuan/p/9055944.html)