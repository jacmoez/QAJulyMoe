from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


url = "https://www.saucedemo.com/"

driver = None

add_item = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-test.allthethings()-t-shirt-(red)"
]



@pytest.fixture(scope='module',autouse=True)
def setup():
    global driver 
    driver = webdriver.Edge()
    driver.get(url)
    driver.maximize_window()
    yield
    driver.quit()



def login(user, username, password):
    try:
        driver.refresh()
        user_name = driver.find_element(By.ID, "user-name")
        user_name.clear()
        user_name.send_keys(username)
        time.sleep(1)
        user_password = driver.find_element(By.ID, 'password')
        user_password.clear()
        user_password.send_keys(password)

        time.sleep(1)

        print(f"{user} login")
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(1)
        try:
            error = driver.find_element(By.TAG_NAME, 'h3').text
            print(f"Login Error Message :  {error}")
        except:
            raise Exception('No Error')
        
    except Exception as e:
        print(f"{str(e)} : {user}")

@pytest.mark.order(1)
def test_login_user():
    users = {
        # "User1": ["", ""],
        # "User2": ["User2", ],
        "User3": ["standard_user", "secret_sauce"]
    }

    for key, val in users.items():
        login(key, val[0], val[1])
    print("Test : Login Test")
    print("="*33)

 
@pytest.mark.order(2)
def test_add_to_cart():
    time.sleep(2)

    for add_id in add_item:
        driver.find_element(By.ID, add_id).click()
        time.sleep(2)

