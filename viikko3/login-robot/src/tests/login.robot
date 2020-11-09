*** Settings ***
Resource  resource.robot
Test Setup  Create User Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Username And Password  kalle  kalle123
    Output Should Contain  Logged in

*** Keywords ***
Create User Input Login Command
    Create User  kalle  kalle123
    Input Login Command
