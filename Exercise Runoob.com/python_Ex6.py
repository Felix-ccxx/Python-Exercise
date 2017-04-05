# -*- coding: cp936 -*-
'''
��Ŀ��쳲��������С�

���������쳲��������У�Fibonacci sequence�����ֳƻƽ�ָ����У�ָ��������һ�����У�0��1��1��2��3��5��8��13��21��34��������
����ѧ�ϣ��Ѳ������������Եݹ�ķ��������壺
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''

def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a

print fib(10)


def fib2(n):
    if n==1 or n==2:
        return 1
    return fib2(n-1)+fib(n-2)

print fib2(10)

def fib3(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs=[1,1]
    for i in range (2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

print fib3(10)
