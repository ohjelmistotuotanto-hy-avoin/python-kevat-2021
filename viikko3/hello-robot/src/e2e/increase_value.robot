*** Settings ***
Suite Setup  Open Browser To Counter Page
Suite Teardown  Reset
Resource  resource.robot

*** Test Cases ***
Increase Counter Value
    Counter Value Should Be  0
    Click Button  Increase
    Counter Value Should Be  1
