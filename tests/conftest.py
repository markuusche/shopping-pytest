from src.mods import *

@pytest.fixture
def getDriver():
    options=Options()
    options.add_argument('--hide-scrollbars')
    driver = webdriver.Chrome()
    driver.get(data()['base'])
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


#print('something')