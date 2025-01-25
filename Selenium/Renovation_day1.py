from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRenovation:

    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.renonation.sg/")
        self.driver.maximize_window()
        print("Driver Success")

    def search(self):
        self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section[1]/div[2]/div/form/div[2]/div[1]/fieldset/div/div/div/div").click()
        time.sleep(3)

        #Style Click
        self.driver.find_element(By.XPATH, "//*[text()='Asian']").click()
        time.sleep(3)

        #find
        self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section[1]/div[2]/div/form/button").click()
        time.sleep(3)

        result = self.driver.find_element(By.XPATH, "//*[@id='allProject']/div/h6").text
        time.sleep(5)

        #Click 1
        self.driver.find_element(By.XPATH, '//*[@id="allProject"]/div/div[1]/div/div[1]/div[1]').click()
        time.sleep(5)
        print(result)

        #Project Detail
        result = self.driver.find_element(By.XPATH, '/html/body/div/div/div[5]/div/main/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/h6').text
        print(result)

        #Living Room
        self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[1]').click()
        time.sleep(4)

        #Kitchen
        self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[2]').click()
        time.sleep(4)

        #Dining Room
        self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[3]').click()
        time.sleep(4)

        #Bed Room
        self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[4]').click()
        time.sleep(4)

        #Bath Room
        self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[5]').click()
        time.sleep(4)

        #Others
        self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[6]').click()
        time.sleep(5)

        #Back Home Page
        self.driver.find_element(By.XPATH, '//*[@id="radix-:re:"]/div/main/div/div/div[2]/div/div/div/button[2]').click()

        print("search success")


    def main(self):
        self.search()
        time.sleep(5)
        self.driver.quit()

TestRenovation().main()