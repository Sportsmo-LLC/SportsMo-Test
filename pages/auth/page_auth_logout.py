from pages.base_page import BasePage

class LogoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.MORE_BUTTON = '//android.widget.ImageView[@content-desc="More\nTab 4 of 4"]'  
        self.LOGOUT_BUTTON = '//android.widget.Button[@content-desc="Logout"]'
        self.CONFIRM_LOGOUT_BUTTON = '//android.widget.Button[@content-desc="Logout"]'
        self.SIGNUP_BUTTON = '//android.widget.Button[@content-desc="Sign up with email"]'

    def click_logout(self):
        """Clicks the More button, then logs out."""
        self.click(self.MORE_BUTTON)  # Click More button before logout
        self.click(self.LOGOUT_BUTTON)
        self.click(self.CONFIRM_LOGOUT_BUTTON)

    def is_logout_successful(self):
        """Checks if the user is redirected to the signup screen after logout."""
        return self.is_visible(self.SIGNUP_BUTTON)

    def perform_logout(self):
        """Combines logout steps into a reusable function."""
        self.click_logout()
