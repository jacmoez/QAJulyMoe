*** Settings ***
Library         SeleniumLibrary
Library    XML
Library    DateTime

*** Variables ***
${url}                     https://web-staging.renonation.sg/
${get_free_quote}          //*[@id="__next"]/div/div[2]/div/header/div/div[2]/div/button[1]
${condo}                   //*[@id="propertyDetail"]/div[2]/div/fieldset[1]/div/button[2]
${2bedroom}                //*[@id="propertyDetail"]/div[2]/div/div/fieldset/div/button[3]
${resale}                  //*[@id="propertyDetail"]/div[2]/div/fieldset[2]/div/button[2]
${key_no}                  //*[@id="propertyDetail"]/div[2]/div/fieldset[3]/div/button[2]
${year}                    //*[@id="propertyDetail"]/div[2]/div/div[2]/div/fieldset[2]/div/div/div/div[2]
${img}                      C:/Users/DELL/Pictures/flower3.jpg
${bedroom}                 //*[@id="renovationReq"]/div[2]/div/fieldset[1]/div/button[3]  
${livingroom}             //*[@id="renovationReq"]/div[2]/div/fieldset[1]/div/button[11]



*** Keywords ***
Get Free Quote 
     Sleep           2
     Click Button    ${get_free_quote}
     Sleep          2
     #Property type *
     Click Button     ${condo}
     Sleep          2 
     #No. of Bedrooms
     Click Button    ${2bedroom}
     Sleep          2 
    #Property Status *
    Click Button    ${resale}
    Sleep            2 
    #Have you collected your keys? *
    Click Button    ${key_no}
    Sleep            2 
    #What is the estimated key collection period? *
    Click Element    css:.react-select__indicators.css-1wy0on6
    Sleep           2 
    Click Element    xpath://*[text()='Apr - Jun']
    Sleep            2 
    Click Element    ${year}
    Sleep            2 
    Click Element    xpath://*[text()='2026']
    Sleep            2 
    Choose File     name:floorPlanImages    ${img}
    Sleep             3 


Renovation Requirements
   
    Click Element    id:renovationReq
    Sleep            2 
    #Area(s) to Renovate *
    Click Button    css:button[value="Selected areas only"]
    Sleep            2 
    #Select areas(s) *
    Click Button    ${bedroom}
    Sleep            2 
    Click Button    ${livingroom}
    Sleep            2 
    #When it comes to renovation, I prioritize *
    Click Button    //*[@id="renovationReq"]/div[2]/div/fieldset[2]/div/button[2]
    Sleep            2 
    #What is your budget? *
    Click Element    //*[@id="renovationReq"]/div[2]/div/div/fieldset/div/div/div/div[2]
    Sleep           2 
    Click Element    xpath://*[text()="S$40,000 - S$60,000"]
    Sleep           2 
    Click Button    //*[@id="renovationReq"]/div[2]/div/fieldset[3]/div/button[1]
    Sleep           2 
    Scroll Element Into View    //*[@id="bankIds-fb5785b3-1bd3-11ee-a91a-0a0b69d58be8"]
    Sleep           2 
    Click Button    //*[@id="bankIds-fb5785b3-1bd3-11ee-a91a-0a0b69d58be8"]
    Sleep           2 

Contact Information
    
    Click Element    id:contactForm
    Sleep            2 
    #First Name *
    Input Text    id:firstName    QA
    Sleep            2 
    #Last Name *
    Input Text    id:lastName    July Moe
    Sleep            2 
    #Mobile Number *
    Input Text    name:phoneNumber    83114456
    Sleep            2 
    #Email Address *
    Input Text    id:email             julymoe@qa.com 
    Sleep            2 
    #Additional Information
    Input Text    id:additionalInformation    Hello QA July Moe
    Sleep           2 
    #Check box
    Click Button    //*[@id="getTips-yes"]    
    Sleep            2 

*** Test Cases ***
Main 
    Open Browser                 ${url}            browser=Edge
    Maximize Browser Window
    Get Free Quote
    Renovation Requirements
    Contact Information