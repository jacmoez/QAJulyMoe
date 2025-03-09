*** Settings ***
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
    Send Value To Input By Name        password         Abc@123
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

Transfer Funds
    Click Link                      Transfer Funds
    Input Text                      id:amount            100
    Sleep                           5
    Click Element                   id:fromAccountId
    Select From List By Value          id:fromAccountId        17229
    Sleep                           3
    Click Element                   id:toAccountId
    Select From List By Value          id:toAccountId        17007
    Sleep                           3
    Click Button                    class:button
Pay Bill
    Click Link                      Bill Pay
    Sleep    2s
    @{elements}=     Get Web Elements     xpath=//input[starts-with(@name,'payee')]
    @{user_data}=    Create List      user    yangon     sanchang  sanchang_state     111111    09778180778     17229
    ${ind}=    Set Variable       0
    FOR     ${el}    IN     @{elements}
       ${idd}=   Get Element Attribute    ${el}     id
       Log    ${idd}
       Input Text   ${el}        ${user_data}[${ind}]
       ${ind}=    Evaluate     ${ind}+1
       Sleep      2
    END
    Input Text                                  name:verifyAccount          17229
    Input Text                                  name:amount                 50
    Click Element                               name:fromAccountId
    Select From List By Value                   name:fromAccountId        17007
    Sleep                                       3
    Click Button                                class:button

Find Transition
    #accountId
    Click Link                                  Find Transactions
    Click Element                               id:accountId
    Select From List By Value                   id:accountId                    17007
    Input Text                                  id:transactionDate              03-09-2025
    Click Button                                id:findByDate
    Sleep                                       3

    Click Link                                  Find Transactions
    Input Text                                  id:fromDate                     03-08-2025
    Input Text                                  id:toDate                       03-09-2025
    Click Button                                id:findByDateRange
    Sleep                                       3

    Click Link                                  Find Transactions
    Input Text                                  id:amount                       50
    Click Button                                id:findByAmount
Update Contact Info
    Click Link                                   Update Contact Info
#    @{element_ids}=    Create List               customer.address.zipCode        customer.address.street      customer.phoneNumber
#    @{user_data}=      Create List               222222                          Mandalay                      09654321
    @{element_ids}=    Create List          //input[@id="customer.address.zipCode"]
    @{user_data}=      Create List               222222
    ${ind}=    Set Variable       0
    FOR     ${idd}    IN     @{element_ids}
     ${el}=   Get WebElement        ${idd}
     Input Text     ${el}         55555
     Sleep      5
    END

#    FOR     ${idd}    IN     @{element_ids}
#       Log To Console        ${idd}
#       Log To Console         ${user_data}[${ind}]
#       ${el}=   Get WebElement        id:${idd}
#       Log To Console        ${el}
#       ${txt}=   Get Element Attribute    ${el}     value
#       Log To Console        ${txt}
#       Log To Console        ------------------------------------
#
#       Click Element                 ${el}
#       Clear Element Text        ${el}
#       Input Text   ${el}        ${user_data}[${ind}]
#       ${ind}=    Evaluate     ${ind}+1
#       Sleep      2
#    END
    Click Button                                 class:button
    Sleep                                        5
    Click Link                                   Update Contact Info

*** Test Cases ***
Main
    Open Browser         ${url}                  browser= Edge
    Maximize Browser Window
    #Register
    Login
    #Transfer Funds
    #Open New Account
    #Account Overview
    #Pay Bill
    #Find Transition
    Update Contact Info
    Sleep     50
    Close Browser
