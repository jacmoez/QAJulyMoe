import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class AutoTest5:

        def __init__(self):
            self.driver = webdriver.Edge()
            self.driver.get("https://testautomationpractice.blogspot.com/")
            self.driver.maximize_window()

        def download(self):
            self.driver.find_element(By.LINK_TEXT, "Download Files").click()
            time.sleep(3)
            self.driver.find_element(By.ID, "inputText").send_keys("Hello QA July Moe")
            time.sleep(3)

            #Dowload text
            self.driver.find_element(By.ID, "generateTxt").click()
            time.sleep(3)

            #Dowlolad text link
            self.driver.find_element(By.ID, "txtDownloadLink").click()
            time.sleep(3)

            #generatePdf btn
            self.driver.find_element(By.ID, "generatePdf").click()
            time.sleep(3)

            #generatePdf link
            self.driver.find_element(By.ID, "pdfDownloadLink").click()
            time.sleep(3)

            #browser pdf
            self.driver.find_element(By.XPATH, "//*[@id='post-body-7103635191948372757']/button[3]").click()
            print("Download File Success")

        def main(self):
            self.download()
            time.sleep(5)
            self.driver.quit()


AutoTest5().main()