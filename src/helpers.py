from src.modules import *
from src.modules import data

#Helpers --
def findElement(driver, *keys, click=False):
    locator = data('selector', *keys)
    element = driver.find_element(By.CSS_SELECTOR, locator)
    if click:
        element.click()
    else:
        return element

def findElements(driver, *keys):
    locator = data('selector', *keys)
    element = driver.find_elements(By.CSS_SELECTOR, locator)
    return element

def formSelect(driver, *keys, click=False):
    locator = findElement(driver, 'form', *keys)
    if click:
        locator.click()
    else:
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
    wait.until(expected.visibility_of_element_located(locator)
                ,message="\"Cannot find element\"")
    
def wait_If_Clickable(driver, *keys):
    locator = (By.CSS_SELECTOR, data(*keys))
    wait = WebDriverWait(driver, 10)
    x = wait.until(expected.element_to_be_clickable(locator)
                ,message="\"Cannot find element\"")
    x.click()

def presenceOfEl(driver, *keys):
    locator = (By.CSS_SELECTOR, data(*keys))
    wait = WebDriverWait(driver, 10)
    wait.until(expected.presence_of_element_located(locator)
                ,message="\"Cannot find element\"")

def removeAds(driver):
    with open("src/removeAds.js","r") as file:
        script = file.read()

        driver.execute_script(script)

def checkAdsUrl(driver, category, productUrl):
    getUrl = [driver.current_url, data()['url'][productUrl] + '#google_vignette']
    if getUrl[0] == data()['url']['vignette'] or getUrl[0] == getUrl[1]:
      wait_If_Clickable(driver, 'selector', 'category', category)

    pageURL = WebDriverWait(driver, 15)
    pageURL.until(expected.url_to_be(data()['url'][productUrl]),
                  message="Page didn't load completely. Timed-out.")
    
    if not pageURL:
      wait_If_Clickable(driver, 'selector', 'category', category)

def generate():
    faker = Faker()
    return faker

def selection(driver,
              genre: str,
              category: str,
              productUrl: str,
              panel: str,
              stringAssertion: str):
    """
    Just a small doc for the function.
    
    :param genre: choose a category to shop eg. 'women'.
    :param category: choose what to shop for this genre eg. 'dress' etc.
    :param productUrl: get the current category url
    :param panel: check the category submenu panel eg. '.panel-group #Women .panel-body'
    :param stringAssertion: assert and compare the text from the page
 
    """

    runJavascript(driver, 'contentLoaded')
    removeAds(driver)
    findElement(driver, 'category', genre, click=True)
    waitElement(driver, 'selector', 'category', panel)
    wait_If_Clickable(driver, 'selector', 'category', category)
    runJavascript(driver, 'contentLoaded')
    checkAdsUrl(driver, category, productUrl)
    removeAds(driver)
    
    presenceOfEl(driver, 'selector', 'category', 'featured')
    WebDriverWait(driver, 10).until(expected.url_to_be(data()['url'][productUrl]))
    
    text = findElement(driver, 'category', 'dressPage')
    assert text.text == stringAssertion.upper()

    product = findElements(driver, 'category', 'add')
    for i in product:
        i.click()
        presenceOfEl(driver, 'selector', 'toaster', 'modal')
        wait_If_Clickable(driver, 'selector', 'toaster', 'continue')
        
        ''' getUrl = driver.current_url
        print(getUrl)
        vignette = data()['url'][productUrl] + '#google_vignette'
        if i == product[2]:
            if getUrl == data()['url']['vignette'] or getUrl == vignette:
                wait_If_Clickable(driver, 'selector', 'category', 'tops')
                continue '''

