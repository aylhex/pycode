#!/usr/bin/env python
#coding:utf-8
# Author:   --<chenjun>
# Purpose: 
# Created: 2015/2/28

import sys
import random

#----------------------------------------------------------------------
def main():
    """
    第 0001 题：
    做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
    
    生成200个激活码，每个激活码20位，包含字母及数字
    """
    activcodes=[]
    codelenth=20   #激活码长度
    codenums=200   #激活码个数
    fp=open(r'activecode.txt','w')
    chrs='abcdefghjkmnpqrstuvwxyz'.upper()*2
    nums='23456789'*2
    for i in range(0,codenums):
        oldstr=list(chrs+nums)
        random.shuffle(oldstr)
        strtemp=random.sample(oldstr,codelenth)
        strtemp=''.join(strtemp)
        fp.writelines(strtemp+'\n')
        activcodes.append(strtemp)
    fp.close()
if __name__=='__main__':
    main()