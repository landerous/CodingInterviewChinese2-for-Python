CodingInterviewChinese2-for-Python
===========================
Last update 3,April,2019</br>

|Author|landerous|
|---|---
|E-mail|landerous@foxmail.com

> 本项目参考《剑指offer》书中的源代码，将所有题目的解法改写为Python版本。

优点在于以下3点：
1. 对部分题目扩充相关解法，如利用黄金分割公式求解Fibonacci数列
2. 比较各解法的运行时间
3. 包括《剑指offer》所有题目的求解代码

****

# 已完成
#### 面试题10
- [x] 10-1 求斐波那契数列的第n项

后续仍需要完成的工作：
背景：目前Fibonacci_Solution3_1【基于矩阵乘法(普通的幂次计算）】此方法在n=93时就开始不是正确的值了，而Fibonacci_Solution4【基于黄金分割公式】此方法在n=71时就开始不是正确的值了，觉得原因在于高次幂会产生溢出，同时，这也导致【Fibonacci_runtime_test_and_anlysis.py】中的算法的运行时间分析3和4结果无效，因此，下一步需要完成：
* [ ] （1）尝试 基于矩阵乘法(矩阵的二分求幂 + 位运算）解决Fibonacci_Solution3_1的问题
* [ ] （2）尝试 在Fibonacci_Solution4算法中涉及幂次运算那里 采用二分求幂解决该问题
* [ ] （3）解决Fibonacci_Solution3_1和4计算高次斐波那契数列后，重新进行算法的运行时间分析3和4
- [x] 10-2 青蛙跳台阶问题
