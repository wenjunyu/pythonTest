# 自动获取电影资源

import requests
from lxml import etree

def text(url):
    html = requests.get(url)

    html.encoding = 'gb2312'
    _selector = etree.HTML(html.text)
    
    return _selector

selector = text('https://www.ygdy8.com/index.html')

#获取“最新电影”
content = selector.xpath('//*[@id="header"]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table/tr')

for tr in content:
    _url = tr.xpath('td[1]/a[2]/@href')
    if len(_url) > 0:
        selector = text('https://www.ygdy8.com' + _url[0])

        href = selector.xpath('//*[@id="Zoom"]//@href')
        font = selector.xpath('//*[@id="header"]/div/div[3]/div[3]/div[1]/div[2]/div[1]/h1/font/text()')
        
        print('name:    ' + font[0])
        if len(href) > 1:
            print('url:    ' + href[1])
        else:
            print('url:    ' + href[0])