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

 
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)').click()

    sort_list = ['Product Name', 'Price', 'Stock']
    for i in sort_list:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, i).click()
        time.sleep(2)


    element = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.HorizontalScrollView')

    #အလျားလိုက်ဆွဲခြင်း
    driver.execute_script('mobile:swipeGesture ', {
    'elementId': element,
    'direction': 'left', 
    'percent': 0.75
} )
    time.sleep(2)

    #edit
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)').click()

    #price 
    element = driver.find_elements(AppiumBy.XPATH, '//android.view.View')
    print("edit value: ", element[10].get_attribute('content-desc'))
    time.sleep(2)

    #delete
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)').click()
    time.sleep(2)

    #Back
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
    time.sleep(2)

def slider():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Slider & Switch ').click()

    #bar 1 
    seekbars = driver.find_elements(AppiumBy.XPATH, '//android.widget.SeekBar')
    seekbar1 = seekbars[0]
    horintal_slider(seekbar1, 0.8)
    time.sleep(2)

    #bar 2 
    seekbar2 = seekbars[1]
    horintal_slider(seekbar2, -0.8)
    time.sleep(2)

    seekbar3 = seekbars[2]
    horintal_slider(seekbar3, -0.9)

    #bar 3
    seekbar4 = seekbars[3]
    horintal_slider(seekbar4, 0.85)

    #bar4
    seekbar5 = seekbars[4]
    horintal_slider(seekbar5, 0.75)

def horintal_slider(slider,value):
    #Get location and size
    location = slider.location
    size = slider.size
    start_x = location['x']
    start_y = location['y'] + size['height'] // 2 
    end_x = start_x + int(size['width'] * value)

 
    driver.execute_script('mobile: dragGesture ', {
    'elementId': slider,
    'endX': end_x, 
    'endY': start_y
} )



#table()
#role_table()
slider()
