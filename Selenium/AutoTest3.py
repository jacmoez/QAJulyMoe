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

    def tab(self):



        #self.driver.find_element(By.ID, "PopUp").click()

        point = self.driver.find_element(By.CLASS_NAME, 'dropbtn')

        time.sleep(3)
        point.click()
        self.driver.find_element(By.LINK_TEXT, "Mobiles").click()

        time.sleep(5)
        point.click()
        self.driver.find_element(By.LINK_TEXT, "Laptops").click()
        time.sleep(5)

        #Double Click
        filed1 = self.driver.find_element(By.ID, "field1")
        filed2 = self.driver.find_element(By.ID, "field2")
        filed1.clear()
        time.sleep(5)
        filed1.send_keys("July Moe")
        time.sleep(5)
        copy_text =self.driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[7]/div[1]/button")

        ActionChains(self.driver).double_click(copy_text).perform()
        d = filed2.get_attribute("value")
        print("Filed 2: " , filed2.get_attribute("value"))
        time.sleep(5)

        #drop and drop
        first = self.driver.find_element(By.ID, "draggable")
        second = self.driver.find_element(By.ID, "droppable")

        self.driver.execute_script("arguments[0].scrollIntoView(true)", first)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", second)
        time.sleep(2)

        #drag and drop
        ActionChains(self.driver).drag_and_drop(first, second).perform()
        time.sleep(5)

        #Slider
        slider = self.driver.find_element(By.XPATH, "//*[@id='slider-range']")
        handle1 = self.driver.find_element(By.XPATH, self.slider1)
        handle2 = self.driver.find_element(By.XPATH, self.slider2)
        slider_width = slider.size["width"]

        offset1 = int(slider_width * (100-10) / 100)
        ActionChains(self.driver).drag_and_drop_by_offset(handle1, offset1, 0).perform()
        time.sleep(3)


        offset2 = int(slider_width * (100-20) / 100)
        ActionChains(self.driver).drag_and_drop_by_offset(handle2, offset2, 100).perform()
        time.sleep(3)

        self.driver.find_element(By.ID, "comboBox").send_keys("Item 10")


        time.sleep(3)
        self.driver.find_element(By.ID, 'apple').click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.ID, "lenovo").click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.ID, "dell").click()

        print("Test 2 : Tab Success")



    def main(self):
        self.tab()

AutoTest().main()