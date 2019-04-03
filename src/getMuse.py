import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
from pathlib import Path


# Create userpass.csv and add whatever username and password you want
# All CSV files are ignored by git

# options = webdriver.ChromeOptions()
# prefs = {'download.default_directory': '/assets'}
# options.add_experimental_option('prefs', prefs)
# browser = webdriver.Chrome(chrome_options=options)
class getMuse:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get(('https://musedirect.choosemuse.com/login?redirect=/'))

        self.moveNew()
        self.login()
        self.download()
        self.moveDownload()

    def moveNew(self):
        print("start")
        subprocess.call("~/Code/SciFair/src/bash/moveNew.sh", shell=True)
        print("end")


    def login(self):
        data = pd.read_csv("assets/userpass.csv")

        username = data['Username'][0]
        password = data['Password'][0]

        # find_element_by_tag_name
        # browser.find_element_by_tag_name('input')[0].send_keys(username)
        # browser.find_element_by_tag_name('input')[1].send_keys(password)
        time.sleep(5)
        
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys(username)

        self.browser.find_element_by_name('email').send_keys(username)
        self.browser.find_element_by_name('password').send_keys(password)
        self.browser.find_element_by_class_name('auth0-lock-submit').click()
        time.sleep(5)

    def download(self):
        # browser.find_elements_by_tag_name('input')[1].click()
        # browser.find_elements_by_tag_name('input')[2].click()

        # TODO: make elements only from the right time
        self.browser.find_elements_by_tag_name('input')[1].click()

        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[1]/button/div/div/span').click()
        time.sleep(1)
        self.browser.find_elements_by_tag_name('input')[-4].click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[6]/button').click()
        time.sleep(3)

    def moveDownload(self):
        # my_file = Path("~/Downloads/Muse*")
        
        # while(not my_file.exists()):
        #     print(my_file.exists())
        #     time.sleep(1)
        time.sleep(5)
        print("start")
        subprocess.call("/home/berk/Code/SciFair/src/bash/moveDownload.sh", shell=False)
        print("end")
