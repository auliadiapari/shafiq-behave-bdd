from behave import *
from locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
  


# You can implement step definitions for undefined steps with these snippets:

@given(u'user launch Chrome Browser')
def step_impl(context):
        # Headed browser
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    # # Headless Browser
    # options = Options()
    # options.add_argument("--headless")  #
    # context.driver = webdriver.Chrome(options=options)


## Login Scneario
@when(u'user open shafiq home page and go to login page')
def step_impl(context):
    context.driver.get(Locators.URL)
    context.driver.find_element(By.XPATH, Locators.LOGIN_GO_TO_LOGIN_PAGE).click()


@when(u'user enter email "{email}" and password "{password}"')
def step_impl(context, email, password):
    context.driver.find_element(By.ID, Locators.LOGIN_FIELD_EMAIL).send_keys(email)
    context.driver.find_element(By.ID, Locators.LOGIN_FIELD_KATA_SANDI).send_keys(password)
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, Locators.ALL_CAPTCHA).click()
  
    ## Please pay attention when the test running and encountering image verifications after clicking captcha, you should complete the image puzzle/selections
  
    time.sleep(10)


@when(u'user click on login button')
def step_impl(context):
    context.driver.switch_to.default_content()
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_CLICK_BUTTON).click()


@then(u'user must successfully login to the dashboard page')
def step_impl(context):
    sidebar_menu = context.driver.find_element

    DASHBOARD = sidebar_menu(By.CSS_SELECTOR, Locators.SIDEBAR_DASHBOARD)
    PORTOFOLIO = sidebar_menu(By.CSS_SELECTOR, Locators.SIDEBAR_PORTOFOLIO)
    DOMPET = sidebar_menu(By.CSS_SELECTOR, Locators.SIDEBAR_DOMPET)
    PROFIL = sidebar_menu(By.CSS_SELECTOR, Locators.SIDEBAR_PROFIL)
    BISNIS_SAYA = sidebar_menu(By.CSS_SELECTOR, Locators.SIDEBAR_BISNIS_SAYA)
    LAPORAN = sidebar_menu(By.CSS_SELECTOR, Locators.SIDEBAR_LAPORAN)
    BANTUAN = sidebar_menu(By.CSS_SELECTOR, Locators.SIDEBAR_BANTUAN)

    time.sleep(2)
    
    assert DASHBOARD.is_displayed(), "Dashboard is not displayed"
    assert PORTOFOLIO.is_displayed(), "Portofolio is not displayed"
    assert DOMPET.is_displayed(), "Dompet is not displayed"
    assert PROFIL.is_displayed(), "Profil is not displayed"
    assert BISNIS_SAYA.is_displayed(), "Bisnis Saya is not displayed"
    assert LAPORAN.is_displayed(), "Laporan is not displayed"
    assert BANTUAN.is_displayed(), "Bantuan is not displayed"

    print('assertion is passed')


## Logout Scenario
@when(u'user perform logout')
def step_impl(context):
    driver.find_element(By.CSS_SELECTOR, PROFILE_DROPDOWN).click()
    driver.find_element(By.LINK_TEXT, PROFILE_DROPDOWN_LOGOUT).click()


@then(u'user redirected to home page')
def step_impl(context):
    verfiyInHomePage = context.driver.find_element(By.XPATH, Locators.LOGIN_GO_TO_LOGIN_PAGE)
    assert verfiyInHomePage.is_displayed(), 'Not successfull redirect to homepage'



## Forgot Password Scenario
@then(u'user navigate to forgot password page')
def step_impl(context):
    context.driver.find_element(By.XPATH, Locators.LOGIN_GO_TO_LOGIN_PAGE).click()
    context.driver.find_element(By.XPATH, Locators.LUPA_KATA_SANDI_TXTLINK).click()

    pageTitle = context.driver.find_element(By.XPATH, Locators.LUPA_KATA_SANDI_PGTITLE)
    assert pageTitle.is_displayed, 'PageTitle is not displayed'


@when(u'user enter email "{email}}" and submit')
def step_impl(context):
    context.driver.find_element(By.NAME, Locators.LUPA_KATA_SANDI_FIELD_EMAIL).send_keys(email)
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, Locators.ALL_CAPTCHA).click()
  
    ## Please pay attention when the test running and encountering image verifications after clicking captcha, you should complete the image puzzle/selections
  
    time.sleep(10)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_CLICK_BUTTON).click()
    time.sleep(2)


@then(u'user will notify the validation message')
def step_impl(context):
    verifyMessage = context.driver.find_element(By.CSS_SELECTOR, Locators.LUPA_KATA_SANDI_ALLERT)
    assert verifyMessage.is_displayed()
