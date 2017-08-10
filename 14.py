import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


downloadDirectory = "downloaded"
baseUrl="http://pythonscraping.com"

#获取资源的绝对路径，因为可能是urlretrieve需要绝对路径，然而有的路径是相对路径，并且没有加上http这个访问头
def getAbsoluteURL(baseUrl,source):
    print("这里是getAbsoluteURL函数里面"+source)
    
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("http://"):
        url=source
    elif source.startswith("www."):
        url = "http://"+source[4:]
    else:
        url =baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    
    print("这里是getDownloadPath函数里面：")
    print(baseUrl)
    print(absoluteUrl)
    print(downloadDirectory)
    
    path = absoluteUrl.replace("www.","")
    print(path)
    path = path.replace(baseUrl,"")
    print(path)
    path = downloadDirectory+path
    print(path)
    #所在脚本是以绝对路径运行的则输出绝对路径，否则输出为空
    directory = os.path.dirname(path)
    print("directory:"+directory)
    isExits = os.path.isdir(directory)
    if not isExits:
        os.makedirs(directory)
        
    return path


html = urlopen("http://www.pythonscraping.com")
bsObj= BeautifulSoup(html.read())
downloadedLis= bsObj.findAll(src=True)

print(len(downloadedLis))
print("输出采集到的所有src")
for download in downloadedLis:
    print(download["src"])

for download in downloadedLis:
    fileUrl = getAbsoluteURL(baseUrl,download["src"])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))
