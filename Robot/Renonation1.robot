*** Settings ***
Library                  SeleniumLibrary
Library    XML
Resource    ../AutoTest1.robot

*** Variables ***
${url}                        https://www.renonation.sg/
${browser}                    Edge
${style_xpath}                //*[@id="__next"]/div/main/section[1]/div[2]/div/form/div[2]/div[1]/fieldset/div/div/div/div
${budget_xpath}               //*[@id="__next"]/div/main/section[1]/div[2]/div/form/div[2]/div[2]/fieldset/div/div/div
${find}                       //*[@id="__next"]/div/main/section[1]/div[2]/div/form/button
${tampines_greengem}          //*[@id="allProject"]/div/div[1]/div/div/div[1]
${header}                     //*[@id="radix-:r2e:"]/div/main/div/div/div[1]/div[1]


*** Keywords ***
Search
     Click Element    css:.custom-react-select__control.css-1xjxcct-control
     Sleep            2 
     Click Element    xpath://*[text()='HDB']
     Sleep            2
     Click Element    ${style_xpath}
     Sleep            2 
     Click Element    xpath://*[text()='French']
     Sleep            2
     Click Element    ${style_xpath}
     Sleep            2 
     Click Element    xpath://*[text()='Classic']
     Sleep            2
     Click Element    ${budget_xpath}
     Sleep            2 
     Click Element    xpath://*[text()='S$40,001 - S$60,000']
     Sleep            2 
     Click Button    ${find} 
     Sleep            3 
     ${result}=       Get Text      //*[@id="allProject"]/div/h6
     Log To Console    ${result}
     Click Element    ${tampines_greengem} 
     Sleep              2
     ${result}=        Get Text    css:.header-h3-regular.text-white
     Log To Console    ${result}
     Sleep              5
     
    



*** Test Cases ***
Main
    Open Browser            ${url}          ${browser}
    Maximize Browser Window
    Search
    
  