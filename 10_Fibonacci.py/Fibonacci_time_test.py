# -*- coding: utf-8 -*-
"""
Author：胡绍阳
"""

"""
测试运行时间结果（最小运行时间从小到大排序）：
基于循环的方法 < 基于循环的方法（用list）< 基于黄金分割公式 < 基于递归 < 基于矩阵乘法(普通的幂次计算）

时间单位注释：1s=10^3ms(毫秒)=10^6μs(微秒)=10^9ns(纳秒)=10^12ps(皮秒)

// 面试题10：斐波那契数列
// 题目一：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项:
    [0,1,1,2,3,5,8,13...],第0项是0，第1项是1，第2项是1，第3项是2。
"""

#-----------方法 1：递归---------------
def Fibonacci_Solution1(n):

    if n <= 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return Fibonacci_Solution1(n-1) + Fibonacci_Solution1(n-2)


#-----------方法 2-1：循环---------------
def Fibonacci_Solution2_1(n):

    if n <=0:
        return 0
    
    elif n ==1:
        return 1
    
    else:
        
        num_small = 0
        num_big = 1
        for pos_now in range(n-1):   #这里发现使用range比使用np.arange的速度要快
            num_result = num_small + num_big
            num_small , num_big = num_big , num_result
            
        return num_result
    
#方法2-2 循环（用list保存）---------------
def Fibonacci_Solution2_2(n):
    
    n_list = [0,1]
    
    if n <=0:
        return 0
    
    elif n ==1:
        return 1
    
    else:
        for pos_now in range(n-1):
            n_list.append( n_list[pos_now] + n_list[pos_now + 1] )
            
        return n_list[n]
    
#-----------方法3-1：基于矩阵乘法(普通的幂次计算）---------------
def Fibonacci_Solution3_1(n):
    
    F = np.matrix([[1,1],[1,0]])
    
    return ((F ** (n-1))[0,0])

#-----------方法3-1：基于矩阵乘法(矩阵的二分求幂）---------------
def Fibonacci_Solution3_2(self,n):
    pass
    
    return 1

#-----------方法4：基于黄金分割公式---------------
def Fibonacci_Solution4(n):
    
    #num = range(0,n)
    num = n
    sqrt5 = np.sqrt(5)
    phi = (1 + sqrt5) / 2
    fibonacci = np.rint(((phi**num) - (-1/phi)**num)/sqrt5)
    return fibonacci

"""
// 题目一：测试代码
"""
import timeit

#测试：方法 1：递归
test1 = timeit.Timer('Fibonacci_Solution1(10)','from __main__ import Fibonacci_Solution1')
print(min(test1.repeat(repeat=5,number=10000)))

#测试：方法 2-1：循环
test2_1 = timeit.Timer('Fibonacci_Solution2_1(10)','from __main__ import Fibonacci_Solution2_1')
print(min(test2_1.repeat(repeat=5,number=10000)))

#测试：方法2-2 ：循环（用list保存）
test2_2 = timeit.Timer('Fibonacci_Solution2_2(10)','from __main__ import Fibonacci_Solution2_2')
print(min(test2_2.repeat(repeat=5,number=10000)))

#测试：方法3-1：基于矩阵乘法-普通的幂次计算
import numpy as np
test3_1 = timeit.Timer('Fibonacci_Solution3_1(10)','from __main__ import Fibonacci_Solution3_1')
print(min(test3_1.repeat(repeat=5,number=10000)))


#测试：方法4：基于黄金分割公式
test4 = timeit.Timer('Fibonacci_Solution4(10)','from __main__ import Fibonacci_Solution4')
print(min(test4.repeat(repeat=5,number=10000)))
