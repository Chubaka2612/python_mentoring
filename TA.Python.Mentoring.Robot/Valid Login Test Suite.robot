*** Settings ***
Documentation     Tests to verify that account with valid credentials login successful and fail in case of invalid credentials usage.
Library           SeleniumLibrary
Resource          resource.robot

*** Test Cases ***
Valid Login Simple
    [Documentation]    This TC is amed to demonstrate basic features and concepts of RobotFramework
    Open Browser    https://github.com/login    chrome
    Element Should Be Visible    xpath://a[@class='header-logo']
    Input Text    //input[@name='login']    ${VALID USER}
    Input Text    //input[@name='password']    ${VALID PASSWORD}
    Click Button    //input[@name='commit']
    Element Should Be Visible    //details[contains(@class, 'details-overlay')]//*[contains(@class,'avatar-user')]
    [Teardown]    Close Browser

Valid Login
    [Documentation]    This TC is amed to demonstrate custom keywords and variable usage concepts of RobotFramework
    Open Browser To Login Page
    Input User Name    ${VALID USER}
    Input User Password    ${VALID PASSWORD}
    Submit Credentials
    Home Page Should Be Opened
    [Teardown]    Close Browser

Valid Login Gherkin
    [Documentation]    This TC is aimed to demonstrate test scenario in Gherkin Style in RobotFramework
    ...    _Given_ - initial state
    ...    _When_ - the actions
    ...    _Then_ \ - expectations
    ...    Keyword starting with _And_ or _But_ may be used if a step has more than one action.
    Given browser is opened to Login Page
    When user "${VALID USER}" logs in with password "${VALID PASSWORD}"
    Then Home page should be opened
    [Teardown]    Close Browser
