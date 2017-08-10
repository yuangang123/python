#下面的程序用id是loadedButton的按钮检查页面是不是已经完全加载：
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path='/usr/local/phantomjs/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

#判断button有没有出现，如果出现了，则表示页面已经转到了我们所期待的页面
try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"loadedButton")))

finally:
    print(driver.find_element_by_id('content').text)
    driver.close()
