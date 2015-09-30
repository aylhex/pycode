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
try:
     #dllpath=os.path.join(os.getcwd(),'getDigitalSigner.dll')
     dllpath=os.path.join(os.path.dirname(sys.argv[0]),'getDigitalSigner.dll')
     dll = ctypes.windll.LoadLibrary(dllpath)
except:
     print os.path.join(os.getcwd(),os.path.basename(sys.argv[0]))+' is not correct!!'
     sys.exit()
extlist=['.exe','.dll','.sys','.khf']
#限制大小100M
maxsize=104857600
logfile=os.path.join(os.path.dirname(sys.argv[0]),'filesinfo.log')
logs=''
def getFileVersion(filepath):
     if os.path.splitext(filepath)[1] not in extlist:
          return ''
     else:
          try:
               info=win32api.GetFileVersionInfo(filepath,os.sep)
               ms = info['FileVersionMS']  
               ls = info['FileVersionLS']
               version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))  
               return version
          except:
               return '                 '
#----------------------------------------------------------------------
def getDigitalSigner(filepath):
     """"""
     if os.path.splitext(filepath)[1] not in extlist:
          return ''
     elif os.path.getsize(filepath)>maxsize:
          return 'Exceed the limit size!\nExceed the limit size!'
     else:
          pStr = ctypes.c_wchar_p(filepath)
          temp = dll.GetDigitalSigner(pStr)
          result = ctypes.c_wchar_p(temp).value
          if result:
               return result
          else:
               return ' '
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
     if len(sys.argv)==2 and sys.argv[1]!='':
          root=sys.argv[1]
          #root=r'\\10.20.225.20\data_back\update_back_kmobile\201308\22\1152\old'
          #root=r'\\10.20.223.55\data\update_back_kav2010\201309\02\1917\old'
          fp=open(logfile,'w')
          if root[-1]=='\\':
               root=root[0:-1]
          for item in walkdir(root):
               print '%s  %s  %s  %s'%(item.name,item.version,item.time,item.signer)
               line_temp='%s  %s  %s  %s\n'%(item.name,item.version,item.time,item.signer)
               fp.writelines(line_temp)
          fp.close()
               