#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/5/15
# setup.py
#import sys
from distutils.core import setup
import py2exe
setup(console=['getfilesinfo.py'],
      options={'py2exe':{'bundle_files':1}},
      zipfile=None)
    