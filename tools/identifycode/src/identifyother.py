#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-05 10:28:49
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import os
import sys
import json
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

DEBUG = False
# the num of chars
charnum = 5  
# start postion of first number
xstart = 6
# width of each number
xwidth = 9
# start postion of top 
ystart = 5
# height of each number
yhigh = 13  

def ImgFilter(image_name):
    im = Image.open(image_name)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    # im.show()
    return im

# split five numbers in the picture
def CropPic(imobj):
    im_crop_list = []
    # cut every char
    for i in range(charnum):
        im1 = imobj.crop((xstart+xwidth*i, ystart, xstart+xwidth*(i+1), ystart+yhigh))
        im_crop_list.append(im1)
    return im_crop_list

# 单个图片字模的提取
def ExtractCharFromOnePic(imobj):
    chardata=[]
    for i in range(yhigh):
        for j in range(xwidth):
            if (imobj.getpixel((j, i)) == 255):
                # set 0 if white
                chardata.append(0)
            else:
                # set 1 if black
                chardata.append(1)
    return chardata

# 提取所有字模数据
def ExtractChars(im_crop_list):
    f = open("data.txt", "a")
    for k in range(charnum):
        l = ExtractCharFromOnePic(im_crop_list[k])
        f.write("l=[")

        n = 0
        for i in l:
            if (n % xwidth == 0):
                f.write("\n")
            f.write(str(i)+",")
            n += 1
        f.write("]\n")
    f.close()
    return True

# 匹配最合适的字符，不过代码太扯淡了
def Get_Num(l):
    if not l:
        return ""
    # 图片比字模多出的点的数目
    min1 = []
    # 字模比图片多出的点的数目
    min2 = []
    # 遍历字模库，匹配字模
    for n in Data.N:
        # 图片中1的数目,图片&字模中1的数目，字模中1的数目，字模&图片中1的数目,
        count1 = count2 = count3 = count4 = 0
        # 像素不匹配
        if (len(l) != len(n)):
            print "Wrong pic"
            exit()
        for i in range(len(l)):
            if (l[i] == 1):
                count1 += 1
                if (n[i] == 1):
                    count2 += 1
        for i in range(len(l)):
            if (n[i] == 1):
                count3 += 1
                if (l[i] == 1):
                    count4 += 1
        min1.append(count1-count2)
        min2.append(count3-count4)
    # 下面这些代码太局限了
    for i in range(10):
        if (min1[i] <= 2 or min2[i] <= 2):
            if ((abs(min1[i] - min2[i])) < 10):
                return i
    for i in range(10):
        if (min1[i] <= 4 or min2[i] <= 4):
            if (abs(min1[i] - min2[i]) <= 2):
                return i

    for i in range(10):
        flag = False
        if (min1[i] <= 3 or min2[i] <= 3):
            for j in range(10):
                if (j != i and (min1[j] < 5 or min2[j]<5)):
                    flag = True
                else:
                    pass
            if (not flag):
                return i
    for i in range(10):
        if (min1[i] <= 5 or min2[i] <= 5):
            if (abs(min1[i] - min2[i]) <= 10):
                return i
    for i in range(10):
        if (min1[i] <= 10 or min2[i] <= 10):
            if (abs(min1[i] - min2[i]) <= 3):
                return i

def Pic_Reg(image_name=None):
    im = ImgFilter(image_name)
    im_crop_list = CropPic(im)
    s = ""
    for k in range(charnum):
        l = ExtractCharFromOnePic(im_crop_list[k])
        s += str(Get_Num(l))
    return s


def main():
    image_name = '../pic/96859.jpg'
    imobj = ImgFilter(image_name)
    im_crop_list=CropPic(imobj)
    ExtractChars(im_crop_list)
    # print Pic_Reg(image_name)

if __name__ == '__main__':
    main()
