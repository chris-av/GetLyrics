import re
import requests
from bs4 import BeautifulSoup
import time


# imports for selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class GetLyrcis:
        
    def initDriver():
        my_options = Options()
        my_options.add_argument('--headless')
        chrome = webdriver.Chrome('chromedriver',options=my_options)
        # chrome = webdriver.Chrome()

        return chrome
    
    def find(chrome):
        song = input('enter song title : ')
        artist = input('enter name of artist or group : ')
        print('\n\n')

        chrome.get('https://www.google.com')
        target = chrome.find_element_by_name('q')
        target.send_keys('{} {} lyrics'.format(song, artist))
        target.send_keys(Keys.RETURN)

        # trying to find that expansion bar in the search results. otherwise, lyrics are cut off / repeated
        try:
            target = chrome.find_element_by_class_name('vk_ard')
            target.click()
            target = chrome.find_element_by_class_name('hide-focus-ring pSO8Ic vk_arc')
            target.click()
        except:
            print('did not find expansion bar div, finding lyrics as is...\n')
        
        # let the htlm render for a quick sec
        time.sleep(3)
        soup = BeautifulSoup(chrome.page_source, 'html.parser')
        contents = soup.find('div', attrs={ 'class': 'NFQFxe siXlze yp1CPe mod' })
        lyrics = contents.find_all('span')

        # return beautiful soup search results
        return lyrics


    def closeDriver(chrome):
        chrome.close()



# see if what was returned is valid. 
try:
    chrome = GetLyrcis.initDriver()
    data = GetLyrcis.find(chrome)
    GetLyrcis.closeDriver(chrome)

    for lyric in data:
        print(lyric.text)
except:
    print('lyrics not found, please retry search')