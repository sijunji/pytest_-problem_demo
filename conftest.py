
import pytest
from selenium import webdriver
global driver


@pytest.fixture(scope='session')
def web_driver_initialize():
    """
    Initialize the browser
    """
    global driver
    chrome_driver_path = '/Users/sijunji/ProjectFile/PYObject/TMT_QA_UI_Test/demo/chromedriver'
    driver = webdriver.Chrome(chrome_driver_path)
    return driver


@pytest.fixture(scope='session', autouse=True)
def quit_driver(request):
    """
    :return:
    """
    def _quit_driver():
        driver.quit()
    request.addfinalizer(_quit_driver)

