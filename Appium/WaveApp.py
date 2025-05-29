from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()

options.set_capability("appium:ignoreHiddenApiPolicyError", True) 

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

def categories():
     navs=driver.find_elements(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="mm.com.wavemoney.wavepay.newPreProd:id/navigation_bar_item_icon_view"])')
     for i in range(len(navs)):
        print(i)
        if i != 2:
          navs[i].click()
          time.sleep(2)
     time.sleep(2)
     navs[2].click()
     time.sleep(2)
     driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="mm.com.wavemoney.wavepay.newPreProd:id/imgClose"]').click()
     time.sleep(2)

     # click home 
     driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="mm.com.wavemoney.wavepay.newPreProd:id/navigation_bar_item_small_label_view" and @text="Home"]').click()
     time.sleep(3)
      
def ticket():
    # scroll by text
    '''driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Partners"));')
    time.sleep(3)
    # driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="mm.com.wavemoney.wavepay.newPreProd:id/imgMiniApp"])[9]').click()
                                        # (//android.widget.ImageView[@resource-id="mm.com.wavemoney.wavepay.newPreProd:id/imgMiniApp"])[9]
    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="mm.com.wavemoney.wavepay.newPreProd:id/imgMiniApp"])[10]').click()
    time.sleep(2)

    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="mm.com.wavemoney.wavepay.newPreProd:id/img_thumbnail"])[1]').click()
    time.sleep(3)'''
    #from
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="From"]').click()
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="location-filter-input"]').send_keys('Yangon')
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Yangon (ရန်ကုန်)"]').click()

    # to
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="To"]').click()
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="location-filter-input"]').send_keys('Mandalay')
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Mandalay (မန္တလေး)"]').click()
    
    # deapature date
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Departure Date"]').click()

    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,'(//android.widget.TextView[@text="2"])[2]').click()
    time.sleep(5)
    plus_icon=driver.find_element(AppiumBy.XPATH,'//android.view.View[@resource-id="app-root"]/android.view.View[4]')
    plus_icon.click()
    plus_icon.click()
    time.sleep(2)
    minus_icon=driver.find_element(AppiumBy.XPATH,'//android.view.View[@resource-id="app-root"]/android.view.View[3]')
    minus_icon.click()
    time.sleep(1)
    # local
    driver.find_element(AppiumBy.XPATH,'//android.view.View[@resource-id="app-root"]/android.view.View[5]/android.widget.Image').click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="Search Now"]').click()
    time.sleep(5)
    view =driver.find_elements(AppiumBy.XPATH,'//android.view.View')
    # for i in range(len(view)):
    #     print(i,view[i].get_attribute('content-desc'))
    view[4].click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="29"]').click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH,'(//android.widget.Button[@text="Select"])[1]').click()
    time.sleep(5)
    choose_seat()
    # i=0
    # for i in range(1,21):
    #     seat=driver.find_element(AppiumBy.XPATH,f'//android.widget.TextView[@text="{i}"]')
    #     print('Focus : ',seat.get_attribute('focusable'))
    #     time.sleep(2)
    #     if i==2: break
    #     if seat.get_attribute('focusable')=="true":
    #         seat.click()
    #         i+=1
    #         time.sleep(2)

    # driver.find_element(AppiumBy.ACCESSIBILITY_ID,'A1').click()
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID,'A2').click()
    

def choose_seat():

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                "new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollIntoView(" +
                        "new UiSelector().text(\"31\"))"
        )
    print('choose seat 1')
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="33"]').click()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="34"]').click()
    print('choose seat 2')
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="Continue"]').click()
    time.sleep(5)
    #  traveller name 
    traveller_name_el=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="input-id-name"]')
    traveller_name_el.click()
    driver.back()
    traveller_name_el.send_keys("July")
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.view.View[@resource-id="travellerForm"]/android.view.View[2]/android.view.View[2]/android.view.View[2]').click()
    time.sleep(2)
    #phone
    phone=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="input-id-phoneNumber"]')
    phone.click()
    driver.back()
    phone.clear()
    phone.send_keys("09795419303")
    time.sleep(2)

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                "new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollIntoView(" +
                        "new UiSelector().text(\"Special Request\"))"
        )
    
    #email
    email=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="input-id-email"]')
    email.click()
    # driver.back()
    email.send_keys("july@gmail.com")
    time.sleep(2)
    time.sleep(2)
    # send request
    send_request=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="input-id-specialRequest"]')
    send_request.click()
    driver.back()
    send_request.send_keys("july")
    time.sleep(2)

    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="Submit"]').click()







        


#uninstall_app()
# time.sleep(2)
#install_app()
#login()
#logout()
#categories()
#ticket()
choose_seat()
