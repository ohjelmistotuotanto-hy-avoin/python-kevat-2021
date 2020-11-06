*** Settings ***
Suite Setup  Open Browser To Counter Page
Suite Teardown  Reset
Resource  resource.robot

*** Test Cases ***
Reset Counter Value
    Counter Value Should Be  0
    Counter Page Should Be Open
    Click Button  Increase
    Counter Value Should Be  1
    Click Button  Reset
    Counter Value Should Be  0
