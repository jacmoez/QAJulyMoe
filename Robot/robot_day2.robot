*** Settings ***
Library    SeleniumLibrary

Suite Setup    Open Browser         https://www.saucedemo.com/     Edge

*** Test Cases ***
Login User
    Maximize Browser Window
    Input Text      id:user-name        standard_user
    Input Text      id:password         secret_sauce
#    Click Button    id:login-button
    Sleep       1
    PressKeys       id:password             ENTER

Check Inventory Page Arrived
    Page Should Contain             Products
    Sleep       1

#Add Item To Cart
#    Click Button        id:add-to-cart-sauce-labs-onesie
#    Click Button        id:add-to-cart-sauce-labs-bike-light
#    Click Button        id:add-to-cart-sauce-labs-bolt-t-shirt
#    Click Button        id:add-to-cart-test.allthethings()-t-shirt-(red)
#    Sleep       3
#    Click Button        id:remove-sauce-labs-onesie
#    Sleep       5

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
     END


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
