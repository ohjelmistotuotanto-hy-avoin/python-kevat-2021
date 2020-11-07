*** Settings ***
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Home Page
Resource  resource.robot

*** Test Cases ***
Login With Valid Credentials
    Go To Login Page
    Login Page Should Be Open
    Set Username  ${TEST USER USERNAME}
    Set Password  ${TEST USER PASSWORD}
    Submit Credentials
    Todos Page Should Be Open

Login With Empty Credentials
    Go To Login Page
    Login Page Should Be Open
    Submit Credentials
    Login Page Should Be Open
    Page Should Contain  Username and password are required

Login With Invalid Credentials
    Go To Login Page
    Login Page Should Be Open
    Set Username  invalidusername
    Set Password  invalidpassword
    Submit Credentials
    Login Page Should Be Open
    Page Should Contain  Invalid username or password

Register Link Click
    Go To Login Page
    Click Link  Register
    Register Page Should Be Open

*** Keywords ***
Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
