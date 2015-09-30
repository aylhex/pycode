#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-12 15:27:23
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import urllib2
from bs4 import BeautifulSoup

"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
"""

rootpath = os.path.dirname(__file__)
imgdir = os.path.join(rootpath, 'img')

# 访问指定的URL，爬取所有图片的下载地址


def getImgeList(strurl):
    result = False
    try:
        strhtml = urllib2.urlopen(strurl).read()
    except urllib2.URLError, e:
        return result, e
    objhtml = BeautifulSoup(strhtml)
    tempimglist = objhtml.find_all('img')
    tempimglist = filter(ifimgcorrct, tempimglist)
    imglist = [img.get('src') for img in tempimglist]
    result = True
    # print imglist[0]
    return result, imglist


def ifimgcorrct(imgobj):
    imgclass = imgobj.get('class')
    if imgclass and u'BDE_Image' in imgclass:
    # if imgclass and u'image_original_original' in imgclass:
        return True
    else:
        return False

# 创建图片存放目录


def makedir():
    result = False
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)
    result = True
    return result

# 下载指定图片到img目录


def downloadImg(imgurl):
    result = False
    imgname = os.path.basename(imgurl)
    localpath = os.path.join(imgdir, imgname)
    print 'downloading %s' % imgname
    imgcontent = urllib2.urlopen(imgurl).read()
    with open(localpath, 'wb') as fp:
        fp.write(imgcontent)
    result = True
    return result


def main():
    strurl = u'http://tieba.baidu.com/p/2166231880'
    """
    strurl2=u'http://tieba.baidu.com/photo/p?kw=%E6%9D%89%E6%9C%AC%E6%9C%89%E7%BE%8E&ie=utf-8&flux=1&tid=\
    2166231880&pic_id=86674dafa40f4bfb85a9f275024f78f0f736187e&pn=1&fp=2&see_lz=1#!/pid5603c7160924ab18f\
    c6c8d1634fae6cd7b890b79/pn1'
    """
    result, imglist = getImgeList(strurl)
    if not result:
        print imglist
        return
    result = makedir()
    if not result:
        print 'create dir failed!'
        return
    print 'count:%d' % len(imglist)
    map(downloadImg, imglist)
    print 'END'

if __name__ == '__main__':
    main()
