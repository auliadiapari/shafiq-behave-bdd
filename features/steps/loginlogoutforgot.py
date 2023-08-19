from behave import *
from locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pdb
import time


@given(u'user launch Chrome Browser')
def launch_browser(self):
    # Headed browser
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()

    # # Headless Browser
    # options = Options()
    # options.add_argument("--headless")  #
    # self.driver = webdriver.Chrome(options=options)

## Login Scneario
@when(u'user open shafiq home page and go to login page')
def homepage_and_loginpage(self):
    self.driver.get(Locators.URL)
    self.driver.find_element(By.XPATH, Locators.LOGIN_GO_TO_LOGIN_PAGE).click()


@when(u'user enter email "<aulia.diapari@gmail.com>" and password "<Riverdale06!>"')
def step_impl(self):
    self.driver.find_element(By.ID, Locators.LOGIN_FIELD_EMAIL).send_keys('aulia.diapari@gmail.com')
    self.driver.find_element(By.ID, Locators.LOGIN_FIELD_KATA_SANDI).send_keys('Riverdale06!')
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, Locators.ALL_CAPTCHA).click()
    time.sleep(10)


@when(u'user click on login button')
def verify_captcha_and_login_button(self):
    self.driver.switch_to.default_content()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_CLICK_BUTTON).click()



@then(u'user must successfully login to the Dashboard page')
def verify_dashboard(self):
    sidebar_menu = self.driver.find_element

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


## Logout Scneario
@when(u'user perform Logout')
def step_impl(self):
    self.driver.find_element(By.CSS_SELECTOR, Locators.PROFILE_DROPDOWN).click()
    self.driver.find_element(By.LINK_TEXT, Locators.PROFILE_DROPDOWN_LOGOUT).click()
    

@then(u'user redirected to Home page')
def step_impl(self):
    verfiyInHomePage = self.driver.find_element(By.XPATH, Locators.LOGIN_GO_TO_LOGIN_PAGE)
    assert verfiyInHomePage.is_displayed(), 'Not successfull redirect to homepage'


## Forgot Password Scenario
@then(u'user navigate to forgot password page')
def step_impl(self):
    self.driver.find_element(By.XPATH, Locators.LOGIN_GO_TO_LOGIN_PAGE).click()
    self.driver.find_element(By.XPATH, Locators.LUPA_KATA_SANDI_TXTLINK).click()

    pageTitle = self.driver.find_element(By.XPATH, Locators.LUPA_KATA_SANDI_PGTITLE)
    assert pageTitle.is_displayed, 'PageTitle is not displayed'


@when(u'user enter email "<aulia.diapari@gmail.com>" and submit')
def step_impl(self):
    self.driver.find_element(By.NAME, Locators.LUPA_KATA_SANDI_FIELD_EMAIL).send_keys('email@gmail.com')
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, Locators.ALL_CAPTCHA).click()
    time.sleep(10)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_CLICK_BUTTON).click()
    time.sleep(2)


@then(u'user will notify the validation message')
def step_impl(self):
    verifyMessage = self.driver.find_element(By.CSS_SELECTOR, Locators.LUPA_KATA_SANDI_ALLERT)
    assert verifyMessage.is_displayed()