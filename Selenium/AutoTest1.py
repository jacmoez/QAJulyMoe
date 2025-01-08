from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class AutoTest1:

    def __init__(self):
        self.driver = webdriver.Edge()


    def open_browser(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)

    def text_input(self):
        self.driver.find_element(By.ID, "name").send_keys("QA")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='email']").send_keys("July@qa.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "phone").send_keys("966738320")
        time.sleep(2)
        self.driver.find_element(By.ID, "textarea").send_keys("Yangon, Myanmar.")
        time.sleep(2)

    def check_box(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[value='female']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "sunday").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input[value='tuesday']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='thursday']").click()


    def main(self):
        self.open_browser()
        self.text_input()
        self.check_box()
        time.sleep(5)

AutoTest1().main()