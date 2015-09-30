#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-01 00:33:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import string
import random
from PIL import Image, ImageDraw, ImageFont

"""
第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
"""


def createstrcode():
    lencode = 4
    strletters = 'abcdefghjkmnpqrstuvwxyz'.upper()
    strnums = '23456789'
    strlist = list(strletters * 2 + strnums * 2)
    random.shuffle(strlist)
    strcode = random.sample(strlist, lencode)
    return ' '.join(strcode)


def createImage(strcode):
    width = 110
    height = 35
    bgcolor = (171,140,171)
    #字体设置
    font = ImageFont.truetype('verdana.ttf', 28)
    #字体颜色
    fontcolor = (100,84,129)
    #画布大小
    imagesize = (width, height)
    #创建画布
    image = Image.new('RGB', imagesize, bgcolor)
    draw = ImageDraw.Draw(image)
    #将随机字符写入图片
    draw.text((0, 0), strcode, font=font, fill=fontcolor)
    image.save('test.gif', 'GIF')
    # image.show()
    return True


def main():
    strcode = createstrcode()
    result = createImage(strcode)
    print strcode, result

if __name__ == '__main__':
    main()
