from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Sauce:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_browser(self):
        self.driver.get("https://www.saucedemo.com/")
        print("Testing 1: Browser Success")

    def login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user", Keys.ENTER)
        time.sleep(3)

        err1 = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text

        time.sleep(2)
        #Error1 Close
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button").click()
        time.sleep(2)

        self.driver.find_element(By.ID, "password").send_keys("123", Keys.ENTER)
        time.sleep(2)
        err2 = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button").click()
        time.sleep(2)

        #password clear
        self.driver.find_element(By.ID, "password").clear()
        time.sleep(2)

        #password true
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.ENTER)
        time.sleep(2)
        #btn Click

        print(err1)
        print(err2)

    def check_page_go(self):
        url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.driver.current_url

        assert url == actual_url
        assert "Swag Labs" in self.driver.title
        print("Verify success")

    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
        time.sleep(2)

        print("Add To Cart Success")

    def remove_item(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(2)
        print("Remove Success!")

    def view_order_items(self):

        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("View Order Item")
        time.sleep(2)

    def check_cart_page_go(self):
        url = "https://www.saucedemo.com/cart.html"
        actual_url = self.driver.current_url

        assert url == actual_url
        assert "Swag Labs" in self.driver.title
        print("Check cart page success")

    def view_cart_ditail(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "remove").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        print("View Cart Ditail Success")

    def check_out(self):
        self.driver.find_element(By.ID, "checkout").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "first-name").send_keys("QA")
        time.sleep(2)
        self.driver.find_element(By.NAME, "lastName").send_keys("Testing")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("1111")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Continue']").click()
        time.sleep(2)

    def payment(self):
        total_item = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        total_tax = self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total_price = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text

        print(total_item)
        print(total_tax)
        print(total_price)

    def finish(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.cart_button").click()
        time.sleep(2)
        show = self.driver.find_element(By.TAG_NAME, "h2").text
        self.driver.find_element(By.ID, "back-to-products").click()
        time.sleep(5)
        print(show)


    def main(self):
        self.open_browser()
        self.login()
        self.check_page_go()
        self.add_to_cart()
        self.remove_item()
        self.view_order_items()
        self.check_cart_page_go()
        self.view_cart_ditail()
        self.check_out()
        self.payment()
        self.finish()
        time.sleep(5)


Sauce().main()