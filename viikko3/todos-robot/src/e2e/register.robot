*** Settings ***
Suite Setup  Open Browser To Home Page
Suite Teardown  Close Browser
Test Setup  Reset And Go To Home Page
Resource  resource.robot

*** Test Cases ***
Register With Valid Credentials
    Go To Register Page
    Register Page Should Be Open
    Set Username  newuserusername
    Set Password  newuserpassword
    Submit Credentials
    Todos Page Should Be Open

Register With Empty Credentials
    Go To Register Page
    Register Page Should Be Open
    Submit Credentials
    Register Page Should Be Open
    Page Should Contain  Username and password are required

Register With Existing Username
    Go To Register Page
    Register Page Should Be Open
    Set Username  ${TEST USER USERNAME}
    Set Password  newuserpassword
    Submit Credentials
    Register Page Should Be Open
    Page Should Contain  Username already exists

Login Link Click
    Go To Register Page
    Register Page Should Be Open
    Click Link  Login
    Login Page Should Be Open

*** Keywords ***
Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
