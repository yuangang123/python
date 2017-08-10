from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

#需要注意的是，这个页面的内容只运行一次，全局对象bsobj由多个测试共享
#setupClass只在类的初始化阶段运行一次，用setupclass代替setup可以省去不必要的页面加载，我们可以一次性采集全部内容，供多个测试使用
class TestWikipedia(unittest.TestCase):
    bsObj = None
    def setUpClass():
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj =BeautifulSoup(urlopen(url))
        
    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python",pageTitle)
        
    def test_contentExists(self):
        global bsObj
        content =bsObj.find("div",{'id':'mw-content-text'})
        self.assertIsNotNone(content)
        
if __name__=='__main__':
    unittest.main()
