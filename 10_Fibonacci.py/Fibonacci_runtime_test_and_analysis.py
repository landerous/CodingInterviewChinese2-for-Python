# -*- coding: utf-8 -*-
"""
Author：胡绍阳
"""

"""
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
    
    F = np.matrix([[1,1],[1,0]],dtype=np.int64)
    
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
// 题目一：测试各算法的运行时间
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

"""
// 算法的运行时间分析
""" 
def runtime_analysis(method_string_run,fibonacci_n_run,repeat_run=5,number_run=100):
    """
    功能：对算法进行运行时间分析
    输入：method_string_run - 算法字符串列表
         fibonacci_n_run - 测试的斐波那契数列的n组成的列表
         repeat_f（timeit.repeat里的参数repeat）
         number_f（timeit.repeat里的参数number）
    输出：time_run - 运行时间统计
    """
    method_len = len(method_string_run) 
    number_len = len(fibonacci_n_run)
    time_run = np.zeros((method_len,number_len))
    
    """计算不同输入对算法运行时间的影响"""
    for method_i in range(method_len): #每一种方法
        
        method_string_i = method_string_run[method_i]
        
        for num_i in range(number_len): #每一个数字n
            
            number_test_i = fibonacci_n_run[num_i]
            
            test = timeit.Timer('Fibonacci_Solution%s(%d)' %(method_string_i,number_test_i),'from __main__ import Fibonacci_Solution%s' %method_string_i)
            time_run[method_i][num_i] = min(test.repeat(repeat=repeat_run,number=number_run))
            
    return time_run

import matplotlib.pyplot as plt

"""----算法的运行时间分析1：方法 1：递归的运行时间分析"""
method_string_1 = ['1'] ##计算斐波那契数列的方法的函数名后缀
fibonacci_n_test_1 = range(1,38,5)  #计算斐波那契数列的第n项的n——38
time_running_1 = runtime_analysis(method_string_1,fibonacci_n_test_1,number_run=1)

#创建图片，并添加文本
fig = plt.figure()

#画折线图
line1_1,=plt.plot(fibonacci_n_test_1,time_running_1[0][:],'bs-')

#添加图例
line_list = [line1_1]
line_list_legend = ['1-recursion']
plt.legend(line_list,line_list_legend,loc='upper left')

#设置横纵轴的名称
plt.xlabel("Fibonacci n-th")
plt.ylabel("Time/s")
plt.title("Running Time Analysis of Recursion\nrepeat = 5  number = 1")

plt.show()

"""----算法的运行时间分析2：各算法的运行时间分析："""
method_string_2 = ['1','2_1','2_2','3_1','4'] ##计算斐波那契数列的方法的函数名后缀
fibonacci_n_test_2 = range(1,17,5)  #计算斐波那契数列的第n项的n
time_running_2 = runtime_analysis(method_string_2,fibonacci_n_test_2,number_run=100)

#创建图片，并添加文本
fig = plt.figure()

#画折线图
line1_2,=plt.plot(fibonacci_n_test_2,time_running_2[0][:],'bs-')
line2_1_2,=plt.plot(fibonacci_n_test_2,time_running_2[1][:],'rs-')
line2_2_2,=plt.plot(fibonacci_n_test_2,time_running_2[2][:],'ys-')
line3_1_2,=plt.plot(fibonacci_n_test_2,time_running_2[3][:],'ks-')
line4_2,=plt.plot(fibonacci_n_test_2,time_running_2[4][:],'ms-')

line_list = [line1_2,line2_1_2,line2_2_2,line3_1_2,line4_2]
line_list_legend = ['1-recursion','2-1_loop','2-2_loop with list','3-1_Matrix multiplication','4-Golden Section Formula']
#['1-递归','2-1_循环','2-2_list循环','3-1_矩阵乘法','4-黄金分割公式']
plt.legend(line_list,line_list_legend,loc='upper left')

#设置横纵轴的名称
plt.xlabel("Fibonacci n-th")
plt.ylabel("Time/s")
plt.title("Running Time Analysis of Different Algorithms\nrepeat = 5  number = 100")
plt.show()


"""----算法的运行时间分析3：除递归解法外的各算法的运行时间分析："""
method_string_3 = ['2_1','2_2','3_1','4'] ##计算斐波那契数列的方法的函数名后缀
fibonacci_n_test_3 = range(1,1000,5)  #计算斐波那契数列的第n项的n
time_running_3 = runtime_analysis(method_string_3,fibonacci_n_test_3,number_run=100)

#创建图片，并添加文本
fig = plt.figure()

#画折线图
line2_1_3,=plt.plot(fibonacci_n_test_3,time_running_3[0][:],'rs-')
line2_2_3,=plt.plot(fibonacci_n_test_3,time_running_3[1][:],'ys-')
line3_1_3,=plt.plot(fibonacci_n_test_3,time_running_3[2][:],'ks-')
line4_3,=plt.plot(fibonacci_n_test_3,time_running_3[3][:],'ms-')

line_list = [line2_1_3,line2_2_3,line3_1_3,line4_3]
line_list_legend = ['2-1_loop','2-2_loop with list','3-1_Matrix multiplication','4-Golden Section Formula']
#['2-1_循环','2-2_list循环','3-1_矩阵乘法','4-黄金分割公式']
plt.legend(line_list,line_list_legend,loc='upper left')

#设置横纵轴的名称
plt.xlabel("Fibonacci n-th")
plt.ylabel("Time/s")
plt.title("Running Time Analysis of Different Algorithms (Except Recursion) \nrepeat = 5  number = 100")
plt.show()

"""----算法的运行时间分析4：对矩阵乘法-普通的幂次计算 and 黄金分割公式 2种方法计算斐波那契数列第n项的运行时间分析 """
method_string_4 = ['3_1','4'] ##计算斐波那契数列的方法的函数名后缀
fibonacci_n_test_4 = range(1,100,5)  #计算斐波那契数列的第n项的n——38
time_running_4 = runtime_analysis(method_string_4,fibonacci_n_test_4,number_run=100)

#创建图片，并添加文本
fig = plt.figure()

#画折线图
line3_1_4,=plt.plot(fibonacci_n_test_4,time_running_4[0][:],'ks-')
line4_4,=plt.plot(fibonacci_n_test_4,time_running_4[1][:],'ms-')
#添加图例
line_list = [line3_1_4,line4_4]
line_list_legend = ['3-1_Matrix multiplication','4-Golden Section Formula']
plt.legend(line_list,line_list_legend,loc='upper left')

#设置横纵轴的名称
plt.xlabel("Fibonacci n-th")
plt.ylabel("Time/s")
plt.title("Running Time Analysis of Recursion\nrepeat = 5  number = 100")

plt.show()
