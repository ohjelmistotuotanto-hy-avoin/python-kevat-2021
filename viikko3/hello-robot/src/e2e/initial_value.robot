*** Settings ***
Suite Setup  Open Browser To Counter Page
Suite Teardown  Reset
Resource  resource.robot

*** Test Cases ***
Counter Initial Value
    Counter Value Should Be  0
