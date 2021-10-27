*** Settings ***
Documentation     A test suite containing tests related to invalid login. These tests are data-driven. They use a single keyword, specified with Test Template setting, that is called with different arguments to cover different scenarios.
Suite Setup
Suite Teardown
Test Setup        Open Browser To Login Page
Test Teardown     Close Browser
Force Tags
Test Template     Login With Invalid Credentials Should Fail
Library           SeleniumLibrary
Resource          resource.robot

*** Test Cases ***    USERNAME         PASSWORD
Invalid Username      [Tags]           negative
                      invalid          ${VALID PASSWORD}

Invalid Password      [Tags]           negative
                      ${VALID USER}    invalid

Invalid Both          [Tags]           negative
                      invalid          invalid

Empty Username        [Tags]           negative
                      ${EMPTY}         ${VALID PASSWORD}

Empty Password        [Tags]           negative
                      ${VALID USER}    ${EMPTY}

Empty Both            [Tags]           negative
                      ${EMPTY}         ${EMPTY}

*** Keywords ***
Login With Invalid Credentials Should Fail
    [Arguments]    ${username}    ${password}
    Input User Name    ${username}
    Input User Password    ${password}
    Submit Credentials
    Error Toast Should Be Displayed
