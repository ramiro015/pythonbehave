from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback


@when('I go to "{url}"')
def step_go_to_url(context, url):
    context.browser.get("http://"+url)

@when('I type "{word}" in the searchbox')
def step_insert_query(context, word):
    search_field = context.browser.find_element_by_id("lst-ib")
    search_field.send_keys(word)


@when('I press ENTER in the searchbox')
def step_search(context):
    search = context.browser.find_element_by_id("lst-ib")
    search.send_keys(Keys.ENTER)


@when('I click on Selenium HQ link')
def step_select_selenium_page(context):
    try:
        result = WebDriverWait(context.browser, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Selenium - Web Browser Automation"))
        )
        result.click()
    except(TimeoutException, StaleElementReferenceException):
        traceback.print_exc()


@then('Im on Selenium HQ Page')
def step_verify_selenium_page(context):
    assert context.browser.current_url == "http://www.seleniumhq.org/"
