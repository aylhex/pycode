#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/10/24
import Image,ImageDraw,ImageFont
import random
import math
width=100
height=40
bgcolor=(255,255,255)
image=Image.new('RGB',(width,height),bgcolor)
font=ImageFont.truetype('verdana.ttf',30)
fontcolor=(122,5,139)
draw=ImageDraw.Draw(image)
strText=''
for i in random.sample(xrange(9),4):
    strText+=str(i)
print strText
draw.text((0,0),strText,font=font,fill=fontcolor)
del draw
image.save('1234_1.jpeg')
newimage=Image.new('RGB',(width,height),bgcolor)
#new image
newPix=newimage.load()
pix=image.load()
offset=0
for y in range(0,height):
    offset+=1
    for x in range(0,width):
        newx=x+offset
        if newx < width:
            newPix[newx,y]=pix[x,y]
newimage.save('1234_2.jpeg')
newimage=image.transform((width+30,height+10),Image.AFFINE,(1,-0.3,0,-0.1,1,0))
newimage.save('1234_3.jpeg')
draw=ImageDraw.Draw(newimage)
linecolor=(0,0,0)
for i in range(0,15):
    x1=random.randint(0,width)
    x2=random.randint(0,width)
    y1=random.randint(0,height)
    y2=random.randint(0,height)
    draw.line([(x1,y1),(x2,y2)],linecolor)
newimage.save('1234_4.jpeg')
newimage.show()
