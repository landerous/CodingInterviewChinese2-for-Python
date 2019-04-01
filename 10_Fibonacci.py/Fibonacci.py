# -*- coding: utf-8 -*-
"""
参考：https://github.com/zhedahht/CodingInterviewChinese2
将其C代码改写为Python代码
作者：胡绍阳
"""

"""
// 面试题10：斐波那契数列
// 题目一：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项:
    [0,1,1,2,3,5,8,11...],第0项是0，第1项是1，第2项是1，第3项是2。
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

"""运行"""
result = Solution()

#方法1
print(result.Fibonacci_Solution1(10))

#方法2
print(result.Fibonacci_Solution2(10))

#方法3
print(result.Fibonacci_Solution_my(10))
