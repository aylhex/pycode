#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/1/23
import random

strList=['1234','sheff','abcd','banana','python','c++','cj']

#----------------------------------------------------------------------
def get_randomstrs(strList,num):
    """"""
    strList=strList
    num=num
    result=random.sample(strList,num)
    return result
#----------------------------------------------------------------------
def getstrlist():
    """"""
    chrs='abcdefghjkmnpqrstuvwxyz'.upper()
    return chrs
#----------------------------------------------------------------------
def getnums():
    """"""
    nums='23456789'
    return nums
#----------------------------------------------------------------------
def getmixstrs():
    """"""
    chrs='abcdefghjkmnpqrstuvwxyz'.upper()+'23456789'
    return chrs
#----------------------------------------------------------------------
if __name__=='__main__':
    print get_randomstrs(getmixstrs(),4)
    print get_randomstrs(getnums(),4)
    print get_randomstrs(getstrlist(),4)