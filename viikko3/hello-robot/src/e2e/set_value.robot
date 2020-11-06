*** Settings ***
Suite Setup  Open Browser To Counter Page
Suite Teardown  Close Browser
Test Setup  Reset And Go To Counter Page
Resource  resource.robot

*** Test Cases ***
Set Valid Counter Value
    Counter Value Should Be  0
    Set Counter Value  29
    Submit Counter Value
    Counter Value Should Be  29

Set Empty Counter Value
    Counter Value Should Be  0
    Submit Counter Value
    Counter Value Should Be  0

Set Invalid Counter Value
    Counter Value Should Be  0
    Set Counter Value  foobar
    Submit Counter Value
    Counter Value Should Be  0

*** Keywords ***
Submit Counter Value
    Click Button  Set value

Set Counter Value
    [Arguments]  ${value}
    Input Text  value  ${value}
