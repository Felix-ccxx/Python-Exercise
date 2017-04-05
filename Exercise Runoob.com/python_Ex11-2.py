# -*- coding: cp936 -*-
'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

斐波那契数列
'''

def fab(n):
    if n==1:
        return 1
    if n==0:
        return 0
    else:
        result=int(fab(n-1))+int(fab(n-2))
        #print result,
        return result

for i in range(20):
    print fab(i),


