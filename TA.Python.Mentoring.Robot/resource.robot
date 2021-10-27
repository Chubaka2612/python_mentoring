*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...               The system specific keywords created here form the domain specific language. They utilize keywords provided by the imported SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
${VALID USER}     viktoriya.skirko@gmail.com
${VALID PASSWORD}    PROVIDE OWN PASSWORD
${LOGIN URL}      https://github.com/login
${HOME URL}       https://github.com/
${ERROR URL}      https://github.com/session
&{LOGIN LOCATORS}    username_input=//input[@name='login']    userpassword_input=//input[@name='password']    signin_btn=//input[@name='commit']    logo=//a[@class='header-logo']    error_toast=//div[contains(@class, 'flash-error')]    # Stores web elements locators of Login Page
&{HOME LOCATORS}    avatar=//details[contains(@class, 'details-overlay')]//*[contains(@class,'avatar-user')]    search=//input[contains(@class, 'header-search-input')]    repo_list=//ul[contains(@class, 'repo-list')]    repo_list_item=//li[contains(@class, 'repo-list-item')]//a[@class='v-align-middle']    # Stores web elements locators of Home Page

*** Keywords ***
Open Browser To Login Page
    Log    Open Browser
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    1
    Login Page Should Be Opened

Login Page Should Be Opened
    Log    Verify Login Page is opened
    Title Should Be    Sign in to GitHub · GitHub
    Element Should Be Visible    ${LOGIN LOCATORS.logo}

Go To Login Page
    Log    Go to Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Opened

Input User Name
    [Arguments]    ${username}
    Log    Input User Name
    Input Text    ${LOGIN LOCATORS.username_input}    ${username}

Input User Password
    [Arguments]    ${password}
    Log    Input User Password
    Input Password    ${LOGIN LOCATORS.userpassword_input}    ${password}

Submit Credentials
    Log    Submit Credentials
    Click Button    ${LOGIN LOCATORS.signin_btn}

Home Page Should Be Opened
    Log    Verify Home Page is opened
    Location Should Be    ${HOME URL}
    Title Should Be    GitHub
    Element Should Be Visible    ${HOME LOCATORS.avatar}

Browser Is Opened To Login Page
    Open Browser To Login Page

User "${username}" Logs In With Password "${password}"
    Log    User login with required password
    Input User Name    ${username}
    Input User Password    ${password}
    Submit Credentials

Error Toast Should Be Displayed
    Log    Verify Error Message is dispalyed
    Element Should Be Visible    ${LOGIN LOCATORS.error_toast}

Search Text
    [Arguments]    ${textToSearch}
    Log    Search repositories by text
    Input Text    ${HOME LOCATORS.search}    ${textToSearch}
    Press Keys    ${HOME LOCATORS.search}    ENTER
    Wait Until Element Is Visible    ${HOME LOCATORS.repo_list}
    ${xpath}    Set Variable    ${HOME LOCATORS.repo_list_item}
    ${count}    Get Element Count    ${xpath}
    FOR    ${i}    IN RANGE    1    ${count} +1
        ${itemText}    Get Text    xpath = (${xpath})[${i}]
        Should Contain    ${itemText}    ${textToSearch}    ignore_case=True
    END
