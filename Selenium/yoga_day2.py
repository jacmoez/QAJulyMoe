import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Yoga:

    driver = webdriver.Edge()
    def open_browser(self):

        self.driver.get("https://webfront-uat.yogamovement.com/")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div/div/aside/div/div[2]/button').click()
        print("Open Browser Success")


    def signin(self):
        img = "C:/Users/DELL/Pictures/flower3.jpg"

        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav[1]/ul/li[2]/a').click()
        time.sleep(3)
        self.driver.find_element(By.NAME, 'email').send_keys("aung10@yopmail.com")
        time.sleep(3)
        self.driver.find_element(By.NAME, 'password').send_keys("P@ssw0rd")
        time.sleep(3)

        self.driver.find_element(By.XPATH, '/html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button').click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, '/html/body/div/div/aside/div/div[2]/button').click()
        time.sleep(5)

        #Class
        self.driver.find_element(By.XPATH,  '//*[@id="header"]/div[2]/div/div/nav[2]/ul/li[3]/a').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav[2]/ul/li[3]/div/ul/li[2]/a').click()
        time.sleep(5)

        #All access pack
        self.driver.find_element(By.LINK_TEXT, 'ALL ACCESS').click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, '//*[@id="all-access"]/div[3]').click()
        time.sleep(3)

        #All access btn
        self.driver.find_element(By.XPATH, '//*[@id="all-access"]/div[3]/div[4]/button').click()
        time.sleep(3)

        #Order btn
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/form/button').click()
        time.sleep(3)

        #Home Studio
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/label/div/div/div/div[2]').click()
        time.sleep(3)

        #vale send

        self.driver.find_element(By.XPATH, '//*[text()="East Coast"]').click()
        time.sleep(3)

        #Image Upload
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/label/input').send_keys(img)
        time.sleep(5)

    def main(self):
        self.open_browser()
        #self.register()
        self.signin()
        time.sleep(5)

Yoga().main()