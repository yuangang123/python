from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup
wordFile = urlopen("http://www.pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
#将远程word文档读成一个二进制文档，再用Python的标准库zipfile进行文件的解压，然后读取这个文件，就变成xml了
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

print(xml_content.decode('utf-8'))

textString=BeautifulSoup(xml_content.decode('utf-8')).find("w:t")

print(len(textString))

print(textString)
