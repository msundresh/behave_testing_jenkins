from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.home_page import HomePage

@given(u'I navigate to the URL')
def step_impl(context):
    context.browser.get("https://fire.qa.honeywell.com/#/home")


@when(u'I login to the application')
def step_impl(context):

    login_page = LoginPage(context.browser)
    login_page.click_login_button()
    login_page.enter_username("performance.glss@honidentitydev.onmicrosoft.com")
    time.sleep(4)
    login_page.enter_password("Walk12345")
    login_page.click_dont_remember_user()

    time.sleep(20)
    home_page = HomePage(context.browser)
    home_page.click_burger_navigate_icon()
    home_page.click_customer_management_tab()
    home_page.click_add_customer_button()

@then(u'the application should enter accounts page')
def step_impl(context):
    pass

