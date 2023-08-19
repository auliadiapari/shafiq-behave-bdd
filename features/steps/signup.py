from behave import *
from locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# You can implement step definitions for undefined steps with these snippets:

@given(u'user open Browser')
def step_impl(context):
            # Headed browser
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    # # Headless Browser
    # options = Options()
    # options.add_argument("--headless")  #
    # context.driver = webdriver.Chrome(options=options)

    context.driver.get(Locators.URL)

@then(u'user successfully in home page')
def step_impl(context):
    verfiyInHomePage = context.driver.find_element(By.XPATH, Locators.LOGIN_GO_TO_LOGIN_PAGE)
    assert verfiyInHomePage.is_displayed(), 'Not successfull redirect to homepage'

    context.driver.find_element(By.CSS_SELECTOR, Locators.HOMEPAGE_MULAI_INVESTASI).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.SGNUP_AS_PERSONAL).click()


@then(u'user perform Signup with valid format')
def step_impl(context):
    signUpPageTitle = context.driver.find_element(By.XPATH, Locators.SGNUP_PAGE_TITLE)
    assert signUpPageTitle.is_displayed(), 'Signup page is not displayed'

    # Regsiter with valid Format
    context.driver.find_element(By.ID, Locators.SGNUP_FIELD_NAME).send_keys('test')
    context.driver.find_element(By.ID, Locators.SGNUP_FIELD_EMAIL).send_keys('testasd@gmail.com')
    context.driver.find_element(By.ID, Locators.SGNUP_FIELD_KATA_SANDI).send_keys('Auliard06!')
    context.driver.find_element(By.ID, Locators.SGNUP_FIELD_KONFIRMASI_KATA_SANDI).send_keys('Auliard06!')
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.ID, "recaptcha-anchor-label").click()
    time.sleep(10)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.CSS_SELECTOR, Locators.SGNUP_CLICK_BUTTON).click()
    time.sleep(2)

    # Terms on condition Page
    context.driver.find_element(By.LINK_TEXT, "Kebijakan Privasi").click()
    context.driver.find_element(By.ID, "setuju").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn-block > .text-h4").click()
    

@then(u'user notify with email verification')
def step_impl(context):
    verifyVerificationMessage = context.driver.find_element(By.CSS_SELECTOR, ".text-h2")
    verifyVerificationMessage.is_displayed(), 'Verification Message is not displayed'