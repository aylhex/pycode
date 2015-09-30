#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*- 

import os,sys,ftplib
i = 0
downloaddir = ['/dubarelease/updata/UpdateIndex_kav2010/backFile',
            '/dubarelease/updata/UpdateIndex_kcomponent/backFile',
            '/dubarelease/updata/UpdateIndex_kmobile/backFile',
            '/dubarelease/updata/UpdateIndex_kvalue/backFile',
            '/dubarelease/updata/UpdateIndex_kxe_app/backFile',
            '/dubarelease/updata/UpdateIndex_kxe_arch/backFile',
            '/dubarelease/updata/UpdateIndex_kxe_com/backFile',
            '/dubarelease/updata/UpdateIndex_kxe_data/backFile']
TryNoList = ['1508','1337','1509','1335','1334']


FilterDir = ['indexfile','old','MD5SUM.md5']

FiterChannel = ['kav2010','kmobile','kxe_app','kxe_com']
FiterChannelA = ['kcomponent','kvalue','kxe_arch','kxe_data']

class FoundExcepton(Exception):
    pass
class FTPSync(object):
    def __init__(self):
        self.conn = ftplib.FTP('10.20.220.119', 'readupdata', 'readupdatabak')
        self.conn.cwd('/')        # 远端FTP目录
        self.d = FoundExcepton()
     
    def RegConfig(self):
        Channel = []
        ChannelA = []
        fp = open("config.ini","r")
        for line in fp:
            line = line.strip()
            if line == "Channel":
                for line in fp:
                    line = line.strip()
                    Channel.append(line)
                    if line == "ChannelA":
                        Channel.remove(line)
                        for line in fp:
                            line = line.strip()
                            ChannelA.append(line)
        fp.close()
        
        return (Channel,ChannelA)
            
    def GetChanenl(self,str):
        for line in FiterChannel:
            if line in str:
                return True

        for line in FiterChannelA:
            if line in str:
                return False
        
            
    def is_num_by_except(self,num):
        try:
            int(num)
            return True
        except ValueError:
            return False
        
    def get_dirs_files(self):
        u''' 得到当前目录和文件, 放入dir_res列表 '''
        dir_res = []
        self.conn.dir('.', dir_res.append)
        files = [f.split(None, 8)[-1] for f in dir_res if f.startswith('-')]
        dirs = [f.split(None, 8)[-1] for f in dir_res if f.startswith('d')]
        return  (files,dirs)
    
    def GetFile(self,next_dir,LocalPath):
        global i
        self.conn.cwd(next_dir)
        os.chdir(LocalPath)

        ftp_curr_dir = self.conn.pwd()
        local_curr_dir = os.getcwd()
        files,dirs = self.get_dirs_files()
        for f in files:
            if f in FilterDir:
                pass
            else:
                outf = open(f, 'wb')
                try:
                    self.conn.retrbinary('RETR %s' % f, outf.write)
                finally:
                    outf.close()
          
        for d in dirs:
            self.conn.cwd(ftp_curr_dir)
            if d in FilterDir:
                continue
            if d == "duba":
                self.GetFile(d,LocalPath)
            else:
                SaveFile = self.GetLocalDir(LocalPath,d)
                self.GetFile(d,SaveFile)
       
                
    
    def GetLocalDir(self,path,filename):
        filepath = os.path.join(path,filename)
        try:
            os.makedirs(filepath)
        except:
            pass
        return filepath

    def walk(self, next_dir,LocalPath,a):
        global i
       # print next_dir
        self.conn.cwd(next_dir)
        os.chdir(LocalPath)

        ftp_curr_dir = self.conn.pwd()
        local_curr_dir = os.getcwd()

        files,dirs = self.get_dirs_files()
        
        
        for f in files:
            if f in FilterDir:
                pass
            else:
                outf = open(f, 'wb')
                try:
                    self.conn.retrbinary('RETR %s' % f, outf.write)
                finally:
                    outf.close()
        for d in dirs:
            self.conn.cwd(ftp_curr_dir)
            if d == "anon_root":
                print ftp_curr_dir
                self.GetFile(d,LocalPath)
                i = 1
                dirs = []
                continue
            if self.is_num_by_except(d) == True and i == 0:
                d = dirs[len(dirs) -1]
                self.walk(d,LocalPath,a)
            else:
                if d in FilterDir:
                    continue
                else:
                    if i == 1 and a == 0:
                        continue
                    if i == 1 and a == 1 and len(ftp_curr_dir.split('/')) == 5:
                        i = 0
                        self.walk(d,LocalPath,a)
                    if i == 0:
                        self.walk(d,LocalPath,a)
            
    def run(self):
        global i
        Channel,ChannelA = self.RegConfig()
        
        for tryno in TryNoList:
            for line in Channel:
                dir1 = line + '/' + tryno
                path = os.path.dirname(sys.argv[0])  + "\\duba"
                try:
                    os.makedirs(path)
                except:
                    pass
        
                i = 0
                self.walk(dir1,path,0)
                
        for line in ChannelA:
            dir1 = line
            path = os.path.dirname(sys.argv[0]) + '\\' + "\\duba"
            try:
                os.makedirs(path)
            except:
                pass
        
            i = 0
            self.walk(dir1,path,1)

def main():
    d = FoundExcepton()
    f = FTPSync()
    f.run()

if __name__ == '__main__':
    main()