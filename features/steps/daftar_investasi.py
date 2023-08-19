from behave import *
from locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



@given(u'user go to shafiq webpage')
def step_impl(context):
            # Headed browser
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    # # Headless Browser
    # options = Options()
    # options.add_argument("--headless")  #
    # context.driver = webdriver.Chrome(options=options)

    context.driver.get(Locators.URL)


@then(u'user navigate to Daftar Investasi')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, Locators.HOMPAGE_DAFTAR_INVESTASI).click()
    verifyPageTitle = context.driver.find_element(By.XPATH, Locators.DFTAR_INVEST_PAGE_TITLE)
    assert verifyPageTitle.is_displayed(), 'Page Title is not displayed'


@then(u'user search the list by filtering')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, Locators.HOMPAGE_DAFTAR_INVESTASI).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.FILTER_ICON).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.FILTER_VALUE_1).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.FILTER_SUBMIT).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.FILTER_ICON).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.FILTER_RESET).click()


@then(u'user search the list by sorting')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, Locators.SORT_ICON).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.SORTING_VALUE_1).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.SORT_ICON).click()
    context.driver.find_element(By.CSS_SELECTOR, Locators.SORTING_RESET).click()


@then(u'user search the list by searching')
def step_impl(context):
    context.driver.find_element(By.NAME, Locators.SEARCH_BAR).send_keys('mobil')
    context.driver.find_element(By.CSS_SELECTOR, Locators.SEARCH_ICON).click()
    rowDisplayed = context.driver.find_element(By.XPATH, Locators.SEARCH_RESULT)
    assert rowDisplayed.is_displayed(), 'Row list item is not displayed'

    context.driver.find_element(By.NAME, Locators.SEARCH_BAR).clear()
    context.driver.find_element(By.CSS_SELECTOR, Locators.SEARCH_ICON).click()
    
    
    
    