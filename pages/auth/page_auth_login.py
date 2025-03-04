from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
class LoginPage(BasePage):
    def __init__(self, driver):
     super().__init__(driver)
     
    # Locators
    LOGIN_BUTTON = "//android.widget.Button[@content-desc='Log in']"
    EMAIL_TEXT_BOX = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
    EMAIL_TEXT_BOX_2 = "//android.widget.ScrollView/android.widget.EditText[1]"
    PASSWORD_TEXT_BOX = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]"
    PASSWORD_TEXT_BOX_2 = "//android.widget.ScrollView/android.widget.EditText[2]"
    
    def login(self, email, password):
        """Perform login action"""
        self.click(self.LOGIN_BUTTON)
        self.click(self.EMAIL_TEXT_BOX)
        self.type(self.EMAIL_TEXT_BOX_2, email)
        self.click(self.PASSWORD_TEXT_BOX_2)
        self.type(self.PASSWORD_TEXT_BOX_2, password)
        self.click(self.LOGIN_BUTTON)
        
