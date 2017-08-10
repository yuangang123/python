from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html)

print("这里是打印出来孩子节点：")
for child in bsobj.find("table",{"id":"giftList"}).children:
    print(child)
    
print("这里打印出来是兄弟节点：")
for sibling in bsobj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
    
print("这里打印出来是父亲标签的内容：")
print(bsobj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

print("使用正则表达式来抓取图片：")
images=bsobj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image)
    
print("获取img的全部属性")
image=bsobj.find("img",{"src":"../img/gifts/logo.jpg"})

      
print("使用lambda表达式来采集数据：")
tags=bsobj.findAll(lambda tag:len(tag.attrs)==2)
for tag in tags:
    print(tag)
