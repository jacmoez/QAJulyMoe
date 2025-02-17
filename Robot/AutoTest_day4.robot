*** Settings ***
Library                  SeleniumLibrary
Library    XML
Resource    ../AutoTest1.robot

*** Variables ***
${url}                  https://testautomationpractice.blogspot.com/
${browser}              Edge
${slider1}              //*[@id="slider-range"]/span[1]
${slider2}              //*[@id="slider-range"]/span[2]

*** Keywords ***
Drag
  Sleep            3 
  Drag And Drop    id:draggable    id:droppable
  Sleep            2 
  Drag And Drop By Offset    ${slider1}    -75    0
  Sleep            2 
  Drag And Drop By Offset    ${slider2}   -300   0
  Sleep            2
  ${text}=                    Get Text    id:samsung
  Log To Console              ${text}
  ${text}=                    Get Text    id:realme
  Log To Console              ${text}
  ${text}=                    Get Text    id:moto
  Log To Console              ${text}
  Click Element               id:apple 
  Sleep                       2 
  Execute Javascript          window.history.back()
  Sleep                       2 
  Click Element               id:lenovo
  Sleep                       2 
  Execute Javascript          window.history.back()
  Sleep                       2 
  Click Element               id:dell
  Sleep                       2 
  Execute Javascript          window.history.back()
  Sleep                       2 
  FOR    ${i}                 IN RANGE             1             8 
         Click Element        //*[@id="broken-links"]/a[${i}]
         Sleep                2 
         ${title}=            Get Title
         Log To Console       ${title}
         Execute Javascript    window.history.back()
         Sleep                 3    
  END
      ${text}=                Get Text    id:Stats1_totalCount
      Log To Console          ${text}
  
Form 
    Sleep                   3 
    ${user_data}            Create List            QA       July        Moe
    FOR    ${i}             IN RANGE               0        3 
           ${count}=            Evaluate               ${i} + 1 
           Input Text       id:input${count}           ${user_data}[${i}]
           Sleep             2 
           Click Button     id:btn${count}
           Sleep            2 
    END
Hidden 
     Sleep             3 
     Click Link        Hidden Elements & AJAX
     Sleep             3 
     Click Button      id:toggleInput
     ${result}=          Get Text    id:statusLabel
     Log To Console    ${result}
     Sleep             2 
     Click Button    id:toggleCheckbox
     ${result}=          Get Text    id:statusLabel
     Log To Console    ${result}
     Click Button    id:loadContent
     Sleep            4 
     ${result}=        Get Text      id:ajaxContent 
     Log To Console    ${result}

Download Files
    Sleep             2
    Click Link         Download Files
    Sleep              2 
    Input Text         id:inputText     QA July Moe 
    Sleep              2 
    Click Button       id:generateTxt
    Sleep              2 
    Click Element      id:txtDownloadLink
    Sleep              2 
    Click Button       id:generatePdf
    Sleep              2
    Click Element      id:pdfDownloadLink
    Sleep              2 
    Click Button       //*[@id="post-body-7103635191948372757"]/button[3]
    Sleep              3 


*** Test Cases ***
Main
    Open Browser            ${url}          ${browser}
    Maximize Browser Window
    Drag
    Form
    Hidden
    Download Files