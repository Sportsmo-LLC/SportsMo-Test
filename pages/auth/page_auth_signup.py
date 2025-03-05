from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
        # Locators
        self.SIGNUP_BUTTON ="//android.widget.Button[@content-desc='Sign up with email']"
        self.EMAIL_SIGNUP_BUTTON = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
        self.EMAIL_TEXTBOX = "//android.widget.ScrollView/android.widget.EditText[1]"
        self.PASSWORD_TEXTBOX = "//android.widget.ScrollView/android.widget.EditText[2]"
        self.TICK_CHECKBOX = "//android.widget.ScrollView/android.view.View[2]"
        self.CREATE_ACCOUNT = "//android.widget.Button[@content-desc='Create account']"
        self.SKIP_BUTTON = "//android.widget.Button[@content-desc='Skip']"

    def signup(self, email, password, click_skip=False):
        """Click on Sign up with email button"""
        self.click(self.SIGNUP_BUTTON)
        self.click(self.EMAIL_SIGNUP_BUTTON)
        self.type(self.EMAIL_TEXTBOX, email)
        self.click(self.PASSWORD_TEXTBOX)
        self.type(self.PASSWORD_TEXTBOX, password)
        self.click(self.TICK_CHECKBOX)
        self.click(self.CREATE_ACCOUNT) 
        
        if click_skip:  # Only click the skip button if explicitly requested
           self.click(self.SKIP_BUTTON)

