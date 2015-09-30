#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import cmd_color
from filecmp import dircmp
import logging
import os,sys
import string
import time
import urllib

basedir=os.getcwd()
#basedir=os.path.dirname(__file__)
basedir2=basedir+os.sep+'data'
configpath=basedir+os.sep+'config.txt'
datalist=basedir+os.sep+'datalist.txt'
tryno=['1509','1335','1337','1334']
str_pre=r'http://cu005.www.duba.net'
data_path_strs=r'anon_root\duba\2013\krcmdmon\pop'
krcmdom_strs='update_back_krcmdmon'
def logger():
    """"""
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh=logging.FileHandler(os.path.join(os.getcwd(),'log.txt'),'w')
    fh.setLevel(logging.DEBUG)
    fm=logging.Formatter("%(asctime)s  %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fm)
    logger.addHandler(fh)
    debug=logger.debug
    return debug
#----------------------------------------------------------------------
def download():
    if os.path.exists(basedir2):
        debug('%s exists!',basedir2)
        cmd='rmdir'+' /s'+' /q '+basedir2
        os.system(cmd)
        debug('del %s',basedir2)
    if not os.path.exists(configpath):
        print 'file not exists:'+configpath
        debug('config file not exist!')
        config=''
    else:
        #---
        configop=file(configpath,'r')
        config=configop.readlines()
        debug('read config success')
        #---
    for urls in config:
        #---
        urls=urls.strip(' \n')
        urltemp=urls.split('/')
        filename=urltemp[len(urltemp)-1]
        dirtemp2=urltemp[len(urltemp)-3]
        dirtemp1=urltemp[len(urltemp)-2]
        if  dirtemp1 in tryno:
            filesdir=basedir2+os.sep+dirtemp1
        elif dirtemp2 in tryno:
            filesdir=basedir2+os.sep+dirtemp2+os.sep+dirtemp1
        else:
            filesdir=basedir2
        fs=os.path.exists(filesdir)
        debug('file dir: %s',filesdir)
        if not fs:
            try:
                os.makedirs(filesdir)
                debug('create dir %s',filesdir)
            except:
                #print 'Failed to makedir:'+filesdir
                debug('Failed to makedir:%s',filesdir)
        if filesdir:
            local=filesdir+os.sep+filename
        else:
            local=filename
        try:
            #print 'Start download:'+urls,
            debug('Local path:%s',local)
            debug('Start download:%s',urls)
            clr.print_green_text(urls)
            print 'downloading...'
            urllib.urlretrieve(urls,local,cbk)
        except:
            #print 'Error download:'+local
            #debug('Error download:%s',local)
            clr.print_red_text('Error download:%s'+local)
#----------------------------------------------------------------------
def cbk(a,b,c):
    ''''
    callback func
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print '%.2f%%' %per
#----------------------------------------------------------------------
#get download url
def getDLurl(path):
    """"""
    result=[]
    path_fornet=os.path.join(path,'anon_root')
    for root,dirs,files in os.walk(path_fornet):
        for d in dirs:
            pass
        for f in files:
            fpath=os.path.join(root,f)
            path_forurl=fpath.replace(path_fornet,str_pre)
            path_forurl=path_forurl.replace('\\','/')
            result.append(path_forurl)
            #print path_forurl
    return result
def comparefiles(datadirlist):
    #clr.print_green_text('start compare files')
    debug('start compare files')
    for datapath in datadirlist:
        datapath=str(datapath).strip(' \n')
        if not datapath:
            continue
        if datapath.find(krcmdom_strs)==-1:
            print '[%s] is not krcmdmon data' %datapath
            continue
        try:
            comparepath_res=os.path.join(datapath,data_path_strs)
            cmpdirs=dircmp(comparepath_res,basedir2,ignore=None, hide=None)
            clr.print_green_text('[%s]'%datapath)
            clr.print_red_text('Differing files :')
            cmpdirs.report_full_closure()
        except:
            print 'Wrong path!'
        #print cmpdirs.diff_files
        #differant_files=''
        #if cmpdirs.diff_files:
            #for i in cmpdirs.diff_files:
                #differant_files+='|'+i
            #print 'diff files:',differant_files
            #debug('diff files:'+differant_files)
        #else:
            #print 'All files same!'
            #debug('All files same!')
#----------------------------------------------------------------------
class dircmpsub(dircmp):
    def __ini__(self,a,b):
        dircmp.__init__(self, a, b, ignore=None, hide=None)
    def report(self):
        if self.diff_files:
            self.diff_files.sort()
            print 'Differing files :', self.diff_files
    def report_full_closure(self): # Report on self and subdirs recursively
        self.report()
        for sd in self.subdirs.itervalues():
            print
            sd.report_full_closure()
def main():
    """"""
    urllist=[]
    os.system('cls')
    if os.path.exists(datalist) and os.path.getsize(datalist)>=50:
        clr.print_green_text('====> Download krcmdmon data <====')
        debug('found datalist')
        print 'found datalist.txt'
        dp=open(datalist,'r')
        cp=open(configpath,'w')
        datapathlist=dp.readlines()
        for i in datapathlist:
            i=str(i).strip(' \n')
            result=getDLurl(i)
            urllist.extend(result)
        for j in urllist:
            cp.write(j+'\n')
        dp.close()
        cp.close()
        clr.print_green_text('-'*10+'Downloading'+'-'*10)
        download()
        clr.print_green_text('Finished download!')
        debug('Finished download!')
        clr.print_green_text('-'*10+'Compare files'+'-'*10)
        comparefiles(datapathlist)
        clr.print_green_text('-'*33)
        print 'press any key to continue'
        os.system('pause>nul')
    else:
        debug('get config.txt')
        print 'get config.txt'
        clr.print_green_text('-'*10+'Downloading'+'-'*10)
        download()
        clr.print_green_text('Finished download!')
        debug('Finished download!')
if __name__=='__main__':
    debug=logger()
    clr=cmd_color.Color()
    while True:
        main()
    #print os.path.dirname(__file__)
    