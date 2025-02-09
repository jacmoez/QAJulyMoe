*** Settings ***
Library    SeleniumLibrary

Suite Setup    Open Browser         https://www.saucedemo.com/     Edge
*** Test Cases ***
Suace Test
#     Login User
#     Check Inventory Page Arrived
#      Login Credential
      Check Credentials
#     View Details
#     View All Details
#     Search Items Choose One
#    Search Items Choose Many Times
#     Add Item To Cart Using WebElements
#     Remove Some Items From Cart
     Sleep    5


*** Keywords ***

Login User
    Maximize Browser Window
    Input Text      id:user-name        standard_user
    Input Text      id:password         secret_sauce
#    Click Button    id:login-button
    Sleep       1
    PressKeys       id:password             ENTER

Login Credential
     Maximize Browser Window
     ${credentials}=    Get Text     id:login_credentials
     Log    ${credentials}
     ${password_credential}=    Get Text     css:.login_password
     Log    ${password_credential}

Check Inventory Page Arrived
    Page Should Contain             Products
    Sleep       1

Check Credentials
     Maximize Browser Window
     @{wrong_credentials}=   Create List      locked_out_user     visual_user
     FOR     ${user}    IN     @{wrong_credentials}
       Input Text      id:user-name        ${user}
       Input Text      id:password         secret_sauce
       PressKeys       id:password             ENTER
       Sleep    4s
     END

#    standard_user
#    problem_user

#    locked_out_user
#    performance_glitch_user
#    error_user
#    visual_user


#Add Item To Cart
#    Click Button        id:add-to-cart-sauce-labs-onesie
#    Click Button        id:add-to-cart-sauce-labs-bike-light
#    Click Button        id:add-to-cart-sauce-labs-bolt-t-shirt
#    Click Button        id:add-to-cart-test.allthethings()-t-shirt-(red)
#    Sleep       3
#    Click Button        id:remove-sauce-labs-onesie
#    Sleep       5

View Details
    Click Element      xpath:/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/a/div
    Click Button      id:add-to-cart

View All Details
#    inventory_item_name
#     /html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div
#     /html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div
     FOR     ${i}    IN RANGE    1    7
        ${element_text}=    Get Text     xpath:/html/body/div/div/div/div[2]/div/div/div/div[${i}]/div[2]/div[1]/a/div
        Log    ${element_text}
        Click Element       xpath:/html/body/div/div/div/div[2]/div/div/div/div[${i}]/div[2]/div[1]/a/div
        Sleep       5

        Execute JavaScript          window.history.back();
        Sleep    3s
     END

Search Items Choose One
    Click Element     css:.product_sort_container
    Click Element     xpath:/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]
    Sleep   5
Search Items Choose Many Times
    FOR   ${i}    IN RANGE    1     5
        Click Element     css:.product_sort_container
        Click Element     xpath:/html/body/div/div/div/div[1]/div[2]/div/span/select/option[${i}]
        ${txt}=  Get Text    xpath:/html/body/div/div/div/div[1]/div[2]/div/span/select/option[${i}]
        Log    ${txt}
        Sleep    2
    END





Add Item To Cart Using WebElements
#     ${items}=  Get WebElements      css:.btn.btn_primary.btn_small.btn_inventory
#     Log    ${items}
#     ${count}=    Evaluate    len($items)
#     FOR     ${i}    IN RANGE    0      ${count}    2
#        ${txt}=    Get Text    ${items}[${i}]
#        Log    ${txt}
#        Click Button       ${items}[${i}]
#        Sleep    5s
#     END

     @{items}=  Get WebElements      css:.btn.btn_primary.btn_small.btn_inventory
     FOR     ${el}    IN   @{items}
        ${txt}=    Get Text    ${el}
        Log    ${txt}
        Click Button       ${el}
        Sleep    2s
        ${item_count}=    Get Text    css:.shopping_cart_badge
        Log     ${item_count}
     END




Remove Some Items From Cart
    Click Button     id:remove-sauce-labs-fleece-jacket
    ${item_count}=    Get Text    css:.shopping_cart_badge
    Log     ${item_count}
    Sleep       2
    Click Button     id:remove-sauce-labs-bike-light
    ${item_count}=    Get Text    css:.shopping_cart_badge
    Log     ${item_count}

View Cart
    Click Element       xpath:/html/body/div/div/div/div[1]/div[1]/div[3]/a
    Click Button        id:remove-sauce-labs-bolt-t-shirt
    Sleep       2
    Click Element       id:checkout
    Sleep       2

Checkout Information
    Input Text      id:first-name        QA
    Input Text      id:last-name         Tester
    Input Text      id:postal-code       111222
    Sleep       2
    Click Button        id:continue

Checkout Overview
    ${item_total}=  Get Text    class:summary_subtotal_label
    ${total}=    Get Text     class:summary_total_label
    Log     ${item_total}
    Log      ${total}
     ${total_price_value}=  Set Variable    0.0
     @{items}=  Get WebElements      class:inventory_item_price
     FOR    ${item_price}        IN        @{items}
         ${price}=    Get Text      ${item_price}
         ${number}=    Evaluate         float("${price}".replace('$',''))
         Log    ${price}
         Log   ${number}
         ${total_price_value}=       Evaluate     ${total_price_value}+${number}
     END
     Log        ${total_price_value}


    Click Button      id:finish
