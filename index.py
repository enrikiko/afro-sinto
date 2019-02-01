def download_pdf(lnk):

    from selenium import webdriver
    from time import sleep

    options = webdriver.ChromeOptions()

    download_folder = "D:\\"    

    profile = {"plugins.plugins_list": [{"enabled": False,
                                         "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_folder,
               "download.extensions_to_open": ""}

    options.add_experimental_option("prefs", profile)

    print("Downloading file from link: {}".format(lnk))

    # driver = webdriver.Chrome(executable_path="D:\geckodriver") #execute by shell
    driver = webdriver.Firefox(executable_path='D:\geckodriver')
    driver = webdriver.Chrome(chrome_options = options)
    driver.get(lnk)

    filename = lnk.split("/")[4].split(".cfm")[0]
    print("File: {}".format(filename))

    print("Status: Download Complete.")
    print("Folder: {}".format(download_folder))

    driver.close()

download_pdf("http://www.poderjudicial.es/search/contenidos.action?action=contentpdf&databasematch=TS&reference=8549179&links=&optimize=20181026&publicinterface=true")


# from Configuration import *

# download_dir = "D:\proyectos-github" 
# options = webdriver.ChromeOptions()

# profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
#                "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
# options.add_experimental_option("prefs", profile)
# # driver = webdriver.firefox('D:\geckodriver.exe', firefox_options=options)  # Optional argument, if not specified will search path.

# browser.get('http://www.poderjudicial.es/search/contenidos.action?action=contentpdf&databasematch=TS&reference=8549179&links=&optimize=20181026&publicinterface=true')
########################
# #Set the url
# url = 'http://www.poderjudicial.es/search/contenidos.action?action=contentpdf&databasematch=TS&reference=8549179&links=&optimize=20181026&publicinterface=true'
#Import Configuration and functions
# from Configuration import *

# #Open the browser
# browser.get(url)

# #Set browser position
# browser.set_window_position(0, 0)
# # browser.set_window_size(1000,500)

# #Set browser size
# browser.set_window_size(1200,800)


# #Enter the credencial
# input = getXpath('//input')
# input[0].send_keys('Afrosinto2018')
# input[1].send_keys('Qwer1234')

# button = getXpath('//button[contains(text(), "Log in")]')
# button[0].click()

# searchInput = getXpath("//input[@placeholder='Search']")
# searchInput[0].send_keys("hola")
# searchInput[0].send_keys(Keys.ENTER)

# users = getXpath("//span//section//nav//div[position()=2]//div//div//div[position()=2]//div/div[position()=2]//div//a[position()=2]")
# users[0].click()

# button = getXpath('//button[contains(text(), "Follow")]')
# button[0].click()
# #
