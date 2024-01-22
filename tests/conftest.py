import time

import pytest

from base.BaseClass import BaseClass
from base.DriverClass import WebDriverClass


@pytest.fixture(scope='class')
def beforeClass(request):
    print("Before Class")
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("https://rahulshettyacademy.com/seleniumPractise/#/")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After Class")


@pytest.fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")


@pytest.fixture(params=["Tomato", "Potato", "Mango"])
def veg(request):
    return request.param

