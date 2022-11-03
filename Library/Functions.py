# Common functions repository
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

__author__ = 'Komal Kumbhare'


# methods
def launch_browser(context):
    context.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.browser.maximize_window()


def get_title(browser):
    '''return Page Title
    :return page title'''
    return browser.title

def go_to_url(browser, url):
    '''go to url'''
    browser.get(url)

def wait_till_present(browser, locator, timeout=30):
    '''Dynamic wait, wait till element to be visible
                :argument locator: By.Xpath, By.ID, etc.
                :argument timeout : By default 15'''
    return WebDriverWait(browser, timeout).until(EC.presence_of_element_located(locator))

def wait_till_visibled(browser, locator, timeout=30):
    '''Dynamic wait, wait till element to be visible
                :argument locator: By.Xpath, By.ID, etc.
                :argument timeout : By default 15'''
    return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(locator))

def set_text(browser, locator, text):
    '''enter text, send text to text field
        :argument locator: By.Xpath, By.ID, etc.
        :argument text : text to be sent/enter'''
    try:
        # find element using explicit wait
        webElement = wait_till_present(browser, locator)
        webElement.send_keys(text)
    except Exception as error:
        raise Exception('Unable to send text due to ', error)

def click(browser, locator):
    '''normal click action using selenium click() method
        :argument locator: By.Xpath, By.ID, etc.'''
    webElement = browser.find_element(*locator)
    webElement.click()

def get_all_elements(browser, locator):
    '''Get all elements by given locat*locatoror'''
    values = browser.find_elements(*locator)
    return values


def get_text(browser, locator):
    '''Get text, return text
        :argument locator: By.Xpath, By.ID, etc.
        :return text : text/label'''
    webElement =browser.find_element(*locator)
    return webElement.text