from base.BaseClass import BaseClass
from utilities import CustomLogger as cl


class Search(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger()
    _searchField = "input[type='search']"  # css
    _addCart = "//button[contains(text(),'ADD TO CART')]"  # xpath

    def searchGreen(self, veg):
        self.sendText(veg, self._searchField, "css")
        self.log.info("Entered vegetable")
        self.clickOnElement(self._addCart, "xpath")
        self.log.info("Added to cart")
