*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0
${COUNTER URL}  http://${SERVER}/
${RESET URL}  http://${SERVER}/tests/reset

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Counter Page Should Be Open
    Title Should Be  Counter

Go To Counter Page
    Go To  ${COUNTER URL}

Reset And Go To Counter Page
    Reset
    Go To Counter Page

Counter Value Should Be
    [Arguments]  ${value}
    Page Should Contain  Counter: ${value} 

Reset
    Go To  ${RESET URL}
