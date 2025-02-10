*** Settings ***
Library                  SeleniumLibrary


*** Variables ***
${url}                  https://testautomationpractice.blogspot.com/
${browser}              Edge


*** Keywords ***
Inpute Filed
        Input Text                      id:name             July Moe
        Sleep                           3
        Clear Element Text              id:name

        ${elements}=                    Get WebElements     css:input[placeholder^='Enter']

        ${user_data}=                   Create List         QA July Moe       july@qa.com             0977554433

        FOR       ${i}                  IN RANGE            0                   3
                                        Input Text          ${elements}[${i}]               ${user_data}[${i}]
                                        Sleep               1
        END

        Input Text                      id:textarea          Downbon, Yangon, Myanmar.
        Sleep                           2

Radio Test
        Click Element                   css:input[value='female']
        Sleep                           2

Checkbox
        #Click Element                   id:sunday
        ${days}=                        Create List         monday      tuesday     thursday        friday      saturday

        FOR                             ${i}                IN RANGE       0            5
                                        Click Element       id:${days}[${i}]
                                        Sleep               2
        END

Select
       #Select From List By Index           id:country              1
       Select From List By Value            id:country              japan
       Sleep                                2
       Select From List By Value            id:colors              yellow           red
       Sleep                                2
       Select From List By Value            id:animals             dog              cat

Date Picker
        Input Text          id:datepicker               07/29/1997
        Sleep               1
        Press Keys          id:datepicker               RETURN
        Sleep               1
        Click Element       id:txtDate
        Sleep               2
        Select From List By Value                       xpath://*[@id="ui-datepicker-div"]/div/div/select[2]                 2020
        Sleep               2
        Select From List By Value                      xpath://*[@id="ui-datepicker-div"]/div/div/select[1]                 2
        Sleep               2
        Click Element       xpath://*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[1]/a


*** Test Cases ***
Main
    Open Browser            ${url}          ${browser}
    Maximize Browser Window
    #Inpute Filed
    #Radio Test
    #Checkbox
    Select
    Date Picker
    Sleep                   5
