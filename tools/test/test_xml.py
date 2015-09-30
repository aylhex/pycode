#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/12/26

import sys
from xml.etree import ElementTree
def readxml(path):
    root=ElementTree.parse(path)
    process=root.getiterator('Progress')
    for p in process:
        print p.attrib
        for child in p.getchildren():
            print child.tag,':',child.text
if __name__=='__main__':
    path=r'e:\code\python\test\game.xml'
    readxml(path)