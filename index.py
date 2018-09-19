from time import sleep

#open the browser and set the url
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
# browser = webdriver.Chrome()
browser = webdriver.Firefox(executable_path="D:\\geckodriver.exe")

browser.set_window_position(0, 0)
browser.set_window_size(1024, 768)
# browser.get(url)
# sleep(1)
browser.get(url)

# Select link to sign in
# link = browser.find_element_by_link_text("/accounts/login/?source=auth_switcher")
# content = browser.find_element_by_class_name('gr27e')
email = browser.find_element_by_id('f1bb7d1b9b0499c')
password = browser.find_element_by_id('f28a63e5f48f1f8')


# class="_5f5mN       jIbKX KUBKM     pm766    "
print(email)
