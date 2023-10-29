from src.mods import *

@pytest.fixture(scope='session')
def getDriver():
    options=Options()
    options.add_argument('--hide-scrollbars')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(data()['base'])
    yield driver
    driver.close()
    driver.quit()
