import os
import re
import xlwt 



class excelfile:
    def __init__(self, exfile):
        self.exf = exfile
        self.wb = xlwt.Workbook();
        self.st = self.wb.add_sheet('My Worksheet')

    def write(self,col,row,value):
        self.col = col
        self.row = row
        self.st.write(self.col,self.row,value)

    def save(self):
        self.wb.save(self.exf)   



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
