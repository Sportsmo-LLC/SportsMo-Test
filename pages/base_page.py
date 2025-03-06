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
        """Click an element after ensuring it's visible."""
        self.wait_for_element(locator)  # Ensure element is visible before clicking
        self.find(locator).click()

    def wait_and_click(self, locator, timeout=10):
        """Wait for an element to be clickable before clicking."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, locator))
        )
        element.click()

    def type(self, locator, text):
        """Enter text into a field after ensuring it's visible."""
        self.wait_for_element(locator)  # Ensure field is visible before typing
        field = self.find(locator)
        field.clear()  # Clear existing text before typing (optional but recommended)
        field.send_keys(text)

    def is_visible(self, locator, timeout=10):
        """Check if an element is visible."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, locator))
            ).is_displayed()
        except Exception:
            return False

    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be present before interacting."""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.XPATH, locator))
        )
