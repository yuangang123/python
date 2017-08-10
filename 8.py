from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
def getLinks(url):
    global pages
    html = urlopen("http://en.wikipedia.org"+url)
    bsobj = BeautifulSoup(html)
    for link in bsobj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                getLinks(newpage)

getLinks("")
