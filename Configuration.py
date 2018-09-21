from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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


# def getPlaceholder(text):
#     item = False
#     count = 5
#     while item == False and count >= 0:
#         sleep(0.2)
#         print("searching", text)
#         item=checkExistsByPlaceholder(text)
#         # count = count - 1
#     if count <= 0:
#         print("Placeholder not found!")
#     else:
#         print("Placeholder found!")
#         return item
#
# def checkExistsByPlaceholder(path):
#     try:
#         print("checking", path)
#         text = "//input[@placeholder='"+path+"']"
#         print(text)
#         elem=browser.find_elements_by_xpath(text)
#     except NoSuchElementException:
#         return False
#     if len(elem) == 0:
#         return False
#     else:
#         return elem
