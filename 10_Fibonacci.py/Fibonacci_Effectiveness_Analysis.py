# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:29:18 2019

@author: 胡绍阳
"""

"""
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
            
        return int(n_list[n])
    
#-----------方法3-1：基于矩阵乘法(普通的幂次计算）---------------
def Fibonacci_Solution3_1(n):
    
    F = np.matrix([[1,1],[1,0]],dtype=np.int64)
    
    return ((F ** (n-1))[0,0])

def matrix_power(F,n):
    """输入：矩阵F，幂次n"""
    
    if n == 1:
        return F
    elif (n % 2) == 1:
        return matrix_power(F,(n-1)/2)*matrix_power(F,(n-1)/2)
    

#-----------方法3-2：基于矩阵乘法(矩阵的二分求幂）---------------
def Fibonacci_Solution3_2(n):
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
    
import numpy as np
"""
// 题目一：基于矩阵乘法和基于黄金分割公式计算斐波那契数列的有效性分析
"""
method_string = ['3_1','4'] ##计算斐波那契数列的方法的函数名后
fibonacci_n = range(1,1000)  #计算斐波那契数列的第n项的n
method_len = len(method_string) 
number_len = len(fibonacci_n)
value_fn = np.zeros((number_len,3))

"""计算出正确的数值，使用方法2_1"""
for num_i in range(number_len): #每一个数字n
    value_fn[num_i][0] = Fibonacci_Solution2_1(num_i)

"""计算方法3_1与方法4的结果，并验证正确性"""
for method_i in range(method_len): #每一种方法
    
    method_string_i = method_string[method_i]
    
    for num_i in range(number_len): #每一个数字n
        
        value_fn_34 = eval('Fibonacci_Solution%s(%d)' %(method_string_i,num_i))
        
        if value_fn_34 == value_fn[num_i][0]:
            value_fn[num_i][method_i+1] = 1   #结果正确为1
        else:
            value_fn[num_i][method_i+1] = 0   #结果不正确为0