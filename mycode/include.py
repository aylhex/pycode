#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import sys
import os
import json
import string
import hashlib
import win32api
import ctypes
import time
dll = ctypes.windll.LoadLibrary(r'e:\code\python\res\getDigitalSigner.dll')
extlist=['.exe','.dll','.sys','.khf']
#计算文件md5
def getmd5(files):
    """"""
    try:
        a_file=open(files,'rb')
        m=hashlib.md5()
        m.update(a_file.read())
        a_file.close()
        return m.hexdigest()
    except:
        return None
def getFileVersion(filepath):
    if os.path.splitext(filepath)[1] not in extlist:
        return None
    else:
        info=win32api.GetFileVersionInfo(filepath,os.sep)
        ms = info['FileVersionMS']  
        ls = info['FileVersionLS']
        version = '%d.%d.%d.%04d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))  
        return version
def getDigitalSigner(filepath):
    try:
            if os.path.splitext(filepath)[1] not in ['.exe', '.dll', '.sys']:
                return ''
            pStr = ctypes.c_wchar_p(filepath)
            temp = dll.GetDigitalSigner(pStr)
            result = ctypes.c_wchar_p(temp).value
            result=str(result.replace('\n','\t'))
            if result<>'':
                return result
            return None
    except:
        return None
def getFileSize(filepath):
    return str(int(os.path.getsize(fpath))/(1024*1024))+'MB'
def getRelativePath(root, filepath):
    filename = os.path.basename(filepath)
    RelativePath = filepath.rsplit(filename, 1)[0].replace(root, '', 1)
    return RelativePath
def getLocalTime():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    return  time.strftime(ISOTIMEFORMAT, time.localtime())
def getFileInfo(root, filepath, channel):
    filename = os.path.basename(filepath)
    filesize = getFileSize(filepath)
    filemd5 = getFileMd5(filepath)
    filerelativepath = getRelativePath(root, filepath)
    fileversion = getFileVersion(filepath)
    filesigner = getDigitalSigner(filepath)
    return {'filename' : filename, 
            'fileversion' : fileversion, 
            'filesize' : filesize, 
            'filemd5' : filemd5, 
            'localfilepath' : filerelativepath.replace('\\', '\\\\'), 
            'channel' : channel,
            'digital_signature' : filesigner,
            }
def checkNeedFile(filename):
    suffixlist = ['.exe', '.dll', '.dat', '.apk']
    filesuf = os.path.splitext(filename)[1]
    if filesuf in suffixlist:
        return True
    else:
        return False
def getAllFiles(dirpath):
    allfiles = []
    for root, dirs, files in os.walk(dirpath):
        if os.path.join(dirpath, 'ktool_update') in root:
            continue
        if os.path.join(dirpath, 'appdata') in root:
            continue
        if os.path.join(dirpath, 'download') in root:
            continue
        for item in files:
            if checkNeedFile(item):
                allfiles.append(os.path.join(root, item))
    return allfiles
if __name__=='__main__':
    pass 