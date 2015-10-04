import sys
from collectfont import show
                    

def main():
    if len(sys.argv)>1:
        strcheck=sys.argv[1]
        show(strcheck)
    else:
        show('2')

    
if __name__ == '__main__':  
    main()