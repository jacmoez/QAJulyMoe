import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Yoga:

    driver = webdriver.Edge()
    def open_browser(self):

        self.driver.get("https://webfront-uat.yogamovement.com/")
        self.driver.maximize_window()
        print("Open Browser Success")

    def register(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div/div/aside/div/div[2]/button').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav[1]/ul/li[1]/a').click()
        time.sleep(2)

        self.driver.find_element(By.NAME, 'email').send_keys("qajuly@21.com")
        time.sleep(2)

        self.driver.find_element(By.NAME, 'password').send_keys('123456')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button').click()
        time.sleep(2)

        #Mandatory
        self.driver.find_element(By.NAME, 'firstname').send_keys("July")
        time.sleep(2)

        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input').send_keys('Moe')
        time.sleep(2)

        #I Identify as *
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/div').click()
        time.sleep(2)

        #Home Country *

        self.driver.find_element(By.CLASS_NAME, 'css-egispl').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[text()="Thailand"]').click()
        time.sleep(5)

        #COUNTRY
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[1]/input').send_keys('Myanmar')
        time.sleep(2)

        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]').click()
        time.sleep(3)

        #Phone
        self.driver.find_element(By.NAME, 'mobile').send_keys("977443322")
        time.sleep(3)

        #DOB
        self.driver.find_element(By.ID, 'dob').click()
        time.sleep(5)

        Select(self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]')).select_by_value('1997')
        time.sleep(5)

        Select(self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]')).select_by_value('6')
        time.sleep(5)

        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[5]/div[3]').click()
        time.sleep(3)
        print("DOB Success")


    def main(self):
        self.open_browser()
        self.register()
        time.sleep(5)

Yoga().main()