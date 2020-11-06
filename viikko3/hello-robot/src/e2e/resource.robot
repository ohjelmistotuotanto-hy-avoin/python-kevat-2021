*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0
${COUNTER URL}  http://${SERVER}/
${RESET URL}  http://${SERVER}/tests/reset

*** Keywords ***
Open Browser To Counter Page
    Open Browser  ${COUNTER URL}  ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Counter Page Should Be Open

Counter Page Should Be Open
    Title Should Be  Counter

Counter Value Should Be
    [Arguments]  ${value}
    Page Should Contain  Counter: ${value} 

Reset
    Open Browser  ${RESET URL}  ${BROWSER}
    Close Browser
