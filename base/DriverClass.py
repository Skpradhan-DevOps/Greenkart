
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities import CustomLogger as cl




class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            #driver = webdriver.Chrome(r"C:\Users\SrikantaKumar\Desktop\Python\chromedriver_win32\chromedriver")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            self.log.info("Chrome Driver is initializing")
        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")
        elif browserName == "firefox":
            #driver = webdriver.Firefox(executable_path="/Users/geckodriver")
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            self.log.info("FireFox Driver is initializing")

        return driver