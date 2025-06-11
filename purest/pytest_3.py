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

 
def get_products():
    return {
        "add-to-cart-sauce-labs-backpack":"remove-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light" : "remove-sauce-labs-bike-light",
        "add-to-cart-test.allthethings()-t-shirt-(red)": "remove-test.allthethings()-t-shirt-(red)",
        "add-to-cart-sauce-labs-fleece-jacket":"remove-sauce-labs-fleece-jacket",
        "add-to-cart-sauce-labs-onesie":"remove-sauce-labs-onesie"

    }
@pytest.mark.order(2)
def test_add_to_cart():
    time.sleep(2)
    proucts = get_products()

    for add_id, remove_id in proucts.items():
        driver.find_element(By.ID, add_id).click()
        time.sleep(1)
        driver.find_element(By.ID, remove_id).click()
        time.sleep(1)

    for item_id in add_item:
        driver.find_element(By.ID, item_id).click()
        time.sleep(2)
    print("Test : Add To Cart")


@pytest.mark.order(3)
def test_view_cart():
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    products = get_products()

    for i in range(0, len(add_item), 2):
        driver.find_element(By.ID, products[add_item[i]]).click()
        print(f"Removed: {add_item[i]}")
        time.sleep(2)
    print("Test : View Cart")


@pytest.mark.order(4)
def test_checkout():
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    info_ids = ["first-name", "last-name", "postal-code"]
    info_values = ["July", "Moe", '1124002']

    for i in range(len(info_ids)):
        driver.find_element(By.ID, info_ids[i]).send_keys(info_values[i])
        time.sleep(2)
    driver.find_element(By.ID, 'continue').click()
    print('Test : Checkout')


@pytest.mark.order(5)
def test_checkout_overiew():
    total = 0
    items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    for item in items: 
        title = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
        desc = item.find_element(By.CLASS_NAME, 'inventory_item_desc').text
        price = item.find_element(By.CLASS_NAME, 'inventory_item_price').text
        total += float(price.replace("$", ""))
        print(f"Title: {title}, Description: {desc}, Price: {price}")
    summary = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    print(f"Total from UI: {summary}, Pytest Total: {total}")

