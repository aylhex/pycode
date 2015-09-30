#!/usr/bin/env python
# coding:utf-8
# Author:   --<chenjun>
# Purpose:
# Created: 2015/3/6

import sys
import os
import glob2
import Image
#----------------------------------------------------------------------


def getimagelist(dirpath):
    imagelist = glob2.iglob(dirpath + '\\*.jpg')
    return imagelist


def changeimage(imagepath):
    print imagepath
    im = Image.open(imagepath)
    size = (1136, 640)
    imn = im.resize(size, Image.ANTIALIAS)
    imn.save(imagepath.replace(r'.jpg', '') + r'_result.jpg', 'jpeg')
#----------------------------------------------------------------------


def main():
    imagedir = os.path.dirname(__file__) + '\\image'
    imagelist = getimagelist(imagedir)
    map(changeimage, imagelist)

if __name__ == '__main__':
    main()
