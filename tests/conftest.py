from src.modules import *

@pytest.fixture(scope='session')
def driver():
  options=Options()
  options.add_argument('--hide-scrollbars')
  webDriver = webdriver.Chrome(options=options)
  webDriver.maximize_window()
  webDriver.get(data()['base'])
  yield webDriver
  webDriver.close()
  webDriver.quit()