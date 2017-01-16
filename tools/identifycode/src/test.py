import os
import json
from StringIO import StringIO
from identify import DoWork,WalkAllPics
from downloadPic import HttpDownloadIO

def testallpic():
    sum5 = 0
    for root,dirs,files in os.walk('..\pic'):
        for file in files:
            filepath = os.path.join(root,file)
            print filepath
            result =  DoWork(filepath)
            if len(result) == 5:
                sum5+=1
            print ''.join(result)
            try:
                os.rename(filepath, root+'\\'+''.join(result) + '.bmp')
            except:
                pass
    print 'approximate correct:',sum5


def GetcharTest():
    # fpath='../pic/17380.jpg'
    im=HttpDownloadIO()
    im = StringIO(im) 
    chars=DoWork(im)
    print chars

def TestWalkTmpPics():
    Pic_dir=os.path.abspath('../tmp/')
    charlist=WalkAllPics(Pic_dir)
    for i in charlist:
        print i 

def main():
    # TestWalkTmpPics()
    GetcharTest()

if __name__ == '__main__':
    main()