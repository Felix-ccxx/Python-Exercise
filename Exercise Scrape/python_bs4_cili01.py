# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup as bs
import urllib2


'''根据URL使用urllib获取HTML源文件,并写入到本地文件中保存'''
url="http://cili13.com/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
search="Person.of.Interest"     #查找的的视频资源名称
geturl=url+"?topic_title3="+search
headers={'User-Agent':user_agent,
         'Referer':'http://cili02.com/' }

request=urllib2.Request(geturl,None,headers)
response=urllib2.urlopen(request)
html=response.read()
fhtml=open(search+"_cili.html","w+")
fhtml.write(html)
fhtml.close()

'''新建文件一个用于存放提取的URL链接 '''
flist=open(search+"_down.txt","wb+")

'''根据HTML结构分析，提取当前网页中所有视频文件的名称,MAGNET和ED2K链接URL'''
#fhtml=open(search+"_cili.html","r")
#soup=bs(fhtml)
soup=bs(html)

#soup.body.find_all('div',class_='pages')    #获取总的页面数
pages=[istr for istr in soup.body.find_all('div','a',class_='pages')[0].strings if istr.isdigit()]


for i in range(len(soup.dl.find_all('span',class_='b'))):
    #soup.dl.find_all('span',class_='b')[i] #返回值包含有HTML的代码，但字符未进行编码
    files=soup.dl.find_all('span',class_='b')[i].string  #返回值准确，但字符进行了utf编码
    magurl=soup.dl.find_all('dd')[i].attrs['magnet']
    edkurl=soup.dl.find_all('dd')[i].attrs['ed2k']
    dlist=files.encode("utf-8")+"|"+magurl+"|"+edkurl+"\n\n"
    print dlist    
    flist.write(dlist)
    
flist.close()

