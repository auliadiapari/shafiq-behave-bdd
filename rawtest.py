from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pdb


# BasePage
URL = 'https://www.shafiq.id'
# Homepage
HOMEPAGE_NAVBAR = '//div[@class="navbar-collapse offcanvas-collapse'   # xpath
# Login
LOGIN_GO_TO_LOGIN_PAGE = '//span[@class="text-h4 lg:text-h5"]'  # xpath
LOGIN_FIELD_EMAIL = 'email'  # id
LOGIN_FIELD_KATA_SANDI = 'password'  # id
LOGIN_CLICK_BUTTON = '.\\[ > .text-h4'  # css
# Dashboard
SIDEBAR_DASHBOARD = 'li:nth-child(1)>a>span.side-shortcut__label'  # css
SIDEBAR_PORTOFOLIO = 'li:nth-child(2)>a>span.side-shortcut__label'  # css
SIDEBAR_DOMPET = 'li:nth-child(3)>a>span.side-shortcut__label'  # css
SIDEBAR_PROFIL = 'li:nth-child(4)>a>span.side-shortcut__label'  # css
SIDEBAR_BISNIS_SAYA = 'li:nth-child(5)>a>span.side-shortcut__label'  # css
SIDEBAR_LAPORAN = 'li:nth-child(6)>a>span.side-shortcut__label'  # css
SIDEBAR_BANTUAN = 'li:nth-child(7)>a>span.side-shortcut__label'  # css
ALL_CAPTCHA = '.recaptcha-checkbox-border'  # css

# Logout
PROFILE_DROPDOWN = '.dropdown-toggle'  # css
PROFILE_DROPDOWN_LOGOUT = 'Logout'  # link text

# Forgot Password
HOMEPAGE_NAVBAR_MASUK = '//div[@class="w-1/2 px-2 lg:px-1 lg:w-auto"]'  # xpath
LUPA_KATA_SANDI_TXTLINK = '//a[@class="text-primary-light"]'  # xpath
LUPA_KATA_SANDI_PGTITLE = '//span[@class="leading-tight text-h2 text-primary"]'  # xpath
LUPA_KATA_SANDI_FIELD_EMAIL = 'email'  # name
ALL_CAPTCHA = '.recaptcha-checkbox-border'  # css
LUPA_KATA_SANDI_SUBMIT_BUTTON = '//span[@class="text-h4"]'  # xpath
LUPA_KATA_SANDI_ALLERT = '.site-content' # css


driver = webdriver.Chrome()
driver = driver

    
driver.maximize_window()

driver.get(URL)

## Login
driver.find_element(By.XPATH, LOGIN_GO_TO_LOGIN_PAGE).click()

driver.find_element(By.ID, LOGIN_FIELD_EMAIL).send_keys('aulia.diapari@gmail.com')
driver.find_element(By.ID, LOGIN_FIELD_KATA_SANDI).send_keys('Riverdale06!')
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, ALL_CAPTCHA).click()
time.sleep(10)
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, LOGIN_CLICK_BUTTON).click()
time.sleep(2)

sidebar_menu = driver.find_element

DASHBOARD = sidebar_menu(By.CSS_SELECTOR, SIDEBAR_DASHBOARD)
PORTOFOLIO = sidebar_menu(By.CSS_SELECTOR, SIDEBAR_PORTOFOLIO)
DOMPET = sidebar_menu(By.CSS_SELECTOR, SIDEBAR_DOMPET)
PROFIL = sidebar_menu(By.CSS_SELECTOR, SIDEBAR_PROFIL)
BISNIS_SAYA = sidebar_menu(By.CSS_SELECTOR, SIDEBAR_BISNIS_SAYA)
LAPORAN = sidebar_menu(By.CSS_SELECTOR, SIDEBAR_LAPORAN)
BANTUAN = sidebar_menu(By.CSS_SELECTOR, SIDEBAR_BANTUAN)

assert DASHBOARD.is_displayed(), "Dashboard is not displayed"
assert PORTOFOLIO.is_displayed(), "Portofolio is not displayed"
assert DOMPET.is_displayed(), "Dompet is not displayed"
assert PROFIL.is_displayed(), "Profil is not displayed"
assert BISNIS_SAYA.is_displayed(), "Bisnis Saya is not displayed"
assert LAPORAN.is_displayed(), "Laporan is not displayed"
assert BANTUAN.is_displayed(), "Bantuan is not displayed"

print('assertion is passed')

## Logout
driver.find_element(By.CSS_SELECTOR, PROFILE_DROPDOWN).click()
driver.find_element(By.LINK_TEXT, PROFILE_DROPDOWN_LOGOUT).click()

verfiyInHomePage = driver.find_element(By.XPATH, LOGIN_GO_TO_LOGIN_PAGE)
assert verfiyInHomePage.is_displayed(), 'Not successfull redirect to homepage'


## Fotgot Password
driver.find_element(By.XPATH, LOGIN_GO_TO_LOGIN_PAGE).click()
driver.find_element(By.XPATH, LUPA_KATA_SANDI_TXTLINK).click()

pageTitle = driver.find_element(By.XPATH, LUPA_KATA_SANDI_PGTITLE)
assert pageTitle.is_displayed, 'PageTitle is not displayed'

driver.find_element(By.NAME, LUPA_KATA_SANDI_FIELD_EMAIL).send_keys('email@gmail.com')
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, ALL_CAPTCHA).click()
time.sleep(10)
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, LOGIN_CLICK_BUTTON).click()
time.sleep(2)
verifyMessage = driver.find_element(By.CSS_SELECTOR, LUPA_KATA_SANDI_ALLERT)
assert verifyMessage.is_displayed()