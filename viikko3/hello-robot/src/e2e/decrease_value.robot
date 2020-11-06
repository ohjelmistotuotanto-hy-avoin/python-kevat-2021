*** Settings ***
Suite Setup  Open Browser To Counter Page
Suite Teardown  Close Browser
Test Setup  Reset And Go To Counter Page
Resource  resource.robot

*** Test Cases ***
Decrease Counter Value
    Counter Value Should Be  0
    Click Button  Decrease
    Counter Value Should Be  -1
