from src.modules import *
from src.helpers import *

#Test cases --
#Register's a a new user --
def register(driver):
    removeAds(driver)
    waitElement(driver, 'page')
    findElement(driver, 'login', click=True)
    waitElement(driver, 'selector', 'container')
    signUp = findElement(driver, 'signup', 'email')
    signUp.send_keys(generate().name())
    signUp = findElement(driver, 'signup', 'pass')
    signUp.send_keys(generate().email())
    findElement(driver, 'signup', 'sgnbtn', click=True)
    waitElement(driver, 'selector', 'form', 'main')

#Fills-up form after registration --
def fillUpForm(driver):
    removeAds(driver)
    elements = findElements(driver, 'form', 'radio')
    dob = findElements(driver, 'form', 'dob')
    dom = findElements(driver, 'form', 'dom')
    doy = findElements(driver, 'form', 'doy')
    checker = findElements(driver, 'form', 'check')
    countries = findElements(driver, 'form', 'countries')

    if elements:
        randClick = random.choice(elements)
        randClick.click()

    formSelect(driver, 'pass').send_keys(generate().password())
    formSelect(driver, 'day', click=True)
    selectDate(dob)
    formSelect(driver, 'months', click=True)
    selectDate(dom)
    formSelect(driver, 'year', click=True)
    selectDate(doy)

    for element in checker:
        element.click()

    formSelect(driver, 'firstName').send_keys(generate().first_name())
    formSelect(driver, 'lastName').send_keys(generate().last_name())
    formSelect(driver, 'company').send_keys(generate().company())
    formSelect(driver, 'address').send_keys(generate().address())
    formSelect(driver, 'addressTwo').send_keys(generate().address())
    formSelect(driver, 'country', click=True)

    if countries:
        select = random.choice(countries)
        select.click()

    formSelect(driver, 'state').send_keys(generate().state())
    formSelect(driver, 'city').send_keys(generate().city())
    formSelect(driver, 'zip').send_keys(generate().zipcode())
    formSelect(driver, 'number').send_keys(generate().phone_number())
    formSelect(driver, 'submit', click=True)
    waitElement(driver, 'selector', 'form', 'headerText')

    text = findElement(driver, 'form', 'headerText')
    assert text.text == 'ACCOUNT CREATED!'
    formSelect(driver, 'continue', click=True)
    removeAds(driver)

    currURL = expected.url_contains('#google_vignette')
    if currURL:
       formSelect(driver, 'continue', click=True)

    checkPage = findElement(driver, 'form', 'navcheck')
    assert checkPage.text == 'Logout' #user should be logged-in.
    removeAds(driver)

#Shoppping -- Add items to cart
def dressShopping(driver):
    selection(driver, 'women', 'dress', 'productOne', 'panel', 'WOMEN - DRESS PRODUCTS')

def topsShopping(driver):
    selection(driver, 'women', 'tops', 'productTwo', 'panel', 'WOMEN - TOPS PRODUCTS')

def sareeShopping(driver):
    selection(driver, 'women', 'saree', 'productSeven', 'panel', 'WOMEN - SAREE PRODUCTS')

def tshirtShopping(driver):
    selection(driver, 'men', 'tshirt', 'productThree', 'panelm', 'MEN - TSHIRTS PRODUCTS')

def jeansShoping(driver):
    selection(driver, 'men', 'jeans', 'productSix', 'panelm', 'Men - Jeans Products')

def kidsDressShopping(driver):
    selection(driver, 'kids', 'kidsDress', 'productFour', 'panelk', 'Kids - Dress Products')

def kidsTopShirts(driver):
    selection(driver, 'kids', 'topShirts', 'productFive', 'panelk', 'Kids - Tops & Shirts Products')

#checkouts ---
def checkout(driver):
    details = ['Address Details', 'Review Your Order']
    findElement(driver, 'cart', click=True)
    runJavascript(driver, 'contentLoaded')
    items = findElements(driver, 'items')
    text = findElements(driver, 'details')

    if len(items) == 0:
        print("The cart is empty!")
    else:
        findElement(driver, 'checkout', click=True)

    runJavascript(driver, 'contentLoaded')
    for i in text:
        assert i.text in details

    message = findElement(driver, 'message')
    message.send_keys(generate().paragraph())
    findElement(driver, 'proceed', click=True)
    runJavascript(driver, 'contentLoaded')

def payment(driver):
    expected.url_to_be(data('url', 'payment'))
    text = findElement(driver, 'payment', 'getPayment')
    assert text.text == 'Payment'
    findElement(driver, 'payment', 'cardname').send_keys(generate().name())
    findElement(driver, 'payment', 'cardnumber').send_keys(generate().credit_card_number())
    findElement(driver, 'payment', 'cardpin').send_keys(generate().credit_card_security_code())
    findElement(driver, 'payment', 'expiryMonth').send_keys(generate().month())
    findElement(driver, 'payment', 'expiryYear').send_keys(generate().year())
    findElement(driver, 'payment', 'payment', click=True)
    expected.url_to_be(data('url', 'orderPlaced'))
    text = findElement(driver, 'payment', 'orderPlaced')
    assert text.text == 'ORDER PLACED!'
    findElement(driver, 'form', 'continue', click=True)



