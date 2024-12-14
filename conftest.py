import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urls import Urls

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1280,720')
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(15)
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()
