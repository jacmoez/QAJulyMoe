*** Settings ***
Library             SeleniumLibrary

Suite Setup        Open Browser         https://www.saucedemo.com/       Chrome

*** Test Cases ***
Main
    Maximize Browser Window
    Sleep               3s
    Input Text          id=user-name                        standard_user
    Sleep               3s
    Click Button        id=login-button
    Sleep               3s
    ${text}=            Get Text                           css=.error-message-container.error
    Log                 ${text}
    Sleep               5s