# -*- coding: cp936 -*-
'''
��Ŀ���ŵ����⣺��һ�����ӣ��ӳ������3������ÿ���¶���һ�����ӣ�С���ӳ����������º�ÿ��������һ�����ӣ��������Ӷ���������ÿ���µ���������Ϊ���٣�

������������ӵĹ���Ϊ����1,1,2,3,5,8,13,21....

쳲���������
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


