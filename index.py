#open the browser and set the url

url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
from selenium import webdriver
from time import sleep
# from funcion import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Firefox(executable_path="./geckodriver") #execute the file
browser = webdriver.Firefox(executable_path="/home/enrique/afro-sinto/geckodriver") #execute by shell

def checkExistsByClassName(name):
    try:
        print("checking", name)
        elem=browser.find_element_by_class_name(name)
        print(a)
    except NoSuchElementException:
        return False
    return elem



def getClass(name):
    item = False
    count = 5
    while item == False and count >= 0:
        sleep(0.2)
        print("searching", name)
        item=checkExistsByClassName(name)
        count = count - 1
    if count <= 0:
        print("class not found!")
    else:
        print("class found!")
        return item



def checkExistsByXpath(path):
    try:
        print("checking", path)
        elem=browser.find_elements_by_xpath(path)
    except NoSuchElementException:
        return False
    if len(elem) == 0:
        return False
    else:
        return elem



def getXpath(path):
    item = False
    count = 5
    while item == False and count >= 0:
        sleep(0.2)
        print("searching", path)
        item=checkExistsByXpath(path)
        # count = count - 1
    if count <= 0:
        print("xpath not found!")
    else:
        print("xpath found!")
        return item

#Define funcion

browser.get(url)
browser.set_window_position(0, 0)
browser.set_window_size(500,500)

# sleep(1) #Break



input = getXpath('//input')
print(input)
# elem = browser.find_elements_by_xpath('//input')
input[0].send_keys('Afrosinto2018')
input[1].send_keys('Qwer1234')
#
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
