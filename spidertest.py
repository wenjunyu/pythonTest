import requests
import xlwt
from bs4 import BeautifulSoup
url="https://blog.csdn.net/LI_AINY"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
ss=None
try:
    r=requests.get(url,headers=headers,timeout=30)
    # print(r.text)
    # r.raise_for_status()    
    # print("网页编码是："+r.encoding)
    # # print(r.)
    # # 获取页面内容
    # # print(r.text)
    # 给excel放数据的  一个就是一行
    all_lists = []
    book = xlwt.Workbook(encoding='utf-8')#创建工作簿
    soup = BeautifulSoup(r.text, 'lxml')
    # 下面的这种方法会报错   TypeError("'NoneType' object is not callable")
    # ss=soup.findall("class",class_="article-item-box csdn-tracking-statistics")
    # 找到所有class为article-item-box csdn-tracking-statistics的节点
    row0 = ['文章标题','文章链接']#定义表头，即Excel中第一行标题
    sheet = book.add_sheet('AINY',cell_overwrite_ok=True)
    sheet.write(0,0,row0[0])#写入表
    sheet.write(0,1,row0[1])#写入表
    for s in soup.findAll(name="div", attrs={"class" :"article-item-box csdn-tracking-statistics"}):
    	for ss in s.findAll(name="h4"):
    		sss=ss.find(name="a",href=True);
    		print("文章标题："+ss.getText().replace("原","").strip()+"\n文章链接："+sss['href'])
    		list=[ss.getText().replace("原","").strip(),sss['href']]
    		all_lists.append(list)
    #第一行开始
    i=1
    for all_list in all_lists:
    	j=0
    	for data in all_list:
    		sheet.write(i,j,data)#迭代列，并写入数据，#重新设置，需要cell_overwrite_ok=True
    		j+=1
    	i+=1
    book.save("AINY.xls")
    print("导出成功！")
except Exception as e:
    print("出现异常------异常信息："+repr(e));
