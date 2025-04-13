from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time



options = UiAutomator2Options()
URL = '127.0.0.1:4723'
driver = webdriver.Remote(URL, options=options )
package_name = 'com.example.ams'



def table():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Table').click()
    time.sleep(2)

    #add 
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(11)').click()
    time.sleep(1)

    #Enter name
    element =  driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')

    element.click()
    element.send_keys('Product F')
    #add click 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add').click()
    time.sleep(2)

    #edit
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()
    time.sleep(1)
    element =  driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')

    element.click() 
    element.clear()
    element.send_keys('ပန်းသီး')
    
    #update 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Update').click()
    time.sleep(2)

    #edit
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)').click()
    time.sleep(1)
    element =  driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')

    element.click() 
    element.clear()
    element.send_keys('လိမ္မော်သီး')
    
    #update 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Update').click()
    time.sleep(2)

    #delete 
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(12)').click()

    #delete
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delete').click()
    time.sleep(2)

    #back
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
    time.sleep(2)

def role_table():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Row Table').click()
    time.sleep(2)

    #ဖုန်းကို လှည့်မည်။
    # driver.orientation = 'LANDSCAPE'
    # time.sleep(2)
    # driver.orientation = 'PORTRAIT'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)').click()

    sort_list = ['Product Name', 'Price', 'Stock']
    for i in sort_list:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, i).click()
        time.sleep(2)
    
    
table()
role_table()
