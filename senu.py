import os
import time
from selenium import webdriver

url = "https://www.douban.com/"
email = "xxxxxx"
password = "xxxxxx"

driver = webdriver.Chrome()
driver.get(url)
cookie1 = driver.get_cookies()
print cookie1
time.sleep(2)
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element_by_id("form_email").send_keys(email)
driver.find_element_by_id("form_password").send_keys(password)
driver.find_element_by_xpath(
    "/html/body/div[2]/div/div[1]/form/fieldset/div[3]/input").click()
cookie2 = driver.get_cookies()
print cookie2 