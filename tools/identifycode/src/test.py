from identify import DoWork,getimpobjbymethod
import os

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
    fpath=r'e:\code\git\ImageRecognizeOf58\hack58\pic\test.jpg'
    result=DoWork(fpath)
    print ''.join(result)

def testothermethod():
    fpath='../pic/17380.jpg'
    # getimgobjbymethod(fpath)

def main():
    testothermethod()

if __name__ == '__main__':
    main()