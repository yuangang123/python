#维基百科六度分割篇：终结篇
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql


#连接数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password=None,db='mysql',charset='utf8')
#设置游标，处理对数据库的输入和输出
cur = conn.cursor()

cur.execute("use wikipedia")

#class SolutionFound继承RuntimeError
class SolutionFound(RuntimeError):
    def __init__(self,message):
        self.message= message
    
def contructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links,[{}]*len(links)))
    return {}
    
def searchDepth(targetPageId,currentPageId,linkTree,depth):
    if depth==0:
        return linkTree
    if not linkTree:
        linkTree = contructDict(currentPageId)
        if not linkTree:
            return {}
    if targetPageId in linkTree.keys:
        print("TARGET"+str(targetPageId)+" FOUND!")
        raise SolutionFound("PAGE: "+str(currentPageId))
        
    for branchKey,branchValue in linkTree.items():
        try:
            linkTree[branchKey] = searchDepth(targetPageId,branchKey,branchValue,depth-1)
            except SolutionFound as e:
                print(e.message)
                raise SolutionFound("PAGE: "+str(currentPageId))
    return linkTree
    
try:
    searchDepth(134951,1,{},4)
    print("No solution fonud")
except SolutionFound as e:
    print(e.message)
