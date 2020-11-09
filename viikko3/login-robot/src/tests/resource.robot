*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input Username And Password
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
