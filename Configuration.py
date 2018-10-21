from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Firefox(executable_path="/home/enrique/afro-sinto/geckodriver") #execute by shell
suggested = 'https://www.instagram.com/explore/people/suggested/'
explore = 'https://www.instagram.com/explore/'
following = 'https://www.instagram.com/afrosinto2018/following/'



#</Joker functions>
def checkExistsByXpath(path):
    try:
        elem=browser.find_elements_by_xpath(path)
    except NoSuchElementException:
        print(path, "not found!")
        return False
    if len(elem) == 0:
        print(path, "not found!")
        return False
    else:
        return elem

def getXpath(path, count=100):
    item = False
    while item == False and count >= 0:
        sleep(0.2)
        item = checkExistsByXpath(path)
        count = count - 1
    if count <= 0:
        print("xpath not found!")
    else:
        print("xpath found!")
        return item

def clickElement(element):
    try:
        element.click()
    except NoSuchElementException:
        print(str(element) + "element not found!")

def deleteUnfollowBanner():
    try:
        certain = getXpath('//button[contains(text(), "Cancel")]', 3)
        if certain == True:
            try:
                cancel = getXpath('//button[contains(text(), "Cancel")]', 3)
                clickElement(cancel[0])
                print("Banner deleted!")
            except NoSuchElementException:
                print("Banner not found!")
    except NoSuchElementException:
        print("Banner not found!")
#</Joker functions>


# def checkExistsByClassName(name):
#     try:
#         print("checking", name)
#         elem=browser.find_element_by_class_name(name)
#         # print(a)
#     except NoSuchElementException:
#         return False
#     return elem
#
#
#
# def getClass(name):
#     item = False
#     count = 5
#     while item == False and count >= 0:
#         sleep(0.2)
#         print("searching", name)
#         item=checkExistsByClassName(name)
#         count = count - 1
#     if count <= 0:
#         print("class not found!")
#     else:
#         print("class found!")
#         return item


def ribOutBanned():
    item = False
    count = 100
    while item == False and count >= 0:
        sleep(0.2)
        item = checkExistsByXpath('//button[@class="chBAG"]')
        count = count - 1
    if count <= 0:
        print("Banned not found!")
    else:
        item[0].click()
        return("Banned 1 delated!")

def turnOnSound():
    item = False
    count = 100
    while item == False and count >= 0:
        sleep(0.2)
        item=checkExistsByXpath("//button[text()='Turn On']")
        count = count - 1
    if count <= 0:
        print("Banned not found!")
    else:
        item[0].click()
        return("Banned 2 delated!")


def addFriend(name):
    try:
        searchInput = getXpath("//input[@placeholder='Search']", 1000)
    except NoSuchElementException:
        return "Add Friend FAILS!  ERROR-001"
    try:
        searchInput[0].send_keys(name)
        searchInput[0].send_keys(Keys.ENTER)
    except NoSuchElementException:
        return "Add Friend FAILS!  ERROR-002"
    try:
        users = getXpath("//span//section//nav//div[position()=2]//div//div//div[position()=2]//div/div[position()=2]//div//a[position()=1]", 1000)
        users[0].click()
    except NoSuchElementException:
        return "Add Friend FAILS!  ERROR-003"
    try:
        button = getXpath('//button[contains(text(), "Follow")]', 1000)
        button[0].click()
    except NoSuchElementException:
        return "Add Friend FAILS!  ERROR-004"
    return "Friend Added!"


def delayFriend(name):
    try:
        print('1')
        searchInput = getXpath("//input[@placeholder='Search']", 1000)
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

def addFriendsLoop():
    browser.get(suggested)
    count = 0
    lenght = 0
    while True:
        followList = getXpath('//button[contains(text(), "Follow")]')
        maxLenght = len(followList)
        # minLenght = maxLenght - minLenght
        while lenght < maxLenght:
            print("Click on " + str(lenght))
            clickElement(followList[lenght])
            lenght = lenght + 1
            browser.execute_script("window.scrollTo(0, " + str(lenght * 82) + ");")
            sleep(7)
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight - 100);")
        # sleep(5)




def addFriendsLoopExplore():
    browser.get(explore)
    sleep(1)
    div = getXpath('//article//div//div//div/div')
    clickElement(div[0])
    clickElement(div[0])
    sleep(2)
    counting = 0
    while True:
        counting += 1
        deleteUnfollowBanner()
        follow = getXpath('//article//header//div//div//div//button[contains(text(), "Follow")]')
        follow[0].click()
        sleep(randint(5,10))
        sig = getXpath('//a[contains(text(),"Next")]')
        clickElement(sig[0])
        print(counting + " users aAdded")
        sleep(randint(5,10))

def deleteFriends():
    browser.get(following)
    sleep(1)
    # button = getXpath('//a[contains(text(), "following")]')
    button = getXpath('//a[@href="/afrosinto2018/following/"]')
    clickElement(button[0])
    sleep(1)
    count = 0
    while True:
        button = getXpath('//ul//div//li//div/div//button[contains(text(), "Following")]')
        clickElement(button[count])
        unfollow = getXpath('//button[contains(text(), "Unfollow")]')
        clickElement(unfollow[0])
        count = count + 1
        sleep(0.2)













































#
