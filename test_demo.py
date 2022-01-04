
import time

import requests
from selenium.webdriver.common.keys import Keys


def test_demo1(web_driver_initialize):
    driver = web_driver_initialize
    driver.get('https://www.google.com')
    driver.find_element_by_xpath('//input[@name="q"]').send_keys('pytest')
    driver.find_element_by_xpath('//input[@name="q"]').send_keys(Keys.ENTER)
    time.sleep(15)
    print('run ok')


def test_demo2(web_driver_initialize):
    driver = web_driver_initialize
    driver.get('https://www.google.com')
    driver.find_element_by_xpath('//input[@name="q"]').send_keys('pytest')
    driver.find_element_by_xpath('//input[@name="q"]').send_keys(Keys.ENTER)
    time.sleep(15)
    print('run ok')

