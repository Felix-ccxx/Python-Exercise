# -*- coding: gbk -*-
import os
import string
import re

path=raw_input("�������ļ�����·���� ")
fname=raw_input("������Ŀ���ļ����� ")

'''path='d:\\pythontest'
fname='SMS279_GET'
'''
'''�г�����·����������.vmg��β���ļ�'''
f_dir=[flist for flist in os.listdir(path) if flist.endswith('.vmg')]
f_d=open(path+'\\'+fname+'.csv','w')
for filelist in f_dir:
    f_s=open(path+'\\'+filelist,'r')
    '''��ʼ�����ںϲ��������ݵĸ��ֶ���ʱ����'''
    vmsg_name=''
    vmsg_cell=''
    vmsg_box=''
    vmsg_date=''
    vmsg_text=''
    regmsg=''
    regcell=r'TEL;TYPE=CELL:(.+\d)'
    regbox=r'X-IRMC-BOX:(.*)\n'
    regdate=r'Date:(.*)\nTEXT;ENCODING=8BIT:'
    regtext=r'TEXT;ENCODING=8BIT:(.*)END:VBODY'

    print f_s.name
    '''��ȡ�����ļ����е�ͨѶ¼���֣�����_���롰.VMG��֮�䲿�ֵ�����'''
    vmsg_name=f_s.name.strip(path+'1234567890_.vmg\\')
    '''��ȡ�����ļ���ȫ�����ݣ�������ȡ�绰���շ�״̬�����ڡ���������������'''
    vmsg=f_s.readlines()
    print vmsg
    for v in vmsg:
        regmsg=regmsg+v

    '''��re.findall���ص����б����ͣ����Բ���������������ȡ����1��ƥ���תΪ�ַ����ͣ���findallΪ��ʱ����BUG'''
    vmsg_cell=re.findall(regcell,regmsg)[0]
    vmsg_box=re.findall(regbox,regmsg)[0]
    vmsg_date=re.findall(regdate,regmsg)[0]
    vmsg_text=re.findall(regtext,regmsg,re.S)[0]
    vmsg_text=vmsg_text.decode('utf-8').encode('gbk')

    '''VMG�ļ��Ķ��Ų���UTF-8���룬����Ϊȷ��ת��CSV�ļ����ڼ��±����ı��Ŀɶ��ԣ���Ҫ�����ַ�����ת����
    ��ʹ��DECODE�����ŵ�UTF-8��ʽ�����UNICODE���루UTF-8��GBK֮����ֱ��ת�뺯������������UNICODE��Ϊ��ת����
    Ȼ����ʹ��ENCODE��UNICODE�����GBK��GB2312�ȱ����ʽ�����������Ļ����¿����ü��±����ˡ�'''

    ''' ���·�������Ҫ���һ����������ռ�ö��е����⣬�������REGEX������ݣ���δ����δ���
    for v in vmsg:
        if v.startswith('TEL;TYPE=CELL:'):
            vmsg_cell=v[len('TEL;TYPE=CELL:'):-1]
        elif v.startswith('X-IRMC-BOX:'):
            vmsg_box=v[len('X-IRMC-BOX:'):-1]
        elif v.startswith('Date:'):
            vmsg_date=v[len('Date:'):-1]
        elif v.startswith('TEXT;ENCODING=8BIT:'):
            vmsg_text=v[len('TEXT;ENCODING=8BIT:'):-1].decode('utf-8').encode('gbk')
    '''

    '''����ϲ���������������ݡ�'''
    if vmsg_name!='':
        f_d.write(vmsg_name+'|'+ \
                  vmsg_cell+'|'+ \
                  vmsg_box+'|'+ \
                  vmsg_date+'|'+ \
                  vmsg_text+'\n')
    else:
        f_d.write(vmsg_cell+'|'+ \
                  vmsg_cell+'|'+ \
                  vmsg_box+'|'+ \
                  vmsg_date+'|'+ \
                  vmsg_text+'\n')
    f_s.close()
f_d.close()

