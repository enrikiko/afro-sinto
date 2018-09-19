from time import sleep

#open the browser and set the url
url = 'https://www.instagram.com/'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# browser = webdriver.Chrome()
# browser.set_window_position(0, 0)
# browser.set_window_size(1024, 768)
# browser.get(url)
# sleep(1)
browser = webdriver.Firefox(executable_path="./geckodriver")
browser.get(url)
browser.set_window_position(0, 0)
browser.set_window_size(1024, 768)
sleep(1)