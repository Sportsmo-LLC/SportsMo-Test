from pages.base_page import BasePage

class LogoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOGOUT_BUTTON = '//android.widget.Button[@content-desc="Logout"]'
        self.CONFIRM_LOGOUT_BUTTON = '//android.widget.Button[@content-desc="Logout"]'
        self.SIGNUP_BUTTON = '//android.widget.Button[@content-desc="Sign up with email"]'

    def click_logout(self):
        """Navigate to More and click Logout."""
        self.go_to_more()  # Ensures More tab is opened only if necessary
        self.click(self.LOGOUT_BUTTON)  
        self.click(self.CONFIRM_LOGOUT_BUTTON)

    def is_logout_successful(self):
        """Verify if logout was successful by checking the visibility of the Sign-up button."""
        return self.is_visible(self.SIGNUP_BUTTON)

    def perform_logout(self):
        """Execute the logout process."""
        self.click_logout()
