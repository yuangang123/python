from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.baidu.com")
print(html.read())
bsObj = BeautifulSoup(YOUR_MARKUO,html.read(),markup_type=markup_type);
print(bsObj.h1)
