#!/usr/bin/env python
#coding:utf-8
# Author:   --<chenjun>
# Purpose: 
# Created: 2013/6/19

import sys
import os
import json
import string
import hashlib
import win32api
import ctypes
import time
########################################################################    
file_json='packages.json'
dll = ctypes.windll.LoadLibrary(r'e:\code\python\res\getDigitalSigner.dll')
#----------------------------------------------------------------------
#遍历给定路径
def main(fpath):
    """"""
    if fpath<>'':
        if os.path.isdir(fpath):
            for root,dirs,files in os.walk(fpath):
                for d in dirs:
                    pass
                for f in files:
                    wpath=os.path.join(fpath,f)
                    getfileinfo(wpath)
        elif os.path.isfile(fpath):
            getfileinfo(fpath)
        else:
            print 'no such file or dir!'
#----------------------------------------------------------------------
def getfileinfo(fpath):
    """获取并输出文件信息"""
    #获取单个文件各种属性
    datekeys=['_99_50','_99_51','_99_52','_99_53',]
    ff=os.path.split(fpath)
    ffname=ff[1]
    ffpath=ff[0]
    ffname_split=str(str(ffname).split('.')[0]).split('_')
    fkeytemp='_'+ffname_split[1]+'_'+ffname_split[2]
    if fkeytemp in datekeys:
        fkey=fkeytemp
    else:
        fkey=str(ffname).split('.')[0]
    fmd5=getmd5(fpath)
    fsign=getDigitalSigner(fpath)
    fsize=str(int(os.path.getsize(fpath))/(1024*1024))
    fversion=getFileVersion(fpath)
    if os.path.exists(file_json):
        fjson=open(file_json,'r')
        lines=fjson.read()
        text=json.loads(lines)
        fjson.close()
        #从json文件中匹配文件信息
        if text.has_key(fkey):
            furl=text[fkey]['url']+ffname
            fto=text[fkey]['to']
            fdate=text[fkey]['date']
            fbackup=text[fkey]['backup']
            result=[fto,ffname,furl,fmd5,fsign,fsize,fversion,fbackup,fdate,fpath,'']
            packname=packages(result)
            packname.show()
        else:
            unknow.append(ffname)
#----------------------------------------------------------------------
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
def getFileVersion(file_name):  
    try:
            info = win32api.GetFileVersionInfo(file_name,os.sep)
            ms = info['FileVersionMS']  
            ls = info['FileVersionLS']  
            version = '%d.%d.%d.%04d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))  
            return version 
    except:
        print '文件类型不对！'
        return None
def getDigitalSigner(filepath):
    try:
            if os.path.splitext(filepath)[1] not in ['.exe', '.dll', '.sys']:
                return None
            pStr = ctypes.c_wchar_p(filepath)
            temp = dll.GetDigitalSigner(pStr)
            result = ctypes.c_wchar_p(temp).value
            result=str(result.replace('\n','\t'))
            if result<>'':
                return result
            return None
    except:
        print '文件类型不对！'
        return None
########################################################################
#暂未启用安装包类
class packages():
    """
    安装包类
    用show()方法显示类属性
    """
    #----------------------------------------------------------------------
    #def __init__(self,name,to,date,url,backup,md5,path,iid=''):
    def __init__(self,lists): 
        """Constructor"""
        self.to=lists[0]
        self.name=lists[1]
        self.url=lists[2]
        self.md5=lists[3]
        self.fsign=lists[4]
        self.size=lists[5]
        self.ver=lists[6]
        self.backup=lists[7]
        self.date=lists[8]
        self.path=lists[9]
        self.iid=lists[10]
    #----------------------------------------------------------------------
    def show(self):
        """打印该类属性"""
        if self.name<>'':
            print self.to
            print 'Name: %s' %(self.name)
            print 'MD5: %s' %(self.md5)
            print 'Sign: %s' %(self.fsign)
            print 'Size: %s' %(self.size)
            print 'Ver: %s' %(self.ver)
            print 'iid: %s' %(self.iid)
            print 'downloadURL: %s' %(self.url)
            print 'Path: %s' %(self.path)
            print 'Date: %s' %(self.date)
            print 'Backup: %s' %(self.backup)
    #----------------------------------------------------------------------
    def savefile(self):
        """"""
        #try:
        pstrs=[self.to,'']
        #pstrs=[self.to,'Name: '+self.name,'MD5: '+self.md5,'Sign: '+self.fsign,'Size: '+self.size,'Ver: '+self.ver,'iid: '+self.iid,'downloadURL: '+self.url,'Path: '+self.path,'Date: '+self.date,'Backup: '+self.backup]
        #pstrs=[s+'\n' for s in pstrs]
        #for i in pstrs:
            #packagesave.write(i)
        #packagesave.write(pstrs)
            #packagesave.writelines(self)
            #packagesave.writelines('Name: '+self.name)
            #pfile.writelines(self.to)
            #pfile.writelines(self.to)
            #pfile.writelines(self.to)
            #pfile.writelines(self.to)
            #pfile.writelines(self.to)
            #pfile.writelines(self.to)
            #pfile.writelines(self.to)
            #pfile.writelines(self.to)
            #pfile.writelines(self.to)
        #except :
            #packagesave.writelines('写入信息失败！\n')
            
if __name__=='__main__':
    unknow=[]
    if os.path.exists('packageinfo.txt'):
        os.remove('packageinfo.txt')
    packagesave=open('packageinfo.txt','a+')
    packagesave.writelines(time.ctime()+'\n')
    try:
        fpath=sys.argv[1]
        main(fpath)
        print '无法识别的包('+str(len(unknow))+'):'
        for p in unknow:
            print p
    except:
        print '请输入有效路径！'
    #fpath=r'\\10.20.223.55\data\auto_setuplive\201306\26\2020'
    #fpath=r'\\dubabin\DubaTest\KIS\DailyBuild\kis_2012makesetup_fb\20130626.112149\package'
    #main(fpath)
    packagesave.close()