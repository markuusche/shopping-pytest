from src.main import *

def test_signup(driver):
    register(driver) 
    fillUpForm(driver)

def test_buy_dress(driver): 
    dressShopping(driver)

def test_buy_tops(driver):
    topsShopping(driver)

def test_buy_saree(driver):
    sareeShopping(driver)

def test_buy_tshirts(driver):
    tshirtShopping(driver)

def test_buy_jeans(driver):
    jeansShoping(driver)

def test_buy_kids_dress(driver):
    kidsDressShopping(driver)

def test_buy_kids_topShirts(driver):
    kidsTopShirts(driver)
