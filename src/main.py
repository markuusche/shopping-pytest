from src.mods import *

#Test cases --
def register(getDriver):
    #isElementVisible(getDriver, 'selector', 'container')
    loginTo = findElement(getDriver, 'selector','login')
    loginTo.click()
    signUp = findElement(getDriver, 'selector', 'signup', 'email')
    signUp.send_keys(fake().name())
    signUp = findElement(getDriver, 'selector', 'signup', 'pass')
    signUp.send_keys(fake().email())
    submit = findElement(getDriver, 'selector', 'signup', 'sgnbtn')
    submit.click()

#Helpers --
def findElement(getDriver, *keys):
    locator = data(*keys)
    element = getDriver.find_element(By.CSS_SELECTOR, locator)
    return element

def isElementVisible(getDriver, *keys):
    locator = data(*keys)
    WebDriverWait(getDriver, 10).until(ec.presence_of_element_located(locator))


#print(data()['selector']['login'])