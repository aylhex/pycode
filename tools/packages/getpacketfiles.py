#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/11/20
import sys,os
sys.path.append('../../mycode')
from read_data import xml_parse
def main():
    rootdir=r'e:\temp\test\installfile'
    xmlpath=os.path.join(rootdir,'packet.xml')
    dirs,files=xml_parse(xmlpath)
    #print 'xmlinfo:'
    #print len(files),len(dirs)
    pathlist_dir,pathlist_file=getfilesinxml(rootdir,dirs,files)   #files path in xml
    print 'xmlfile path:'
    print len(pathlist_file),len(pathlist_dir)
    #for x in pathlist_file:
        #print x
    allfilelist=allfiles(rootdir)        #all local file's path  
    print 'all files:'
    print len(allfilelist)
    #for x in allfilelist:
        #print x
    dellist=filenotcorect(allfilelist,pathlist_file)   #files not in xml
    print len(dellist)
    for x in dellist:
        print x
def getfilesinxml(rootdir,dirs,files):
    pathlist_file=[os.path.join(rootdir,x) for x in files]
    pathlist_dir=[os.path.join(rootdir,x) for x in dirs]
    return (pathlist_dir,pathlist_file)
def allfiles(rootdir):
    fpathlist=[]
    for root,dirs,files in os.walk(rootdir):
        flist=[os.path.join(root,f) for f in files]
        fpathlist.extend(flist)
    return fpathlist
def filenotcorect(allfilelist,xmlfilelist):
    resultlist=[]
    a=set(allfilelist)
    b=set(xmlfilelist)
    resultlist=a-b
    return resultlist
if __name__=='__main__':
    #unittest.main()
    main()
    