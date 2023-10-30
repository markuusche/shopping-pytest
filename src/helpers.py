from src.modules import *
from src.modules import data

#Helpers --
def findElement(driver, *keys):
    locator = data(*keys)
    element = driver.find_element(By.CSS_SELECTOR, locator)
    return element

def findElements(driver, *keys):
    locator = data(*keys)
    element = driver.find_elements(By.CSS_SELECTOR, locator)
    return element

def formSelect(driver, *keys):
    locator = findElement(driver, 'selector', *keys)
    return locator 

def runJavascript(driver, *keys):
    text = driver.execute_script(data(*keys))
    return text

def selectDate(func):
    if func and 1 < len(func):
        getRand = random.choice(func[1:])
        getRand.click()

def waitElement(driver, *keys):
    locator = (By.CSS_SELECTOR, data(*keys))
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located(locator)
                ,message="\"Cannot find element\"")
    
def wait_If_Clickable(driver, *keys):
    locator = (By.CSS_SELECTOR, data(*keys))
    wait = WebDriverWait(driver, 10)
    x = wait.until(ec.element_to_be_clickable(locator)
                ,message="\"Cannot find element\"")
    x.click()

def presenceOfEl(driver, *keys):
    locator = (By.CSS_SELECTOR, data(*keys))
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located(locator)
                ,message="\"Cannot find element\"")

def removeAds(driver):
    with open("src/removeAds.js","r") as file:
        script = file.read()

        driver.execute_script(script)

def checkAdsUrl(driver, category, productUrl):
    getUrl = driver.current_url
    vignette = data()['url'][productUrl] + '#google_vignette'
    if getUrl == data()['url']['vignette'] or getUrl == vignette:
      wait_If_Clickable(driver, 'selector', 'category', category)
      pageURL = WebDriverWait(driver, 10).until(ec.url_to_be(data()['url'][productUrl]))
      if not pageURL:
        wait_If_Clickable(driver, 'selector', 'category', category)

def selection(driver,
              genre: str,
              category: str,
              productUrl: str,
              stringAssertion: str):
    """
    Just a small doc for the function.
    
    :param genre: choose a category to shop eg. 'women'.
    :param category: choose what to shop for this genre eg. 'dress' etc.
    :param productUrl: get the current category url
    :param stringAssertion: assert and compare the text from the page

    """
    removeAds(driver)
    formSelect(driver, 'category', genre).click()
    findElement(driver, 'selector', 'category', 'panel')
    wait_If_Clickable(driver, 'selector', 'category', category)
    checkAdsUrl(driver, category, productUrl)
    removeAds(driver)
    
    presenceOfEl(driver, 'selector', 'category', 'featured')
    WebDriverWait(driver, 10).until(ec.url_to_be(data()['url'][productUrl]))
    
    text = runJavascript(driver, 'selector', 'category', 'dressPage')
    assert text == stringAssertion

    product = findElements(driver, 'selector', 'category', 'add')
    for i in product:
        i.click()
        presenceOfEl(driver, 'selector', 'toaster', 'modal')
        wait_If_Clickable(driver, 'selector', 'toaster', 'continue')
