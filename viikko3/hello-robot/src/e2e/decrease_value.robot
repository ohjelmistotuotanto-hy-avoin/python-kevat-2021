*** Settings ***
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Counter Page
Resource  resource.robot

*** Test Cases ***
Decrease Counter Value
    Counter Page Should Be Open
    Counter Value Should Be  0
    Click Button  Decrease
    Counter Value Should Be  -1
