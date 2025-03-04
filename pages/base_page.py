from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.driver.implicitly_wait(timeout)
        
    def find(self, locator):
        """Find an element."""
        return self.driver.find_element(AppiumBy.XPATH, locator)

    def click(self, locator):
        """Click an element."""
        self.find(locator).click()

    def type(self, locator, text):
        """Enter text into a field."""
        field = self.find(locator)
        #console.log(text)
        field.send_keys(text)

    def is_visible(self, locator):
        """Check if an element is visible."""
        try:
            return self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, locator))).is_displayed()
        except:
            return False
