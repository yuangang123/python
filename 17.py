import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html.read())
table = bsObj.findAll("table",{"class":"wikitable sortable"})
print(table)
