from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.SIGNUP_BUTTON = "//android.widget.Button[@content-desc='Sign up with email']"
        self.EMAIL_SIGNUP_BUTTON = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
        self.EMAIL_TEXTBOX = "//android.widget.ScrollView/android.widget.EditText[1]"
        self.PASSWORD_TEXTBOX = "//android.widget.ScrollView/android.widget.EditText[2]"
        self.TICK_CHECKBOX = "//android.widget.ScrollView/android.view.View[2]"
        self.CREATE_ACCOUNT = "//android.widget.Button[@content-desc='Create account']"
        self.SKIP_BUTTON = "//android.widget.Button[@content-desc='Skip']"
        self.SELECT_TEAMS_PAGE = "//android.view.View[@content-desc='Select your favorite teams']"
        self.ERROR_TOAST = "//android.widget.Toast"
        self.PASSWORD_ERROR_MESSAGE = "//android.view.View[@content-desc='Password must be 8+ chars with at least one uppercase, one lowercase, one number & one special char (@$!%*?&).']"

    def signup(self, email, password):
        self.click(self.SIGNUP_BUTTON)
        self.click(self.EMAIL_SIGNUP_BUTTON)
        self.type(self.EMAIL_TEXTBOX, email)
        self.click(self.PASSWORD_TEXTBOX)
        self.type(self.PASSWORD_TEXTBOX, password)
        self.click(self.TICK_CHECKBOX)
        self.click(self.CREATE_ACCOUNT)

    def verify_signup_success(self):
        wait = WebDriverWait(self.driver, 15)  
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, self.SELECT_TEAMS_PAGE)))
            assert self.is_visible(self.SELECT_TEAMS_PAGE), "Signup failed! 'Select your favorite teams' page not found."
        except Exception as e:
            raise AssertionError(f"Signup verification failed! Error: {e}")

    def verify_user_already_registered(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            toast_message_element = wait.until(EC.presence_of_element_located((By.XPATH, self.ERROR_TOAST)))
            toast_message = toast_message_element.text
            assert "User already registered" in toast_message, f"Expected toast message not found! Found: {toast_message}"
        except Exception:
            raise AssertionError("Toast message for existing user not displayed!")

    def skip_initial_setup(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, self.SKIP_BUTTON)))
            self.click(self.SKIP_BUTTON)
        except Exception:
            raise AssertionError("Skip button not found or not clickable after signup!")

    def verify_password_requirement_message(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            error_message_element = wait.until(
                EC.visibility_of_element_located((By.XPATH, self.PASSWORD_ERROR_MESSAGE))
            )
            assert error_message_element.is_displayed(), "Password requirement message not displayed!"
        except Exception:
            raise AssertionError("Password error message did not appear!")
