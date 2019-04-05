# -*- coding: utf-8 -*-
"""
Author：胡绍阳
"""

"""
// 面试题10：斐波那契数列
// 题目一：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项:
    [0,1,1,2,3,5,8,13...],第0项是0，第1项是1，第2项是1，第3项是2。
"""

class Solution:
    
    #-----------方法 1：递归---------------
    def Fibonacci_Solution1(self,n):

        if n <= 0:
            return 0
        
        elif n == 1:
            return 1
        
        else:
            return self.Fibonacci_Solution1(n-1) +self.Fibonacci_Solution1(n-2)
    
    
    #-----------方法 2-1：循环---------------
    def Fibonacci_Solution2_1(self,n):

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
    def Fibonacci_Solution2_2(self,n):
        
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
    #经过有效性分析，此方法在n=93时就开始不是真实值了，当n足够大，
    #矩阵的幂的结果的元素中产生了负数，我觉得应该和溢出或者内存有关
    #可尝试 基于矩阵乘法(矩阵的二分求幂 + 位运算），看是否能解决这个问题
    def Fibonacci_Solution3_1(self,n):
        
        F = np.matrix([[1,1],[1,0]],dtype=np.int64)
        
        return ((F ** (n-1))[0,0])
    
    #-----------方法3-2：基于矩阵乘法(矩阵的二分求幂 + 位运算）---------------
    def Fibonacci_Solution3_2(self,n):
        pass
        
        return 1

    #-----------方法4：基于黄金分割公式---------------
    def Fibonacci_Solution4(self,n):
    #经过有效性分析，此方法在n=71时就开始不是真实值了，
    #我觉得应该与内存有关
    #可尝试 在平方那里 采用二分求幂解决该问题
        #num = range(0,n)
        num = n
        sqrt5 = np.sqrt(5)
        phi = (1 + sqrt5) / 2
        fibonacci = np.rint(((phi**num) - (-1/phi)**num)/sqrt5)
        return fibonacci

"""运行"""
result = Solution()

#方法1:递归
print(result.Fibonacci_Solution1(7))

#方法 2-1：循环
print(result.Fibonacci_Solution2_1(100))

#方法2-2 循环（用list保存）
print(result.Fibonacci_Solution2_2(120))

#方法3-1：基于矩阵乘法(普通的幂次计算） #从第47项开始就不对了？
import numpy as np
print(int(result.Fibonacci_Solution3_1(100)))

#方法4：基于黄金分割公式
print(int(result.Fibonacci_Solution4(120)))
