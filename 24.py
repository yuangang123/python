#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def ngrams(input,n):
    input = re.sub('\n+'," ",input)
    input = re.sub(' +'," ",input)
    input = bytes(input, encoding = "utf8")
    input = input.decode("ascii","ignore")
    print (input)
    input= input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output
html= urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj= BeautifulSoup(html.read())
content = bsObj.find('div',{'id':'mw-content-text'})
content=content.get_text()

ngrams=ngrams(content,2)
print(ngrams)
print("2-grams count is:"+str(len(ngrams)))
