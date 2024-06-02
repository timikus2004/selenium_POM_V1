import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service




@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path="/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10) # seconds
    yield driver
    driver.quit()