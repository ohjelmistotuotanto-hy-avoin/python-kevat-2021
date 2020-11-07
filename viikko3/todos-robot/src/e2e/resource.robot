*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0
${HOME URL}  http://${SERVER}/
${RESET URL}  http://${SERVER}/tests/reset
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${TODOS URL}  http://${SERVER}/todos
${TEST USER USERNAME}  johndoe
${TEST USER PASSWORD}  secret

*** Keywords ***
Open Browser To Home Page
    Open Browser  ${HOME URL}  ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Register Page Should Be Open
    Title Should Be  Register

Todos Page Should Be Open
    Title Should Be  Todos

Go To Home Page
    Go To  ${HOME URL}

Go To Login Page
    Go To  ${LOGIN URL}

Go To Register Page
    Go To  ${REGISTER URL}

Go To Todos Page
    Go To  ${TODOS URL}

Reset And Go To Home Page
    Reset
    Go To Home Page

Reset
    Go To  ${RESET URL}

Login With Test User
    Go To Login Page
    Login Page Should Be Open
    Input Text  username  ${TEST USER USERNAME}
    Input Text  password  ${TEST USER PASSWORD}
    Click Button  Login
