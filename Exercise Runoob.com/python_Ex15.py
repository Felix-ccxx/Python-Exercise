# -*- coding: cp936 -*-
'''
��Ŀ�����������������Ƕ������ɴ��⣺ѧϰ�ɼ�>=90�ֵ�ͬѧ��A��ʾ��60-89��֮�����B��ʾ��60�����µ���C��ʾ��

������������������(a>b)?a:b��������������Ļ������ӡ�


'''

score = int(raw_input('input score:\n'))

grade=(score>90)?'A':(score>=60)?'B':'C'

print '%d belongs to %s' % (score,grade)



