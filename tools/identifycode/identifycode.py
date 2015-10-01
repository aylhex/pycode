#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-01 09:11:40
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

"""
To indentify the pic code
no zuo no die

要安装pytesseract库，必须先安装其依赖的PIL及tesseract-ocr，其中PIL为图像处理库，而后面的tesseract-ocr则为google的ocr识别引擎。
1、PIL 下载地址：
PIL-1.1.7.win-amd64-py2.7.exe
PIL-1.1.7.win32-py2.7.exe
或者直接使用pillow来代替，使用方法基本没有什么区别。
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
2、tesseract-ocr下载地址：
http://tesseract-ocr.googlecode.com/files/tesseract-ocr-setup-3.02.02.exe
3、pytesseract安装
直接使用pip install pytesseract安装即可，或者使用easy_install pytesseract

"""

import os
import pytesseract
from PIL import Image


def GetCodeByTess(fpath):
    image = Image.open(fpath)
    vcode = pytesseract.image_to_string(image)
    return vcode


def GetCodeByPIL(fpath):
    vcode = None
    return vcode


def main():
    fpath = 'ValidateCodeHeper.jpg'
    print fpath
    vcode = GetCodeByTess(fpath)
    print vcode

if __name__ == '__main__':
    main()
