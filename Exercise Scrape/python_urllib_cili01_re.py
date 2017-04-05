# -*- coding: cp936 -*-
import re

fo=open("cili.html","r")
html=fo.read()
magpat=re.compile(r'magnet:\?+.*announce')
maglist=re.findall(magpat,html)
edkpat=re.compile(r'ed2k://+.*\|\/+')
edklist=re.findall(edkpat,html)
movpat=re.compile(r'(The\.Expanse.+.mkv|The\.Expanse.+.mp4){1}')
movlist=re.findall(movpat,html)
print movlist,len(movlist)


fo.close()
