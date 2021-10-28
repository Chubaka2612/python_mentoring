*** Settings ***
Library           SeleniumLibrary
Resource          resource.robot

*** Test Cases ***
Find Repository
    [Documentation]    This TC is amed to demonstrate loop mechanism
    Open Browser To Login Page
    Input User Name    ${VALID USER}
    Input User Password    ${VALID PASSWORD}
    Submit Credentials
    Home Page Should Be Opened
    Search Text    python
    [Teardown]    Close Browser
