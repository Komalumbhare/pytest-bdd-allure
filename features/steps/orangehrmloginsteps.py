from behave import *
from Locators.HomePage import HomePage
from Library import Functions

@given('I launch Chrome Browser')
def launchChromeBrowser(context):
    Functions.launch_browser(context)


@when('I open orange HRM Homepage')
def openHomePage(context):
    Functions.go_to_url(context.browser,'https://opensource-demo.orangehrmlive.com')


@then('Enter username "{user}" and password "{pwd}"')
def enterUsernamePassword(context, user, pwd):
    Functions.set_text(context.browser, HomePage['txtUsername'], user)
    Functions.set_text(context.browser, HomePage['txtPassword'], pwd)


@then('Click on Login button')
def clickLogin(context):
    Functions.click(context.browser, HomePage['btnLogin'])

@then('User must successfully login to the Dashboard page')
def verifyUserLoggedIn(context):
    assert Functions.wait_till_present(context.browser, HomePage['logoInsideHome']),'Inside Home Logo not loaded'

@then('User must get Invalid Credentials error')
def verifyInvalidCredsError(context):
    assert Functions.wait_till_present(context.browser, HomePage['invalidCredsMsg']),'Invalid Error Message'
