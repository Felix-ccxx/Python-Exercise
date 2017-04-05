# -*- coding: gbk -*-
import os
import string
import re

path=raw_input("请输入文件所在路径： ")
fname=raw_input("请输入目标文件名： ")

'''path='d:\\pythontest'
fname='SMS279_GET'
'''
'''列出给定路径下所有以.vmg结尾的文件'''
f_dir=[flist for flist in os.listdir(path) if flist.endswith('.vmg')]
f_d=open(path+'\\'+fname+'.csv','w')
for filelist in f_dir:
    f_s=open(path+'\\'+filelist,'r')
    '''初始化用于合并短信内容的各字段临时变量'''
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
    '''读取短信文件名中的通讯录名字，即“_”与“.VMG”之间部分的内容'''
    vmsg_name=f_s.name.strip(path+'1234567890_.vmg\\')
    '''读取短信文件的全部内容，逐行提取电话、收发状态、日期、短信正本等内容'''
    vmsg=f_s.readlines()
    print vmsg
    for v in vmsg:
        regmsg=regmsg+v

    '''因re.findall返回的是列表类型，所以采用索引方法，提取出第1个匹配的转为字符类型，当findall为空时会有BUG'''
    vmsg_cell=re.findall(regcell,regmsg)[0]
    vmsg_box=re.findall(regbox,regmsg)[0]
    vmsg_date=re.findall(regdate,regmsg)[0]
    vmsg_text=re.findall(regtext,regmsg,re.S)[0]
    vmsg_text=vmsg_text.decode('utf-8').encode('gbk')

    '''VMG文件的短信采用UTF-8编码，所以为确保转成CSV文件后，在记事本打开文本的可读性，需要进行字符编码转换：
    先使用DECODE将短信的UTF-8格式解码成UNICODE编码（UTF-8与GBK之间无直接转码函数，因此需借助UNICODE作为中转），
    然后再使用ENCODE将UNICODE编码成GBK、GB2312等编码格式，这样在中文环境下可以用记事本打开了。'''

    ''' 以下方法因需要解决一条短信内容占用多行的问题，不如采用REGEX方法简捷，故未代码未完成
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

    '''输出合并后的完整短信内容。'''
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

