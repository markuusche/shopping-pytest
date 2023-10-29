from src.mods import *

#Test cases --
def register(getDriver):
    waitElement(getDriver, 'page')
    loginTo = findElement(getDriver, 'selector','login')
    loginTo.click()
    waitElement(getDriver, 'selector', 'container')
    signUp = findElement(getDriver, 'selector', 'signup', 'email')
    signUp.send_keys(fake().name())
    signUp = findElement(getDriver, 'selector', 'signup', 'pass')
    signUp.send_keys(fake().email())
    submit = findElement(getDriver, 'selector', 'signup', 'sgnbtn')
    submit.click()
    waitElement(getDriver, 'selector', 'form', 'main')

def fillUpForm(getDriver):
    elements = findElements(getDriver, 'selector', 'form', 'radio')
    dob = findElements(getDriver, 'selector', 'form', 'dob')
    dom = findElements(getDriver, 'selector', 'form', 'dom')
    doy = findElements(getDriver, 'selector', 'form', 'doy')
    checker = findElements(getDriver, 'selector', 'form', 'check')
    countries = findElements(getDriver, 'selector', 'form', 'countries')
    created = findElement(getDriver, 'selector', 'form', 'success')


    if elements:
        randClick = random.choice(elements)
        randClick.click()

    formSelect(getDriver, 'pass').send_keys(fake().password())
    formSelect(getDriver, 'day').click()
    selectDate(dob)
    formSelect(getDriver, 'months').click()
    selectDate(dom)
    formSelect(getDriver, 'year').click()
    selectDate(doy)

    for element in checker:
        element.click()

    formSelect(getDriver, 'firstName').send_keys(fake().first_name())
    formSelect(getDriver, 'lastName').send_keys(fake().last_name())
    formSelect(getDriver, 'company').send_keys(fake().company())
    formSelect(getDriver, 'address').send_keys(fake().address())
    formSelect(getDriver, 'addressTwo').send_keys(fake().address())
    formSelect(getDriver, 'country').click()

    if countries:
        select = random.choice(countries)
        select.click()

    formSelect(getDriver, 'state').send_keys(fake().state())
    formSelect(getDriver, 'city').send_keys(fake().city())
    formSelect(getDriver, 'zip').send_keys(fake().zipcode())
    formSelect(getDriver, 'number').send_keys(fake().phone_number())
    formSelect(getDriver, 'submit').click()
    waitElement(getDriver, 'selector', 'form', 'success')
    text = getDriver.execute_script(data('selector', 'form', 'script'))
    assert text == 'Account Created!'
    sleep(3)

#Helpers --
def findElement(getDriver, *keys):
    locator = data(*keys)
    element = getDriver.find_element(By.CSS_SELECTOR, locator)
    return element

def findElements(getDriver, *keys):
    locator = data(*keys)
    element = getDriver.find_elements(By.CSS_SELECTOR, locator)
    return element

def formSelect(getDriver, date):
    locator = findElement(getDriver, 'selector', 'form', date)
    return locator 

def selectDate(func):
    if func and 1 < len(func):
        getRand = random.choice(func[1:])
        getRand.click()

def waitElement(getDriver, *keys):
    locator = (By.CSS_SELECTOR, data(*keys))
    wait = WebDriverWait(getDriver, 10)
    wait.until(ec.visibility_of_element_located(locator)
               ,message="\"Cannot find element\"")
