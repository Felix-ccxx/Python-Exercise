# -*- coding: cp936 -*-
import urllib
import urllib2
import re

url="http://cili02.com/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
search="The.Expanse"
geturl=url+"?topic_title3="+search
headers={'User-Agent':user_agent,
         'Referer':'http://cili02.com/' }

'''把 Debug Log 打开，这样收发包的内容就会在屏幕上打印出来，方便调试
'''
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)

print geturl
request=urllib2.Request(geturl,None,headers)
response=urllib2.urlopen(request)
fhtml=open("cili.html","w+")
fhtml.write(response.read())
fhtml.close
print response.read()
