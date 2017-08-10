from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

#获取页面所有內链的列表
def getInternalLinks(bsObj,includeUrl):
    internalLinks = []
    #找出所有以/开头的链接
    for link in bsObj.find("a",href=re.compile("^(/|.*)"+includeUrl+")")):
        if link.attrs['href']is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.appen(link.attrs['href'])
    
    return internalLinks

#获取所有外链接的列表
def getExterbalLinks(bsObj,excludeUrl):
    externalLinks =[]
    #找出不所有www开头或者http开头且不包含当前的URL的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks =getExterbalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks) ==0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
    else :
        return externalLinks[random.randint(0,len(externalLinks)-1)]
    
def followExternalOnly(startingSite):
    externalLink =getRandomExternalLinks("http://oreilly.com")
    print("随机外链接是："+externalLink)
    followExternalOnly(externalLink)
    
#followExternalOnly("http://oreilly.com")
#收集网站上发现的所有外链接列表
allExtLinks=set()
allIntLinks=set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html)
    internalLinks =getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks = getExterbalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            print(link)
getAllExternalLinks("http://oreilly.com")
    
