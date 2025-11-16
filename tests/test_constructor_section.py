import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver


# Переход из раздела "Булки" в раздел "Начинки"
def test_navigate_buns_to_fillings(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'kamila_moreva_34_123@yandex.ru'
    password = 'qwerty123'

    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    driver.find_element(*Locators.fillings_section).click()
    assert driver.find_element(*Locators.selected_section).text == "Начинки"

# Переход из раздела "Начинки" в раздел "Соусы"
def test_navigate_fillings_to_sauses(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'kamila_moreva_34_123@yandex.ru'
    password = 'qwerty123'

    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    driver.find_element(*Locators.fillings_section).click()
    driver.find_element(*Locators.sauces_section).click()
    assert driver.find_element(*Locators.selected_section).text == "Соусы"


# Переход из раздела "Соусы" в раздел "Булки"
def test_navigate_sausec_to_buns(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'kamila_moreva_34_123@yandex.ru'
    password = 'qwerty123'

    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    driver.find_element(*Locators.sauces_section).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.selected_section))
    driver.find_element(*Locators.buns_section).click()
    assert driver.find_element(*Locators.selected_section).text == "Булки"