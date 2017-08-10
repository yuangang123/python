###
#截屏，使用selenium操作
###
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

driver= webdriver.PhantomJS(executable_path="/usr/local/phantomjs/bin/phantomjs")
driver.get('http://news.mydrivers.com/1/542/542308.htm')
driver.get_screenshot_as_file("快科技.png")

print("OK")
