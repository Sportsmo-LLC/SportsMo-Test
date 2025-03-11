from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators for login elements
        self.LOGIN_BUTTON = "//android.widget.Button[@content-desc='Log in']"
        self.EMAIL_FIELD_CONTAINER = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
        self.EMAIL_FIELD_INPUT = "//android.widget.ScrollView/android.widget.EditText[1]"
        self.PASSWORD_FIELD_CONTAINER = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]"
        self.PASSWORD_FIELD_INPUT = "//android.widget.ScrollView/android.widget.EditText[2]"

    def login(self, email, password):
        """Perform login action."""
        self.click(self.LOGIN_BUTTON)  
        self.click(self.EMAIL_FIELD_CONTAINER) 
        self.type(self.EMAIL_FIELD_INPUT, email)  
        self.click(self.PASSWORD_FIELD_INPUT) 
        self.type(self.PASSWORD_FIELD_INPUT, password) 
        self.click(self.LOGIN_BUTTON) 

    def verify_login_success(self):
        return self.is_visible("//android.view.View[@content-desc='Highlights View']")

    def verify_invalid_login(self):
        return self.is_visible("//android.view.View[@content-desc='Invalid credentials']")
