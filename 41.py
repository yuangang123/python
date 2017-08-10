from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

drive = webdriver.PhantomJS(executable_path='/usr/local/phantomjs/bin/phantomjs')
drive.get("http://pythonscraping.com/pages/files/form.html")

firstnameField = drive.find_element_by_name("firstname")
lastnameFileld= drive.find_element_by_name("lastname")
submitButton = drive.find_element_by_id("submit")

####
#方法1
#firstnameField.send_keys("Ryan")
#lastnameFileld.send_keys("Mitchell")
#submitButton.click()
####


####
#方法2
actions  = ActionChains(drive).click(firstnameField).send_keys("Ryan").click(lastnameFileld).send_keys("Mitchell").send_keys(Keys.RETURN)
actions.perform()
########

print(drive.find_element_by_tag_name("body").text)
drive.close()
