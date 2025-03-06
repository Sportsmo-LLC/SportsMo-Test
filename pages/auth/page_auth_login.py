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
        self.click(self.LOGIN_BUTTON)  # Open login page
        self.click(self.EMAIL_FIELD_CONTAINER)  # Click email text box container
        self.type(self.EMAIL_FIELD_INPUT, email)  # Enter email
        self.click(self.PASSWORD_FIELD_INPUT)  # Click password text box
        self.type(self.PASSWORD_FIELD_INPUT, password)  # Enter password
        self.click(self.LOGIN_BUTTON)  # Submit login

    def verify_login_success(self):
        """Verify successful login by checking the Highlights View."""
        return self.is_visible("//android.view.View[@content-desc='Highlights View']")

    def verify_invalid_login(self):
        """Verify invalid login attempt by checking for an error message."""
        return self.is_visible("//android.view.View[@content-desc='Invalid credentials']")
