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

    #bar 5 
    seekbar6 = seekbars[5]
    vertical_slider(seekbar6, 0.2)

    #scroll 
    window_size = driver.get_window_size()

    start_x = window_size['width'] // 2 
    start_y = window_size['height'] * 0.5
    end_y = window_size['height'] * 0.2 

    driver.swipe(start_x, start_y, start_x, end_y, 800)
    time.sleep(1)

    # slider = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, '50%')[2] 
    slider=driver.find_elements(AppiumBy.XPATH,'(//android.widget.SeekBar[@content-desc="50%"])')
    
    horintal_slider(slider[0], 0.8)
  
  
def registration():
     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Registration Form').click()

     full_name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')

     full_name.click()
     full_name.send_keys('July Moe')

     email = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')

     email.click()
     email.send_keys('julymoe@qa.com')

     phone = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)')

     phone.click()
     phone.send_keys('09795419304')

     address = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(3)')

     address.click()
     address.send_keys('Dawbon, Yangon, Myanmar.')

    #Female
     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.RadioButton").instance(1)').click()

     #Hobbies
     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Reading').click()
     
     #scroll 
     window_size = driver.get_window_size()

     start_x = window_size['width'] // 2 
     start_y = window_size['height'] * 0.6
     end_y = window_size['height'] * 0.2 

     driver.swipe(start_x, start_y, start_x, end_y, 800)
     time.sleep(2)

     #DOB
     driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[5]/android.widget.Button').click()
     
     time.sleep(1)

    #Edit icon
     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)').click()

     #Edit Text
     edit_text = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')
     edit_text.click()
     edit_text.clear()
     edit_text.send_keys("07/29/1997")
     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()

     seekbar = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.SeekBar')
     horintal_slider(seekbar, 0.8)

     driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.Button[7]').click()
     time.sleep(1)
     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Single').click()

     #Register
     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Register').click()

     info = driver.find_elements(AppiumBy.XPATH, '//android.view.View') 
    #  for e in info:
    #       print(e.get_attribute('content-desc'))
     print(info[6].get_attribute('content-desc'))

     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()

     #Back
     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()

     
     

    



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
    
def vertical_slider(slider,value):
    #Get location and size
        location = slider.location
        size = slider.size
        center_x = location['x'] + size['width'] // 2 
        end_y = location['y'] + int(size['height'] * value)
        driver.execute_script('mobile: dragGesture ', {
        'elementId': slider,
        'endX': center_x, 
        'endY': end_y
    } )



table()
role_table()
slider()
registration()
