from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage(BasePage): 
    def __init__(self, driver):
        super().__init__(driver)
        
        # Locators (Updated)
        self.MORE_TAB = "//android.widget.ImageView[@content-desc='More\nTab 4 of 4']"
        self.LOGOUT_BUTTON = "//android.widget.Button[@content-desc='Logout']"
        self.CONFIRM_LOGOUT_BUTTON = "//android.widget.Button[@content-desc='Logout']"

    def logout(self):
        """Perform logout action"""
        print("Clicking on MORE_TAB")
        self.wait_and_click(self.MORE_TAB)

        print("Clicking on LOGOUT_BUTTON")
        self.wait_and_click(self.LOGOUT_BUTTON)

        print("Clicking on CONFIRM_LOGOUT_BUTTON")
        self.wait_and_click(self.CONFIRM_LOGOUT_BUTTON)

    def scroll_to_element(self, locator):
        """Scroll until the element is visible"""
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
