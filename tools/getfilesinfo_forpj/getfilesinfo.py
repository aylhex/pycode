#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$
import os,sys
import win32api
import ctypes
try:
     #dllpath=os.path.join(os.getcwd(),'getDigitalSigner.dll')
     #dllpath=os.path.join(os.path.dirname(sys.argv[0]),'mysite.dll')
     dllpath='mysite.dll'
     dll = ctypes.windll.LoadLibrary(dllpath)
except:
     print os.path.join(os.getcwd(),os.path.basename(sys.argv[0]))+' is not correct!!'
     sys.exit()
extlist=['.exe','.dll','.sys','.khf']
exclist=['openssl.exe','adbwinapi2.dll','aapt.exe']
null='Null'
#限制大小100M
maxsize=104857600
def getFileVersion(filepath):
     if os.path.splitext(filepath)[1] not in extlist:
          return null
     else:
          try:
               info=win32api.GetFileVersionInfo(filepath,os.sep)
               ms = info['FileVersionMS']  
               ls = info['FileVersionLS']
               version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))  
               return version
          except:
               return None
#----------------------------------------------------------------------
def getDigitalSigner(filepath):
     """"""
     if os.path.splitext(filepath)[1] not in extlist:
          return null+'\n'+null
     #elif os.path.getsize(filepath)>maxsize:
          #return None
     else:
          try:
               pStr = ctypes.c_wchar_p(filepath)
               temp = dll.GetDigitalSigner(pStr)
               result = ctypes.c_wchar_p(temp).value
               return result
          except:
               return None
#----------------------------------------------------------------------
def walkdir(root):
     """"""
     signresult=False
     #finfo=[]
     dirtemp=root
     if root=='\\':
          return signresult
     else:
          if root[-1]=='\\':
               root=root[0:-1]
          for root,dirs,files in os.walk(root,topdown=False):
               for f in files:
                    fpath=os.path.join(root,f)
                    fname=fpath.replace(dirtemp+os.sep,'')
                    fv=getFileVersion(fpath)
                    fs=getDigitalSigner(fpath)
                    fs=str(getDigitalSigner(fpath)).split('\n')
                    if fv and len(fs)==2:
                         signresult=True
                         continue
                    elif fname in exclist and len(fs)==2:
                         signresult=True
                         continue
                    else:
                         signresult=False
                         break
          return signresult
#----------------------------------------------------------------------
def main(filepath):
     """"""
     result=False
     if os.path.splitext(filepath)[1] not in extlist:
          return True
     fver=getFileVersion(filepath)
     sign=getDigitalSigner(filepath)
     if sign and fver:
          result_list=sign.split('\n')
          if len(result_list)==2 and result_list[0] and result_list[1]:
               result=True
          else:
               result=False
     else:
          result=False
     return result
     
if __name__=='__main__':
     if len(sys.argv)==2 and sys.argv[1]:
          filepath=sys.argv[1]
          #root=r'\\10.20.225.20\data_back\update_back_kmobile\201308\22\1152\old'
          #root=r'\\10.20.223.55\data\update_back_kav2010\201307\25\1926\old'
          #root=r'\\10.20.223.55\data\update_back_kav2010\201307\29\2004\old'
          #root=r'C:\Program Files (x86)\KingSoft\kingsoft antivirus\kxecore'
          print main(filepath)




               