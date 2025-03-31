from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
URL = '127.0.0.1:4723'
driver = webdriver.Remote(URL, options=options )
package_name = 'com.example.ams'

#install app
def install_app():
    print("--------------befor install------------")
    driver.install_app("C:/Users/DELL/Desktop/Lesson/July/app-release.apk")
    time.sleep(5)
    print('-----------------Afer Install------------')

#uninstall 
def uninstall_app():
    time.sleep(2)
    print("----------berfore uninstall-----------")
    if driver.is_app_installed(package_name):
        driver.remove_app(package_name)
        print('-------- After Uninstall -----------')

def launch_app():
    time.sleep(2)
    driver.activate_app(package_name)
    time.sleep(5)
    print('Launch Success')

def message():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Messages').click()

    #Delete icon
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)').click()
    time.sleep(2)

    #Delete
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delete').click()
    time.sleep(3)

    #Back
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
    print('Message Click Success')


def login_btn():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Login').click()

    #Login btn
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Login"]').click()
    print("Login Click Success")
    view_element = driver.find_elements(AppiumBy.XPATH, '//android.view.View')
    print('Name Error: ', view_element[6].get_attribute('content-desc'))
    print('Password Error: ', view_element[7].get_attribute('content-desc') )

    user_name =  'new UiSelector().className("android.widget.EditText").instance(0)'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, user_name).click()
    time.sleep(2)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, user_name).send_keys('July')

    password = 'new UiSelector().className("android.widget.EditText").instance(1)'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, password).click()
    time.sleep(2)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, password).send_keys('123456')


install_app()
uninstall_app()
launch_app()
message()
login_btn()

