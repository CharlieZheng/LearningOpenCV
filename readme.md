## 1.3.3 性能测量和提高技术
### 统计
cv2.getTickCount：该方法返回当前时钟周期
cv2.getTickFrequency：该方法返回每秒有多少个时钟周期
用法：时间间隔内的时钟周期数量/每秒的时钟周期数量 = 该段时间间隔是多少秒
```
e1 = cv2.getTickCount()
# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
```


类似的：
 - time模块：提供了测量程序运行时间的功能
 - profile：用于生成具体的代码报告，如每个方法执行了多久以及被执行了多少次
 
 
 
 ### 优化
 
 
 使用的是SSE2, AVX的优化技术 // 不知道SSE2, AVX是啥，也许是内置的各大系统的C模块
 cv2.useOptimized()                 // 返回是否开启代码性能优化
 cv2.setUseOptimized()              // 设置是否开启优化

中值过滤是SIMD优化技术

优化默认开启
 
 
 ### 使用IPython测量
 
 通过多次执行一段代码 使测量更准确
  1. 使用pip安装IPython 
 ```
 pip install ipython
 ```
  2. 
 ```
 sudo apt-get install ipython
 ```
 
  - 进入IPython的pylab模式
 
 ```
 ipython --pylab
 ```
  - 退出
  ```
  ctrl + d
  ```
  In [1]: x=5

#### 使用方法
```
In [2]: %timeit y = x**2
The slowest run took 57.57 times longer than the fastest. This could mean that an intermediate result is being cached.
10000000 loops, best of 3: 37.3 ns per loop
```
// 可以用Google翻译一下，就知道上面这段话在说什么了


```
In [10]: x = 5
In [11]: %timeit y=x**2
10000000 loops, best of 3: 73 ns per loop
In [12]: %timeit y=x*x
10000000 loops, best of 3: 58.3 ns per loop
In [15]: z = np.uint8([5])
In [17]: %timeit y=z*z
1000000 loops, best of 3: 1.25 us per loop
In [19]: %timeit y=np.square(z)
1000000 loops, best of 3: 1.16 us per loop
```

上面这些数据，看起来是Numpy的执行效率最高。不知道为什么pdf中说numpy慢了20倍比x*x

```
In [1]: x=5

In [2]: %timeit y = x**2
The slowest run took 57.57 times longer than the fastest. This could mean that an intermediate result is being cached.
10000000 loops, best of 3: 37.3 ns per loop

In [3]: %timeit y = x*x
10000000 loops, best of 3: 27 ns per loop

In [4]: z = np .uint8([5])

In [5]: %timeit y = z*z
The slowest run took 3294.93 times longer than the fastest. This could mean that an intermediate result is being cached.
1000000 loops, best of 3: 273 ns per loop

In [6]: %timeit y = np.square(z)
The slowest run took 30.98 times longer than the fastest. This could mean that an intermediate result is being cached.
1000000 loops, best of 3: 285 ns per loop
```

我在我自己的电脑上执行代码的数据如上，那倒是numpy慢了确实


#### 再对比两个函数的效率
cv2.countNonZero()
np.count_nonzero()

#### IPython的其它魔法
 - profiling
 - line profiling
 - memory measurement
#### 代码优化建议 

 - 避免多重循环 
 - 使用cv2 和numpy帮你实现好的矩阵操作函数
 - 利用缓存一致性 // 不知道缓存一致性是啥，猜测可能是一份缓存的意思
 - 不要做矩阵复制操作，利用视图 // 不知道视图是啥，数据库也有视图这种东西，可能是差不多的东西
