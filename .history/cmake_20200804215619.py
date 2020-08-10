import os
import re



def anysfile(cmfile):
    reStr = r'^set\((.*\sON)\)'
    fo = open(cmfile, "r")
    for line in fo.readlines():
        #print(line.strip())
        mathObj = re.match(reStr, line.strip())
        if mathObj:
            print(mathObj.group(1))
        else:
            print('can not find')
        


def readfile():
    curpath = os.getcwd()
    filelist = os.listdir(curpath)
    for file in filelist:
        if os.path.splitext(file)[1] == '.txt':
            anysfile(file)



def main():
    readfile()

if __name__ == '__main__':
    main()
