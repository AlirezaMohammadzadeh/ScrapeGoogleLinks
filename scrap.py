from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import requests
import json
import time
import pandas as pd



class WebScraper:
    def __init__(self, driver_path, options=None):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        self.driver_path = driver_path
        self.options = options 
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome(executable_path = self.driver_path)

    def stop_driver(self):
        if self.driver:
            self.driver.quit()

    def scrape_data(self,url,counter=0):
        if not self.driver:
            raise Exception("Driver not started. Call start_driver() before scraping data.")
        try:
            data = self.driver.get(url)
            return data
        except Exception as e:
            print(f'An error occured while trying get data by chrome driver : {str(e)}')
            return 0

    def scrape_by_Xpath(self, xpath):
        data = self.driver.find_element(by = By.XPATH,value = xpath).text
        if data == None:
            raise Exception("Could scrape data by xpath")
        else:
            return data

    def scrape_by_class_name(self,class_name):
        data = self.driver.find_element_by_class_name(class_name)
        if data == None:
            raise Exception("Could scrape data by class name")
        else:
            return data 
    
    def click_by_Xpath(self, xpath):
        try:
            self.driver.find_element(by = By.XPATH,value = xpath).click()
        except Exception as e:
            pass

    def click_by_class_name(self,class_name):
        try:
            self.driver.find_element_by_class_name(class_name).click()
        except Exception as e:
            pass

    def scrape_by_tag_name(self,tag_name):
        try:
            data = self.driver.find_elements(By.TAG_NAME, tag_name)
            return data
        except Exception as e:
            pass