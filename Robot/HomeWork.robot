*** Settings ***
Library     SeleniumLibrary

Suite Setup     Open Browser        https://www.saucedemo.com/      Edge


*** Test Cases ***

Login

        Maximize Browser Window
        Input Text      id:user-name        standard_user
        Sleep           1
        Input Text      id:password         secret_sauce
        Sleep           1
        Click Button    id:login-button
        Sleep       2      1


Add to Cart

                  ${items}=  Get WebElements      css:.btn.btn_primary.btn_small.btn_inventory
                  ${price}=  Get Text             class:inventory_item_price

                  Log    ${items}
                  Log    ${price}

                  ${count}=    Evaluate    len($items)
                  FOR     ${i}    IN RANGE    0      ${count}    2
                     ${txt}=    Get Text    ${items}[${i}]
                     Log    ${txt}
                     Log    ${price}
                     Click Button       ${items}[${i}]
                     Sleep    5s
                  END
View Cart

        Click Element       xpath:/html/body/div/div/div/div[1]/div[1]/div[3]/a
        Sleep               1
        Click Button        id:checkout
        Sleep               2

Checkout Information

        Input Text          id:first-name       July
        Sleep               1
        Input Text          id:last-name        Moe
        Sleep               1
        Input Text          id:postal-code      111111
        Sleep               1
        Click Button        id:continue
        Sleep               2

Checkout Overview

        ${item_total}=      Get Text        class:summary_subtotal_label
        ${total}=           Get Text        class:summary_total_label
        Log                 ${item_total}
        Log                 ${total}
        ${total_price_value}=       Set Variable        0.0
        ${items}=           Get WebElements     class:inventory_item_price
        FOR     ${item_price}       IN          @{items}
                ${price}=       Get Text        ${item_price}
                ${number}=      Evaluate        float("${price}".replace('$',''))
                Log             {price}
                Log             {number}
                ${total_price_value}=       Evaluate        ${total_price_value}+${number}
        END
        Log     ${total_price_value}

        Click Button            id:finish


