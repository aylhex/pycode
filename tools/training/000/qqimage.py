#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import sys
import Image
import ImageDraw
import ImageFont

#----------------------------------------------------------------------


def main():
    """
    第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
    """
    thefilepath = r'e:\kuaipan\study\code\python\tools\training\1\testimg.jpg'
    dealwiththeimage(thefilepath)
#----------------------------------------------------------------------


def dealwiththeimage(thefilepath):
    """"""
    # print thefilepath
    pimage = Image.open(thefilepath)
    font = ImageFont.truetype('verdana.ttf', 100)
    fontcolor = (255, 0, 0)
    draw = ImageDraw.Draw(pimage)
    draw.text((550, 0), '7', font=font, fill=fontcolor)
    pimage.save('result.jpg')

if __name__ == '__main__':
    main()
