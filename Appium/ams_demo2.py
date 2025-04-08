from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time


options = UiAutomator2Options()
URL = '127.0.0.1:4723'
driver = webdriver.Remote(URL, options=options )
package_name = 'com.example.ams'



def time_select():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Date & Time').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Time').click()

    # click keyboard icon
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)').click()

    #two edit hour and minute 
    els = driver.find_elements(AppiumBy.XPATH, '//android.widget.EditText')

    #hour
    el = els[0]
    el.click()
    el.clear()
    el.send_keys('10')

    #minute
    el = els[1]
    el.click()
    el.clear()
    el.send_keys('10')

    #AM 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'AM').click()
    time.sleep(3)
    #OK
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()
    time.sleep(2)
    #Back
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
    print('Time Select Success')

def select_box():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Box Demo').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select a fruit').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Strawberry').click()
    time.sleep(2)


time_select()
select_box()
