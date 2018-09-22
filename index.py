
#Set the url
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
basic = 'https://www.instagram.com/'
#Import Configuration and functions
from Configuration import *

#Open the browser
browser.get(url)

#Set browser position
browser.set_window_position(0, 0)
# browser.set_window_size(1000,500)

#Set browser size
browser.set_window_size(1000,700)

#Enter the credencial
input = getXpath('//input')
input[0].send_keys('Afrosinto2018')
input[1].send_keys('Qwer1234')

button = getXpath('//button[contains(text(), "Log in")]')
button[0].click()

print(ribOutBanned())

print(addFriend("EnriqueIglesias"))
browser.get(basic)
# searchInput = getXpath("//input[@placeholder='Search']")
# searchInput[0].send_keys("hola")
# searchInput[0].send_keys(Keys.ENTER)
#
# users = getXpath("//span//section//nav//div[position()=2]//div//div//div[position()=2]//div/div[position()=2]//div//a[position()=2]")
# users[0].click()
#
# button = getXpath('//button[contains(text(), "Follow")]')
# button[0].click()


# browser.get(basic)
# print(delayFriend("Enrique"))
