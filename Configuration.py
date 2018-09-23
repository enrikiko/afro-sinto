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

def ribOutBanned():
    item = False
    count = 100
    while item == False and count >= 0:
        sleep(0.2)
        item=checkExistsByXpath('//body//div[position()=2]//div//button')
        count = count - 1
    if count <= 0:
        print("Banned not found!")
    else:
        item[0].click()
        return("Banned delated!")


def addFriend(name):
    try:
        searchInput = getXpath("//input[@placeholder='Search']")
    except NoSuchElementException:
        return "Add Friend FAILS!  ERROR-001"
    try:
        searchInput[0].send_keys(name)
        searchInput[0].send_keys(Keys.ENTER)
    except NoSuchElementException:
        return "Add Friend FAILS!  ERROR-002"
    try:
        users = getXpath("//span//section//nav//div[position()=2]//div//div//div[position()=2]//div/div[position()=2]//div//a[position()=1]")
        users[0].click()
    except NoSuchElementException:
        return "Add Friend FAILS!  ERROR-003"
    try:
        button = getXpath('//button[contains(text(), "Follow")]')
        button[0].click()
    except NoSuchElementException:
        return "Add Friend FAILS!  ERROR-004"
    return "Friend Added!"


def delayFriend(name):
    try:
        print('1')
        searchInput = getXpath("//input[@placeholder='Search']")
    except NoSuchElementException:
        return "Delay Friend FAILS!  ERROR-001"
    try:
        print('2')
        searchInput[0].send_keys(name)
        searchInput[0].send_keys(Keys.ENTER)
    except NoSuchElementException:
        return "Delay Friend FAILS!  ERROR-002"
    try:
        print('3')
        users = getXpath("//span//section//nav//div[position()=2]//div//div//div[position()=2]//div/div[position()=2]//div//a[position()=1]")
        users[0].click()
    except NoSuchElementException:
        return "Delay Friend FAILS!  ERROR-003"
    try:
        print('4')
        button = getXpath('//button[contains(text(), "Following")]')
        button[0].click()
    except NoSuchElementException:
        return "Delay Friend FAILS!  ERROR-004"
    try:
        print('5')
        button = getXpath('//button[contains(text(), "Unfollow")]')
        button[0].click()
    except NoSuchElementException:
        return "Delay Friend FAILS!  ERROR-005"
    return "Friend Delayed!"


def getSuggestedPage():
    try:
        button = getXpath("//a[contains(@href,'/explore/')]")
        button[0].click()
        return True
    except NoSuchElementException:
        return False

def addFriendsLoop():
    certainly = False
    isSuggested = False
    while  certainly == False and isSuggested == False:
        certainly = getSuggestedPage()
        isSuggested = checkIsSuggested()
    return "ok!"

def chechIsSuggested():
    verify = False
    verify = getXpath()































#
