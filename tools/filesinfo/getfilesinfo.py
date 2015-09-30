#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/6/9
import sys
import os
import win32api
import time
import ctypes
dll = ctypes.windll.LoadLibrary(r'e:\web\www\php\script\getDigitalSigner.dll')
extlist=['.exe','.dll','.sys','.khf']
maxsize=26214400
str_temp='00'
def getFileVersion(filepath):
     if os.path.splitext(filepath)[1] not in extlist:
          return str_temp
     #elif os.path.getsize(filepath)>maxsize:
          #return None
     else:
          try:
               info=win32api.GetFileVersionInfo(filepath,os.sep)
               ms = info['FileVersionMS']  
               ls = info['FileVersionLS']
               version = '%d.%d.%d.%04d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))  
               return version
          except:
               return None
#----------------------------------------------------------------------
def getDigitalSigner(filepath):
     """"""
     if os.path.splitext(filepath)[1] not in extlist:
          return str_temp+'\n'+str_temp
     elif os.path.getsize(filepath)>maxsize:
          return 'Exceed the limit size!\nExceed the limit size!'
     else:
          pStr = ctypes.c_wchar_p(filepath)
          temp = dll.GetDigitalSigner(pStr)
          result = ctypes.c_wchar_p(temp).value
          if result:
               return result
          else:
               return None
########################################################################
class singlefile():
     """"""
     #----------------------------------------------------------------------
     def __init__(self,fn='',fv='',fs='',ft=''):
          """Constructor"""
          self.name=fn
          self.version=fv
          self.signer=fs
          self.time=ft
     
#----------------------------------------------------------------------
def walkdir(root):
     """"""
     finfo=[]
     dirtemp=root
     if root=='\\':
          return []
     else:
          for root,dirs,files in os.walk(root,topdown=False):
               for f in files:
                    fpath=os.path.join(root,f)
                    fname=fpath.replace(dirtemp+os.sep,'')
                    #if os.path.splitext(fpath)[1] in extlist:
                    fv=getFileVersion(fpath)
                    fs=str(getDigitalSigner(fpath)).split('\n')
                    if len(fs)<2:
                         fs.append('')
                    item=singlefile(fname,fv,fs[0],fs[1])
                    #else:
                         #item=singlefile(fname)
                    finfo.append(item)
          return finfo
if __name__=='__main__':
     #if sys.argv[1]!='':
          #root=sys.argv[1]
          #root=r'\\10.20.225.20\data_back\update_back_kmobile\201308\22\1152\old'
          root=r'\\10.20.223.55\data\update_back_kav2010\201307\25\1926\old'
          if root[-1]=='\\':
               root=root[0:-1]
          for item in walkdir(root):
               print item.name,item.version,item.signer,item.time