*** Settings ***
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Counter Page
Resource  resource.robot

*** Test Cases ***
Counter Initial Value
    Counter Page Should Be Open
    Counter Value Should Be  0
