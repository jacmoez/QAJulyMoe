import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class AutoTesting:

        def __init__(self):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

        def open_browser(self):
            self.driver.get("https://testautomationpractice.blogspot.com/")
            print("Testing 1: Browser Success")

        def check_box(self):
            day_checks = self.driver.find_elements(By.CLASS_NAME, "form-check-input")
            #print(len(day_checks))

            for i in range(2, len(day_checks), 2):
                day_checks[i].click()

        def select_box(self):
            time.sleep(2)
            Select(self.driver.find_element(By.ID,"country")).select_by_value("japan")
            time.sleep(2)

            colors = Select(self.driver.find_element(By.ID, "colors"))
            colors.select_by_value("red")
            colors.select_by_value("yellow")

            animals = Select(self.driver.find_element(By.ID, "animals"))
            animals.select_by_value("dog")
            time.sleep(2)
            animals.select_by_value("cat")

        def data_picker(self):
            self.driver.find_element(By.ID, "datepicker").send_keys("07/29/1997", Keys.ENTER)
            time.sleep(2)
            self.driver.find_element(By.ID, "txtDate").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[5]/table/tbody/tr[2]/td[6]/a").click()
            time.sleep(2)
            self.driver.find_element(By.ID, "start-date").send_keys("07/29/1997")
            time.sleep(2)
            self.driver.find_element(By.ID, "end-date").send_keys("01/12/2025")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[8]/button").click()
            result = self.driver.find_element(By.ID, "result").text
            print(result)
            time.sleep(2)

            #self.driver.find_element(By.CLASS_NAME, "home-link").click()

        def file_upload(self):
            img1 = "/Users/winko/Desktop/Screen Shot 2025-01-11 at 11.40.02 PM.png"
            img2 = "/Users/winko/Desktop/Screen Shot 2025-01-11 at 11.19.36 PM.png"

            single_file = self.driver.find_element(By.ID, "singleFileInput")

            self.driver.execute_script("arguments[0].scrollIntoView[true]", single_file)
            time.sleep(2)
            single_file.send_keys(img1)

            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, "#singleFileForm button").click()
            time.sleep(2)

            multiple_file = self.driver.find_element(By.ID, "multipleFilesInput")
            multiple_file.send_keys(img1, "\n", img2)
            time.sleep(2)

            self.driver.find_element(By.CSS_SELECTOR, "#multipleFilesForm button").click()

        def table_data(self):
            table = self.driver.find_element(By.NAME, "BookTable")
            rows = table.find_elements(By.TAG_NAME, "tr")
            table_data = []
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "th") if row == rows[0] else row.find_elements(By.TAG_NAME, "td")
                table_data.append([cell.text for cell in cells])
            for row in table_data:
                print("\t".join(row))

        def main(self):
            self.open_browser()
            self.check_box()
            self.select_box()
            self.data_picker()
            self.file_upload()
            self.table_data()
            time.sleep(5)


AutoTesting().main()