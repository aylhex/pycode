import json
import sys
import os

def show(char):
    fpath='../json_zhuhai/%s.json'%char
    if not os.path.exists(fpath):
        print 'The json file is not exist!'
        return
    with open(fpath) as f:
        dic = json.loads(f.read())
        # print dic
        for j in xrange(dic['height']):
            for i in xrange(dic['width']):
                if [i,j] in dic['points']:
                    print 'O',
                else:
                    print ' ',
            print '\n'
                    

def main():
    if len(sys.argv)>1:
        strcheck=sys.argv[1]
        show(strcheck)
    else:
        show('2')

    
if __name__ == '__main__':  
    main()