*** Settings ***
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Home Page
Resource  resource.robot

*** Test Cases ***
Open Without Login
    Go To Todos Page
    Login Page Should Be Open

Initial Todo List
    Login With Test User
    Go To Todos Page
    Should Have Todo Count  0

Create Valid Todo
    Login With Test User
    Go To Todos Page
    Should Have Todo Count  0
    Create Todo  my awesome new todo
    Should Have Todo Count  1
    Should Have Todo  my awesome new todo

Create Todo Without Content
    Login With Test User
    Go To Todos Page
    Should Have Todo Count  0
    Submit New Todo
    Page Should Contain  Content is required
    Should Have Todo Count  0

Remove Todo
    Login With Test User
    Go To Todos Page
    Should Have Todo Count  0
    Create Todo  my awesome new todo
    Should Have Todo Count  1
    Click Button  Remove
    Should Have Todo Count  0

*** Keywords ***
Set New Todo Content
    [Arguments]  ${content}
    Input Text  content  ${content}

Submit New Todo
    Click Button  Create

Create Todo
    [Arguments]  ${content}
    Set New Todo Content  ${content}
    Submit New Todo

Should Have Todo Count
    [Arguments]  ${count}
    Page Should Contain  Todos (${count})

Should Have Todo
    [Arguments]  ${content}
    Page Should Contain  ${content}
