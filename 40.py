class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None
    
    def test_PageProperties(self):
        global bsObj
        global url
        
        url="http://ee.wikipedia.org/wiki/Monty_Python"
        #测试遇到的前100个页面
        for i in range(1,100):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchsURL()
            self.assertEuquals(titles[0],titles[1])
            self.asserTrue(self.contentExists())
            url = self.getNextLink()
        print("Done!")
        
        
    def titleMatchsURL(self):
        global bsObj
        global url
        pageTitle - bsObj.find("h1").get_text()
        urlTitle = url(url.index("/wiki/"+6):)
        urlTitle = urlTitle.replace("_"," ")
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(),urlTitle.lower()]
    
    def contentExists(self):
        global bsObj
        content = bsObj.find("div",{"id":"mw-content_text"})
        if content is not None:
            return True
        return False
    
    def getNextLink(self):
        #使用第5章介绍的方法返回随机链接
if __name__ =='__main__':
    unittest.main()
