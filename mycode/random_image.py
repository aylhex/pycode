#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/10/24
import Image,ImageDraw,ImageFont
import random
import get_random
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
width=90
height=40
bgcolor=(192,192,192)
font=ImageFont.truetype('verdana.ttf',25)
fontcolor=(255,12,25)
#imgpath=r'E:/web/www/static/img/python_img/'
def create_img():
    strText=''
    mstream=StringIO.StringIO()
    for i in get_random.get_randomstrs(get_random.getmixstrs(),4):
        strText+=str(i)
    #print strText
    image=Image.new('RGB',(width,height),bgcolor)
    draw=ImageDraw.Draw(image)
    draw.text((0,0),strText,font=font,fill=fontcolor)
    del draw
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
    draw=ImageDraw.Draw(newimage)
    linecolor=(0,0,0)
    for i in range(0,15):
        x1=random.randint(0,width)
        x2=random.randint(0,width)
        y1=random.randint(0,height)
        y2=random.randint(0,height)
        draw.line([(x1,y1),(x2,y2)],linecolor)
    newimage.save(mstream,'GIF')
    #newimage.save(imgpath+'imgcode.gif')
    return strText,mstream.getvalue()
if __name__=='__main__':
    print create_img()[0]