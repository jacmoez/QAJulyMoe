from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time


options = UiAutomator2Options()
URL = 'http://127.0.0.1:4723'
driver = webdriver.Remote(URL, options=options)

def login():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Username').send_keys("standard_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Password').send_keys('secret_sauce')
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN').click()
    print("Login Success")

def logout():
    time.sleep(2)
    #loout menu
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)').click()
    time.sleep(2)

    #Logout 
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LOGOUT")').click()
    time.sleep(2)
    print("Logout Success")

def add_to_cart():
    #Sauce Labs Bike Light
    driver.find_element(AppiumBy.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[2]').click()
    time.sleep(2)

    #Test.allTheThings() T-Shirt (Red) Scroll
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("ADD TO CART").instance(1))')
    time.sleep(3)

    #Test.allTheThings() T-Shirt (Red) 
    driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])[4]').click()
    time.sleep(3)
    print('add to cart success')

def view_cart_item():
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(13)').click()
    time.sleep(2)

    #scroll checkout
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("test-CHECKOUT"))')
    
    #checkout click
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-CHECKOUT').click()
    time.sleep(3)
    print('view cart item success')

def check_out_Infomation():
    #First Name
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-First Name').send_keys('မဂျူလိူင်')

    #Last Name
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Last Name').send_keys('မိုး')

    #Zip/Postal Code
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Zip/Postal Code').send_keys('123')

    #continue 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-CONTINUE').click()
    time.sleep(2)

def check_out_overview():
    #scroll checkoutoverview
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("test-FINISH"))')
    time.sleep(2)

    item_total = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Item total: $25.98")').text
    tax = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Tax: $2.08")').text
    total = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Total: $28.06")').text
    print(item_total)
    print(tax)
    print(total)

    #Finsh
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-FINISH').click()
    time.sleep(3)

    complete = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("THANK YOU FOR YOU ORDER")').text
    print(complete)

    #Back To Home 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-BACK HOME').click()
    time.sleep(3)
    
login()
#logout()
add_to_cart()
view_cart_item()
check_out_Infomation()
check_out_overview()
logout()
