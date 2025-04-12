from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import random


options = UiAutomator2Options()
URL = '127.0.0.1:4723'
driver = webdriver.Remote(URL, options=options )
package_name = 'com.example.ams'



def select_box():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Box Demo').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select a fruit').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Strawberry').click()
    time.sleep(2)

    #Select 2 
    select_box = driver.find_element(AppiumBy.CLASS_NAME,'android.widget.EditText')
    select_box.click()
    select_box.send_keys("My")
    time.sleep(2)

    #click
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '🇲🇲\nMyanmar\nMM').click()

    #select 3 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select your interests').click()

    click_items = ['Flutter', 'UI/UX', 'Backend', 'Testing']

    for i in click_items:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, i).click()
        time.sleep(2)

    #Confirm
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Confirm').click()
    time.sleep(2)

    #Back
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
    time.sleep(2)
    print('Select Box Demo Success')


def radio():
    #Basic Radio Group
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Radio').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Option 3').click()

    #Advance 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Main Option B (with nested options)').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Nested Option B2').click()

    #multiple radio
    #အုပ်စု က 
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Option A2').click()
    time.sleep(2)

    #အုပ်စု ခ
    #get screen dimensions 
    window_size = driver.get_window_size()
    
    #Calculate 
    start_x = window_size['width'] // 2 
    start_y = window_size['height'] * 0.8 #80%
    end_y = window_size['height'] * 0.2   #20%

    #action
    driver.swipe(start_x, start_y, end_y, 600)

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Option B2').click()

    #Back
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
    time.sleep(2)
    print('Radio Button Success')

def checkbox():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Checkbox').click()

    #Basic 
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckBox").instance(0)').click()

    #Multiple 
    options_list = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    options_random = random.sample(options_list, k=3)
    print(options_random)
    for i in options_random:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, i).click()
        time.sleep(1)

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Enable notifications\nReceive push notifications').click()
    
    #show options
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Selected Values').click()
    time.sleep(1)
    #Ok
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()
    time.sleep(1)

     #Back
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
    print('Check Box Success')


select_box()
radio()
checkbox()
