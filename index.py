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

sleep(2)

print(ribOutBanned())

sleep(2)

print(addFriendsLoop())
# print(addFriend("EnriqueIglesias"))
# print(delayFriend("EnriqueIglesias"))
# browser.get(basic)   #this is not working
