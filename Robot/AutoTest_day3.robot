*** Settings ***
Library                  SeleniumLibrary
Library    XML
Resource    ../AutoTest1.robot

*** Variables ***
${url}                  https://testautomationpractice.blogspot.com/
${browser}              Edge

*** Keywords ***
Search Text
        Input Text    id:Wikipedia1_wikipedia-search-input    Myanmar
        Sleep         3 
        Click Button    class:wikipedia-search-button
        Sleep         3
        Click Element    //*[@id="wikipedia-search-result-link"]/a
        Sleep         3 
       Switch Window
        ${handles}=      Get Window Handles
        Switch Window    ${handles}[1]
        Close Window
        Sleep            3
        Switch Window   ${handles}[0]

Alter
        Click Button    name:start    
        Sleep           3 
        Click Button    name:stop
        Sleep            3 
        Click Button    id:alertBtn
        Sleep            2
        Handle Alert
        Click Button    id:confirmBtn
        Sleep            2 
        Handle Alert    accept
        ${text}=        Get Text    id:demo
        Log To Console    ${text}
        Sleep            3 
        Click Button    id:confirmBtn
        Sleep            2 
        Handle Alert    dismiss
        ${text}=        Get Text    id:demo
        Log To Console    ${text}
        Sleep            3 
        Click Button     id:promptBtn
        Handle Alert     accept
        ${text}=         Get Text    id:demo
        Log To Console    ${text}

New Tab 
      Click Button     //*[@id="HTML4"]/div[1]/button
      Sleep             3 
      ${handles}=      Get Window Handles
      Switch Window    ${handles}[1]
      Sleep            3 
      Close Window
      Switch Window    ${handles}[0]
      Sleep            3 
      Click Button    class:dropbtn
      Sleep            3 
     Scroll Element Into View  //*[@id="HTML3"]/div[1]/div/div/a[2]
      Sleep            3 
      Clear Element Text           id:field1
      Sleep             2 
      Input Text                id:field1          July Moe
      Sleep             3 
      Double Click Element    //*[@id="HTML10"]/div[1]/button
      Sleep            3 
      ${text}=                Get Value    id:field2
      Log To Console         ${text}
     


      




*** Test Cases ***
Main
    Open Browser            ${url}          ${browser}
    Maximize Browser Window
    #Search Text
    Alter 
    New Tab