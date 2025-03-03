*** Settings ***
Library                SeleniumLibrary

Resource    Auto1.robot

*** Variables ***
${url}                https://webfront-uat.yogamovement.com/
${browser}            Edge
${reg_continue}       //html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button

${last_name}          //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input
${female}             //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/div/div
${myanmar}            //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]
${year}              //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]
${day}               //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[5]/div[3]
${complete_btn}
${logout}            //*[@id="header"]/div[2]/div/div/nav[1]/ul/li[1]/div/ul/li[2]/div

*** Keywords ***
Registry
      Sleep                      3 
      Click Link                Register
      Sleep                      3 
      Input Text                name:email            julymoe@yopmail.com
      Sleep                      3 
      Input Text                name:password         123456
      Sleep                      3 
      Click Button               ${reg_continue}
      Sleep                      3
      Input Text                 name:firstname            ဂျူလိုင်မိုး
      Sleep                      2
      Input Text                 ${last_name}             မမိုး 
      Sleep                      2 
      Click Element              ${female}
     
      Sleep                      2 
      Click Element              css:.dropdown-tools.bg-stone
      Sleep                      2 
      Input Text             css:input[placeholder="Search"]            Myanmar 
      Sleep                      1 
      Click Element             ${myanmar}         
      Sleep                      2        
      Input Text                name:mobile                       091234567
      Sleep                      2 
      Click Element               id:dob    
      Sleep                      1 
      Select From List By Value    css:.yearMonthSelect__select.form__select        6
      Sleep                      2 
      Select From List By Value      ${year}                 1997
      Sleep                      2 
      Click Element                ${day}
      Sleep                      2 
      Click Element              css:.district-select-indicator.css-1wy0on6
      Sleep                      1 
      Click Element              xpath://*[text()="Tiktok"]
      Sleep                      2 
      Click Element             xpath://*[text()="Continue"]
      Sleep                      5 

Login 
    Click Link                 Sign In
    Sleep                      3 
     Input Text                name:email            aung10@yopmail.com
      Sleep                      3 
      Input Text                name:password         P@ssw0rd
      Sleep                      3 
      Click Button               ${reg_continue}
      Sleep                      3 
      Click Button               //html/body/div/div/aside/div/div[2]/button
      Sleep                       3 
      
     
Logout 
      Click Element              class:headerNavUser__profile-name
     
      Sleep                       3 
      Click Element             ${logout}
      Sleep                       3 

    
      
*** Test Cases ***
Main 
    Open Browser                ${url}            ${browser}
    Maximize Browser Window
    Click Button                //html/body/div/div/aside/div/div[2]/button
    #Registry
    Login
    Logout
