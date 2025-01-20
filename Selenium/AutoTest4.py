import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class AutoTest:

    slider1 = "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[9]/div[1]/div/span[1]"

    slider2 = "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[9]/div[1]/div/span[2]"

    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        time.sleep(3)
        print("Test 1 : Driver Success")


    def tab2(self):

        for i in range(1,9):
            block_link = f"//*[@id='broken-links']/a[{i}]"
            self.driver.find_element(By.XPATH, block_link).click()
            title = self.driver.title
            time.sleep(3)
            print(title)
            self.driver.back()
    print("Block Link Success!")
    time.sleep(5)

    def form(self):
        # self.driver.find_element(By.ID, "input1").send_keys("QA July Moe")
        # self.driver.find_element(By.ID, "btn1").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.ID, "input2").send_keys("QA Hnin Hnin")
        # self.driver.find_element(By.ID, "btn2").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.ID, "input3").send_keys("QA May May")
        # self.driver.find_element(By.ID, "btn3").click()

        for i in range(0, 3):
            elements = f"input{i+1}"
            btn = f"btn{i+1}"
            name = ["မောင်မောင်", "အောင်အောင်", "မြမြ"]
            self.driver.find_element(By.ID, elements).send_keys(name[i])
            time.sleep(3)
            self.driver.find_element(By.ID, btn).click()

        self.driver.find_element(By.LINK_TEXT, "Hidden Elements & AJAX").click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'toggleInput').click()
        result = self.driver.find_element(By.ID, "statusLabel").text
        print(result)

        self.driver.find_element(By.ID, "toggleCheckbox").click()
        result = self.driver.find_element(By.ID, "statusLabel").text
        print(result)

        self.driver.find_element(By.ID, "loadContent").click()
        time.sleep(5)
        result = self.driver.find_element(By.ID, "ajaxContent").text
        print(result)


    def main(self):
        #self.tab2()
        self.form()
        time.sleep(5)

AutoTest().main()