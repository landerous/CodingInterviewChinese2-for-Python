# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:56:49 2019

@author: user
"""

"""
// 面试题10：斐波那契数列
// 题目二：青蛙跳台阶问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
本质是斐波那契数列问题，解法与斐波那契数列问题一样，与斐波那契数列不同的是，
该问题需要注意的是：f(1)=1，f(2)=2，循环的次数
"""

class Solution:
    
    #-----------方法 1：递归---------------
    def Frog_jump_steps_Solution1(self,n):

        if n <= 1:
            return 1
        
        elif n == 2:
            return 2
        
        else:
            return self.Frog_jump_steps_Solution1(n-1) +self.Frog_jump_steps_Solution1(n-2)
    
    
    #-----------方法 2：循环---------------
    def Frog_jump_steps_Solution2(self,n):

        if n <=1:
            return 1
        
        elif n ==2:
            return 2
        
        else:
            
            #num_i、j、k为数列中连续的3个数，且数值上i<j<k
            num_i = 1
            num_j = 2
            for pos_i in range(n-2):   #这里发现使用range比使用np.arange的速度要快
                num_k = num_i + num_j
                num_i , num_j = num_j , num_k
                
            return num_k
        
    #方法 自己：循环（用list保存）---------------
    def Frog_jump_steps_Solution_my(self,n):
        
        n_list = [1,2]
        
        if n <=1:
            return 1
        
        elif n ==2:
            return 2
        
        else:
            for pos_i in range(n-2):
                n_list.append( n_list[pos_i] + n_list[pos_i + 1] )
                
            return n_list[n-1]

"""运行"""
result = Solution()

#方法1
print(result.Frog_jump_steps_Solution1(10))

#方法2
print(result.Frog_jump_steps_Solution2(10))

#方法3
print(result.Frog_jump_steps_Solution_my(10))
