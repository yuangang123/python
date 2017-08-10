from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
print("使用正则表达式，beautifulsoup，来遍历单个域名：（如下）")

def getLink(url):
    html = urlopen("http://en.wikipedia.org"+url)
    bsobj= BeautifulSoup(html)
    return bsobj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
link = getLink("/wiki/Kevin_Bacon")
while len(link)>0:
    newAticle = link[random.randint(0,len(link)-1,)].attrs["href"]
    print(newAticle)
    link = getLink(newAticle)
