from src.modules import *
from src.helpers import *

#Test cases --
#Register's a a new user --
def register(driver):
    removeAds(driver)
    waitElement(driver, 'page')
    loginTo = findElement(driver, 'selector','login')
    loginTo.click()
    waitElement(driver, 'selector', 'container')
    signUp = findElement(driver, 'selector', 'signup', 'email')
    signUp.send_keys(fake().name())
    signUp = findElement(driver, 'selector', 'signup', 'pass')
    signUp.send_keys(fake().email())
    submit = findElement(driver, 'selector', 'signup', 'sgnbtn')
    submit.click()
    waitElement(driver, 'selector', 'form', 'main')

#Fills-up form after registration --
def fillUpForm(driver):
    removeAds(driver)
    elements = findElements(driver, 'selector', 'form', 'radio')
    dob = findElements(driver, 'selector', 'form', 'dob')
    dom = findElements(driver, 'selector', 'form', 'dom')
    doy = findElements(driver, 'selector', 'form', 'doy')
    checker = findElements(driver, 'selector', 'form', 'check')
    countries = findElements(driver, 'selector', 'form', 'countries')

    if elements:
        randClick = random.choice(elements)
        randClick.click()

    formSelect(driver, 'form', 'pass').send_keys(fake().password())
    formSelect(driver, 'form', 'day').click()
    selectDate(dob)
    formSelect(driver, 'form', 'months').click()
    selectDate(dom)
    formSelect(driver, 'form', 'year').click()
    selectDate(doy)

    for element in checker:
        element.click()

    formSelect(driver, 'form', 'firstName').send_keys(fake().first_name())
    formSelect(driver, 'form', 'lastName').send_keys(fake().last_name())
    formSelect(driver, 'form', 'company').send_keys(fake().company())
    formSelect(driver, 'form', 'address').send_keys(fake().address())
    formSelect(driver, 'form', 'addressTwo').send_keys(fake().address())
    formSelect(driver, 'form', 'country').click()

    if countries:
        select = random.choice(countries)
        select.click()

    formSelect(driver, 'form', 'state').send_keys(fake().state())
    formSelect(driver, 'form', 'city').send_keys(fake().city())
    formSelect(driver, 'form', 'zip').send_keys(fake().zipcode())
    formSelect(driver, 'form', 'number').send_keys(fake().phone_number())
    formSelect(driver, 'form', 'submit').click()
    waitElement(driver, 'selector', 'form', 'success')

    text = runJavascript(driver, 'selector', 'form', 'script')
    assert text == 'Account Created!'
    formSelect(driver, 'form', 'continue').click()

    removeAds(driver)
    currURL = ec.url_contains('#google_vignette')
    if currURL:
        formSelect(driver, 'form', 'continue').click()

    checkPage = runJavascript(driver, 'selector', 'form', 'navcheck')
    assert checkPage.strip() == 'Logout' #user should be logged-in.
    removeAds(driver)

def dressShopping(driver):
    selection(driver, 'women', 'dress', 'productOne', 'panel', 'Women - Dress Products')

def topsShopping(driver):
    selection(driver, 'women', 'tops', 'productTwo', 'panel', 'Women - Tops Products')

def sareeShopping(driver):
    selection(driver, 'women', 'saree', 'productSeven', 'panel', 'Women - Saree Products')

def tshirtShopping(driver):
    selection(driver, 'men', 'tshirt', 'productThree', 'panelm', 'Men - Tshirts Products')

def jeansShoping(driver):
    selection(driver, 'men', 'jeans', 'productSix', 'panelm', 'Men - Jeans Products')

def kidsDressShopping(driver):
    selection(driver, 'kids', 'kidsDress', 'productFour', 'panelk', 'Kids - Dress Products')

def kidsTopShirts(driver):
    selection(driver, 'kids', 'topShirts', 'productFive', 'panelk', 'Kids - Tops & Shirts Products')

