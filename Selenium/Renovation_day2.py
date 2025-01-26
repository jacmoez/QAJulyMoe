from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRenovation:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web-staging.renonation.sg/")
        self.driver.maximize_window()
        print("Driver Success")

    def search(self):
        time.sleep(3)

        #Property type
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[1]/div[2]/div/form/div[1]/fieldset/div/div/div').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//*[text()='DBSS']").click()
        time.sleep(3)

        #Style Click
        self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section[1]/div[2]/div/form/div[2]/div[1]/fieldset/div/div/div/div").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='Asian']").click()
        time.sleep(3)

        #Other One
        self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section[1]/div[2]/div/form/div[2]/div[1]/fieldset/div/div/div/div").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='Classic']").click()
        time.sleep(3)

        #Budget
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[1]/div[2]/div/form/div[2]/div[2]/fieldset/div/div/div').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[text()="S$40,000 - S$60,000"]').click()
        time.sleep(2)

        #find
        self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section[1]/div[2]/div/form/button").click()
        time.sleep(3)


        # result = self.driver.find_element(By.XPATH, "//*[@id='allProject']/div/h6").text
        # time.sleep(5)
        #
        # #Click 1
        # self.driver.find_element(By.XPATH, '//*[@id="allProject"]/div/div[1]/div/div[1]/div[1]').click()
        # time.sleep(5)
        # print(result)
        #
        # #Project Detail
        # result = self.driver.find_element(By.XPATH, '/html/body/div/div/div[5]/div/main/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/h6').text
        # print(result)
        #
        # #Living Room
        # self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[1]').click()
        # time.sleep(4)
        #
        # #Kitchen
        # self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[2]').click()
        # time.sleep(4)
        #
        # #Dining Room
        # self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[3]').click()
        # time.sleep(4)
        #
        # #Bed Room
        # self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[4]').click()
        # time.sleep(4)
        #
        # #Bath Room
        # self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[5]').click()
        # time.sleep(4)
        #
        # #Others
        # self.driver.find_element(By.XPATH, '//*[@id="images"]/div[1]/div/div[6]').click()
        # time.sleep(5)

        # print("search success")

    def login(self):
        #xpath
        mobile_btn = '//*[@id="__next"]/div/div[3]/div/div/form[1]/div/div/div[1]/button'

        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/header/div/div[2]/div/button[2]').click()
        time.sleep(3)

        #mobile text
        self.driver.find_element(By.NAME, "mobile").send_keys("8311")
        time.sleep(3)

        self.driver.find_element(By.XPATH, mobile_btn).click()
        time.sleep(3)
        err = self.driver.find_element(By.CSS_SELECTOR, '.flex-1.text-sm.text-error').text
        print(err)
        self.driver.find_element(By.NAME, "mobile").clear()

        self.driver.find_element(By.NAME, "mobile").send_keys("83115546")
        time.sleep(3)
        self.driver.find_element(By.XPATH, mobile_btn).click()
        time.sleep(3)

        self.driver.find_element(By.NAME, 'otp').send_keys('232323')
        time.sleep(3)

        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/form[2]/div/div/button').click()


    def login_verify(self):
        time.sleep(3)

        #profile icon
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/header/div/div[2]/div/div[2]/div/div/div').click()
        time.sleep(3)

        #My Profile
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[2]/a[1]/div/div/div').click()

        #URL verify
        my_profile_url = 'https://web-staging.renonation.sg/my-profile'
        time.sleep(2)

        url = self.driver.current_url
        if my_profile_url == url : print("Login Success")
        else : print("Login Fail")

    def logout(self):
        time.sleep(3)
        #Profile icon
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/header/div/div[2]/div/div[2]/div/div/div').click()
        time.sleep(3)

        #Logout icon
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[2]/div').click()
        time.sleep(3)

        #Logout yes
        self.driver.find_element(By.XPATH, '//*[@id="radix-:r3:"]/form/div/div/button[2]').click()

    def main(self):
        self.search()
        #self.login()
        #self.login_verify()
        #self.logout()
        time.sleep(5)
        #self.driver.quit()

TestRenovation().main()