*** Settings ***

Resource            ../CommonResource.robot
Force Tags          MyTag
Library     SeleniumLibrary

*** Variables ***
${url}=         https://parabank.parasoft.com/parabank/index.htm

*** Keywords ***
Register
      Click Element      //html/body/div[1]/div[3]/div[1]/div/p[2]/a
      Sleep    2s
      @{elements}=     Get Web Elements     xpath=//input[starts-with(@id,'customer')]
      @{user_data}=    Create List      first_name     last_name    yangon     sanchang  sanchang_state     111111    09778180778   123456789    user   Abc@123
      ${ind}=    Set Variable       0
      FOR     ${el}    IN     @{elements}
         ${idd}=   Get Element Attribute    ${el}     id
         Log    ${idd}
         Input Text   ${el}        ${user_data}[${ind}]
         ${ind}=    Evaluate     ${ind}+1
         Sleep      2
      END
      Input Text     id:repeatedPassword       Abc@123
      Click Element      //*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input

Login
    Send Value To Input By Name        username         user
    Send Value To Input By Name        password         user
    Click By Xpath      //*[@id="loginPanel"]/form/div[3]/input
    Sleep       5


Open New Account
    Click Link       Open New Account
    Click Element    id:type
    Click Element    //*[@id="type"]/option[2]
    Click Element    class:button
    Sleep      15

Account Overview
    Click Link     Accounts Overview
    Sleep      5
    @{table_data}=    Get Web Elements     //*[@id="accountTable"]/tbody/tr
    FOR    ${tr}    IN    @{table_data}
        FOR    ${i}    IN RANGE    1   4
            ${text}=     Get Text    //*[@id="accountTable"]/tbody/tr[1]/td[${i}]
            Log      ${text}
        END
    END
    Sleep      15


Send Value To Input By Name
    [Arguments]    ${name}         ${value}
     Input Text    name: ${name}      ${value}


Click By Xpath
    [Arguments]    ${x_path}
    Click Element       ${x_path}

*** Test Cases ***
Main
    Open Browser         ${url}      browser= Firefox
    Maximize Browser Window
    #Register
    Login
    #Open New Account
    Account Overview
    Close Browser

