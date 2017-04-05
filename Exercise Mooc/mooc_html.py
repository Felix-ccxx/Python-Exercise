#Python 2.7
import urllib

filext='.html'
urlhttp=r'http://tieba.baidu.com/p/'
count=1

for i in range(1000000000,1000000010):
    url=urlhttp+str(i)
    htmlfile=str(i)+filext
    rurl=urllib.urlopen(url)
    html=rurl.read()
    f=open(htmlfile,'wb')
    f.write(html)
    f.close()
    print 'The HTML file:'+htmlfile+' is created.'
else:
    print 'All HTML files is created.'
    
