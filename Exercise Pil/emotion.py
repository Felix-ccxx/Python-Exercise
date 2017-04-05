# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:47:24 2017

@author: Administrator
"""

from PIL import Image,ImageDraw,ImageFont
img=Image.open(".\\background.jpg")
jgz=Image.open(".\\jgz.jpg")
img.paste(jgz,(73,42))
#img.show()

draw=ImageDraw.Draw(img)
ttfront=ImageFont.truetype('simhei.ttf',24)
draw.text((32,190),"我的内心毫无波动\n 甚至还想笑",fill=(0,0,0),font=ttfront)
img.show()
img.save(".\\emotion.jpg")