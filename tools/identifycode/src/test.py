from identify import DoWork
import os
import json

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

def test():
    fpath='../pic/17380.jpg'
    fn=os.path.basename(fpath).split(r'.')[0]
    print fn

def GetcharTest():
    fpath='../pic/17380.jpg'
    chars=DoWork(fpath)
    print chars

def main():
    GetcharTest()

if __name__ == '__main__':
    main()