import os
import re
import xlwt 



class excelfile:
    def __init__(self, exfile):
        self.exf = exfile
        self.wb = xlwt.Workbook();
        self.st = self.wb.add_sheet('1111')

    def write(self,col,row,value):
        self.col = col
        self.row = row
        self.st.write(self.col,self.row,value)

    def save(self):
        self.wb.save(self.exf)   
        
exfile = excelfile('D:\\junfile\\dev\\python\\1.xls')

def anysfile(cmfile):
    reStr = r'^set\((.*\sON)\)'
    fo = open(cmfile, "r")
    col = 0
    for line in fo.readlines():
        #print(line.strip())
        mathObj = re.match(reStr, line.strip())
        if mathObj:
            col = col + 1
            print(mathObj.group(1))
            exfile.write(0,col,mathObj.group(1))
        else:
            print('can not find')
        


def readfile():
    curpath = os.getcwd()
    filelist = os.listdir(curpath)

    for file in filelist:
        if os.path.splitext(file)[1] == '.txt':
            anysfile(file)

    exfile.save()



def main():
    readfile()

if __name__ == '__main__':
    main()
