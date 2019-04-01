# -*- coding: utf-8 -*-
"""
参考：https://github.com/zhedahht/CodingInterviewChinese2
将其C代码改写为Python代码,并测试其运行的时间（以最小运行时间作为比较）
时间单位注释：1s=10^3ms(毫秒)=10^6μs(微秒)=10^9ns(纳秒)=10^12ps(皮秒)
作者：胡绍阳
"""

"""
// 面试题10：斐波那契数列
// 题目一：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项:
    [0,1,1,2,3,5,8,11...],第0项是0，第1项是1，第2项是1，第3项是2。
"""

s = """
class Solution:
    
    #-----------方法 1：递归---------------
    def Fibonacci_Solution1(self,n):

        if n <= 0:
            return 0
        
        elif n == 1:
            return 1
        
        else:
            return self.Fibonacci_Solution1(n-1) +self.Fibonacci_Solution1(n-2)
    
    
    #-----------方法 2：循环---------------
    def Fibonacci_Solution2(self,n):

        if n <=0:
            return 0
        
        elif n ==1:
            return 1
        
        else:
            
            #num_i、j、k为数列中连续的3个数，且数值上i<j<k
            num_i = 0
            num_j = 1
            for pos_i in range(n-1):   #这里发现使用range比使用np.arange的速度要快
                num_k = num_i + num_j
                num_i , num_j = num_j , num_k
                
            return num_k
        
    #方法 自己：循环（用list保存）---------------
    def Fibonacci_Solution_my(self,n):
        
        n_list = [0,1]
        
        if n <=0:
            return 0
        
        elif n ==1:
            return 1
        
        else:
            for pos_i in range(n-1):
                n_list.append( n_list[pos_i] + n_list[pos_i + 1] )
                
            return n_list[n]
"""

"""
// 题目一：测试代码
"""
import timeit

#方法1
print(min(timeit.repeat('Solution().Fibonacci_Solution1(10)',s,number=10000)))

#方法2
print(min(timeit.repeat('Solution().Fibonacci_Solution2(10)',s,number=10000)))

#方法3
print(min(timeit.repeat('Solution().Fibonacci_Solution_my(10)',s,number=10000)))

