#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/7/29

import random
secret = random.randint(1,10)
print("-------------我爱------------")
temp = raw_input("请输入一个数字: ")
guess = int(temp)
i = 0
while i<3:
    if guess==secret:
        print("succeed!")
        i=3
    else:
        if guess < secret:
            temp=raw_input("sorry,smaller")
            guess = int(temp)
            i=i+1
        else:
            if guess>secret:
                temp=raw_input("sorry,bigger")
                guess=int(temp)
                i=i+1
print("game over")