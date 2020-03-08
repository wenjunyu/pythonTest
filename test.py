# -*- coding = utf-8 -*-
import urllib.request

url = 'http://www.dygangs.com/ys'

response = urllib.request.urlopen(url)

print("status code :",response.getcode())
data = response.read().decode('gb18030')
print(data)

htmlfile = open('dygang.html','w',encoding='gb18030')
htmlfile.write(data)
htmlfile.close()