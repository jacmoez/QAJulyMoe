from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()

#options.set_capability("appium:ignoreHiddenApiPolicyError", True) 

URL = 'http://127.0.0.1:4723'
driver = webdriver.Remote(URL, options=options)
package_name = 'mm.com.wavemoney.wavepay.newSit'

def uninstall_app():
    if driver.is_app_installed(package_name):
        driver.remove_app(package_name)
        print("unistall success")
    else:
        print("No app is install")

def install_app():
    try:
        driver.install_app("C:/Users/DELL/Desktop/Lesson/July/Appium/app-newSit-release-no-insider.apk")
        time.sleep(2)
    except Exception as e:
        print("Could not install error")
    print("App is install: ", driver.is_app_installed(package_name))
    print("--------install----------")

def login():
    #Language
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Drop Down').click()

    # #English
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(3)').click()

    #  #Language
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Drop Down').click()

    # #Chinese
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(4)').click()

    # #Language
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Drop Down').click()

    # #Myanmar
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(2)').click()
    # time.sleep(1)
    #starp
    driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.Button').click()
    time.sleep(2)

    #Cancel
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel').click()
    time.sleep(2)
    #phone
    driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText').send_keys('795419303')
    time.sleep(2)

    #CheckBox
    driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.CheckBox').click()
    time.sleep(2)
    driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.Button').click()
    time.sleep(2)

    #Click box 
    driver.find_element(AppiumBy.ID, 'mm.com.wavemoney.wavepay.newSit:id/btn_confirm').click()
    time.sleep(20)

    #OTP Skip

    #ping code
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").instance(4)').send_keys('2')
    time.sleep(1)

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").instance(5)').send_keys('5')
    time.sleep(1)

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").instance(6)').send_keys('2')
    time.sleep(1)

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").instance(7)').send_keys('5')
    time.sleep(2)


    #skip
    driver.find_element(AppiumBy.ID, 'mm.com.wavemoney.wavepay.newSit:id/btnSkipForNow').click()
    time.sleep(5)

def logout():
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("mm.com.wavemoney.wavepay.newSit:id/navigation_bar_item_icon_view").instance(4)').click()
    time.sleep(2)

    #logout click
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(ture).scrollIntoView(new UiSector().text("ထွက်မည်?"))').click()
    time.sleep(2)

#uninstall_app()
# time.sleep(2)
#install_app()
#login()
logout()
