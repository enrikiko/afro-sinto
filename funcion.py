from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Firefox(executable_path="/home/enrique/afro-sinto/geckodriver") #execute by shell

def checkExistsByClassName(name):
    try:
        print("searching2", name)
        browser.find_element_by_class_name(name)
    except NoSuchElementException:
        return False
    return True


def getClass(name):
    item = False
    count = 5
    while item == False and count >= 0:
        sleep(1)
        print(count , " sec")
        print("searching", name)
        checkExistsByClassName(name)
        count = count - 1
    if count <= 0:
        print("class not found!")
    else:
        item = browser.find_element_by_class_name(name)
        print("class found!")
        return item

def checkExistsByXpath(path):
    try:
        browser.find_element_by_xpath(path)
    except NoSuchElementException:
        return False
    return True


def getXpath(path):
    item = False
    count = 5
    while item == False and count >= 0:
        sleep(1)
        print(count , " sec")
        checkExistsByXpath(path)
        count = count - 1
    if count <= 0:
        print("xpath not found!")
    else:
        item = browser.find_element_by_xpath(path)
        print("xpath found!")
        return item
