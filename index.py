from time import sleep

#open the browser and set the url
url = 'https://www.instagram.com/'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# browser = webdriver.Firefox(executable_path="./geckodriver") #execute the file
browser = webdriver.Firefox(executable_path="/home/enrique/afro-sinto/geckodriver") #execute by shell
browser.get(url)
browser.set_window_position(0, 0)
browser.set_window_size(1024, 1768)
sleep(10)
email = browser.find_element_by_xpath('//a[contains(text(), "Log in")]')
email.click()

# input = browser.find_element_by_id('f1690c22585146')
# password = browser.find_element_by_id('login-password')
# input.send_keys('******@****.com')
# password.send_keys('··········')
# input.send_keys(Keys.ENTER)
# job_button = browser.find_element_by_id('jobs-tab-icon')
# job_button.click()
# sleep(1)

# email = browser.find_element_by_xpath('//a[contains(text(), "Log in")]')
# email.click()
sleep(10)
input = browser.find_elements_by_xpath('//input')
input[0].send_keys('Afrosinto2018')
input[1].send_keys('Qwer1234')

login = browser.find_element_by_xpath('//button[contains(text(), "Log in")]')
login.click()
