import urllib
for i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') :
    urllib.urlretrieve('http://tieba.baidu.com/p/100000000' + i,'100000000' + i + '.html')
