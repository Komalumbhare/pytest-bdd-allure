from behave import *
from selenium.webdriver.common.by import By
from Locators.HomePage import HomePage,RcruitmentPage
from Library import Functions

@when('Navigate to page "{pageName}"')
def navigateToTab(context, pageName):
    Functions.click(context.browser, (By.XPATH,HomePage['pageRecruitment'].format(pageName)))

@then('Recruitment page should display')
def validateRecruitmentPage(context):
    Functions.wait_till_present(context.browser, HomePage['titleRecruitment'])

@when('User selects "{filter}" filter as "{value}"')
def filterBy(context,filter,value):
    Functions.wait_till_present(context.browser, (By.XPATH, RcruitmentPage['dropdownVacancy'].format(filter)))
    Functions.click(context.browser, (By.XPATH,RcruitmentPage['dropdownVacancy'].format(filter)))
    Functions.wait_till_present(context.browser, (By.XPATH,RcruitmentPage['filterBy'].format(value)))
    Functions.click(context.browser, (By.XPATH,RcruitmentPage['filterBy'].format(value)))

@when('Click on Search button')
def filterBy(context):
    Functions.click(context.browser, RcruitmentPage['btnSearch'])

@then('Verify only "{}" vacancies are listed')
def filterBy(context,vacancy):
    cellEntries = Functions.get_all_elements(context.browser, RcruitmentPage['tableCellVacancy'])
    for cell in cellEntries:
        actualVal = Functions.get_text(context.browser,cell)
        assert actualVal==vacancy, 'Wrong Cell entry listed as : '+actualVal

@then('Close Browser')
def closeBrowser(context):
    context.browser.close()
