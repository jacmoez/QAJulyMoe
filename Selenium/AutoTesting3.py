from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class AutoTesting:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_browser(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
        print("Testing 1: Browser Success")

    def table_data(self):
        table = self.driver.find_element(By.ID, "taskTable")
        rows = table.find_elements(By.TAG_NAME, "tr")
        table_data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "th") if row == rows[0] else row.find_elements(By.TAG_NAME, "td")
            table_data.append([cell.text for cell in cells])
        for row in table_data:
            print("\t".join(row))
        print("=" * 55)
        time.sleep(5)

    def pagination(self):
        # p2 = ("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div["
        #       "1]/div/ul/li[2]/a")
        #
        # p3 = ("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div["
        #       "1]/div/ul/li[3]/a")
        # p4 = ("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div["
        #       "1]/div/ul/li[4]/a")
        #
        # self.driver.find_element(By.XPATH, p2).click()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, p3).click()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, p4).click()
        # time.sleep(3)

        #Pagination Click
        for i in range(1, 5):
            p = (
                f"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/ul/li[{i}]/a")

            self.driver.find_element(By.XPATH, p).click()
            time.sleep(2)
            table = self.driver.find_element(By.ID, "productTable")
            rows = table.find_elements(By.TAG_NAME, "tr")
            table_data = []
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "th") if row == rows[0] else row.find_elements(By.TAG_NAME, "td")
                table_data.append([cell.text for cell in cells])
            for row in table_data:
                print("\t ".join(row))
        print("=" * 55)
        time.sleep(5)
        for i in range(1, 5):
            p = (
                f"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/ul/li[{i}]/a")

            self.driver.find_element(By.XPATH, p).click()
            time.sleep(2)
            table = self.driver.find_element(By.ID, "productTable")
            rows = table.find_elements(By.TAG_NAME, "tr")
            table_data = []
            for row in rows:
                td = row.find_element(By.XPATH, "//td[4]")
                td.click()
                # self.driver.find_element(By.XPATH, td).click()

    def click(self):
        # self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[1]/td[4]/input")
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[1]/td[4]/input").click()
        # time.sleep(2)

        # self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[2]/td[4]/input").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[3]/td[4]/input").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[4]/td[4]/input").click()

        for i in range(1, 6):
            c = f"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[{i}]/td[4]/input"

            self.driver.find_element(By.XPATH, c).click()
            time.sleep(2)

    def tab(self):
        self.driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Myanmar", Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/div[2]/div[2]/a").click()
        time.sleep(3)
        handles = self.driver.window_handles
        time.sleep(2)
        self.driver.switch_to.window(handles[1])
        time.sleep(2)
        self.driver.switch_to.window(handles[0])
        time.sleep(3)
        self.driver.find_element(By.NAME, "start").click()
        time.sleep(5)

        self.driver.find_element(By.NAME, "stop").click()
        # time.sleep(3)

        # self.driver.find_element(By.ID, "alertBtn").click()
        time.sleep(2)

        confimation = self.driver.find_element(By.ID, "confirmBtn")
        confimation.click()
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        result = self.driver.find_element(By.ID, "demo").text
        print(result)
        confimation.click()
        time.sleep(2)

        #close alert
        alert.dismiss()
        result = self.driver.find_element(By.ID, "demo").text
        print(result)
        print(2)

        time.sleep(2)

    def main(self):
        self.open_browser()
        #self.table_data()
        #self.pagination()
        #self.click()
        self.tab()

        time.sleep(5)


AutoTesting().main()
