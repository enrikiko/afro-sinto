#open the browser and set the url

url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
from selenium import webdriver
from time import sleep
from funcion import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Firefox(executable_path="./geckodriver") #execute the file
browser = webdriver.Firefox(executable_path="D:\geckodriver") #execute by shell

browser.get(url)
browser.set_window_position(0, 0)
# browser.set_window_size(1000,500)
browser.set_window_size(1200,800)

#Define funcion

# def check_exists_by_class_name(path):
#     try:
#         browser.find_element_by_class_name(path)
#     except NoSuchElementException:
#         return False
#     return True



# def delayUntilClass(name):
#     item = False
#     count = 5
#     while item == False and count >= 0:
#         sleep(1)
#         print(count , " sec")
#         check_exists_by_class_name(name)
#         count = count - 1
#     if count <= 0:
#         print("item not found")
#     else:
#         item = browser.find_element_by_class_name(name)
#         print("Page Charged")
#         return item


# browser.get(url)
# browser.set_window_position(0, 0)
# browser.set_window_size(1024, 1768)

# # sleep(1) #Break


# q=delayUntilClass("q")

input = browser.find_elements_by_xpath('//input')
input[0].send_keys('Afrosinto2018')
input[1].send_keys('Qwer1234')

login = browser.find_element_by_xpath('//button[contains(text(), "Log in")]')
login.click()


# ----->


# #open the browser and set the url

# url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
# # from selenium import webdriver
# # from time import sleep
# from Configuration import *
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.common.exceptions import NoSuchElementException
# # # browser = webdriver.Firefox(executable_path="./geckodriver") #execute the file
# # browser = webdriver.Firefox(executable_path="/home/enrique/afro-sinto/geckodriver") #execute by shell
# #
# # #Define funcion

# browser.get(url)
# browser.set_window_position(0, 0)
# # browser.set_window_size(1000,500)
# browser.set_window_size(1200,800)

# # sleep(1) #Break



# input = getXpath('//input')
# input[0].send_keys('Afrosinto2018')
# input[1].send_keys('Qwer1234')
# button = getXpath('//button[contains(text(), "Log in")]')
# button[0].click()
# searchInput = getXpath("//input[@placeholder='Search']")
# searchInput[0].send_keys("hola")
# searchInput[0].send_keys(Keys.ENTER)
# users = getXpath("//span//section//nav//div[position()=2]//div//div//div[position()=2]//div/div[position()=2]//div//a[position()=2]")
# print(users)
# users[0].click()
# button = getXpath('//button[contains(text(), "Follow")]')
# button[0].click()
# #
# login = browser.find_element_by_xpath('//button[contains(text(), "Log in")]')
# login.click()
# #open the browser and set the url
# url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# # browser = webdriver.Firefox(executable_path="./geckodriver") #execute the file
# browser = webdriver.Firefox(executable_path="/home/enrique/afro-sinto/geckodriver") #execute by shell
# browser.get(url)
# browser.set_window_position(0, 0)
# browser.set_window_size(1024, 1768)
#
# sleep(1) #Break
#
# input = browser.find_elements_by_xpath('//input')
# input[0].send_keys('Afrosinto2018')
# input[1].send_keys('Qwer1234')
#
# login = browser.find_element_by_xpath('//button[contains(text(), "Log in")]')
# login.click()
