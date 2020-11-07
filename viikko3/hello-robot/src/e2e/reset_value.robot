*** Settings ***
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Counter Page
Resource  resource.robot

*** Test Cases ***
Reset Counter Value
    Counter Page Should Be Open
    Counter Value Should Be  0
    Click Button  Increase
    Counter Value Should Be  1
    Click Button  Reset
    Counter Value Should Be  0
