import pytest
from pages.auth.page_auth_logout import LogoutPage
from pages.auth.page_auth_login import LoginPage  # Import the login page

def test_mobile_logout(appium_driver):
    login_page = LoginPage(appium_driver)  # Initialize the login page
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")
    
    logout_page = LogoutPage(appium_driver)
    logout_page.logout()
    assert logout_page.is_visible("//android.widget.Button[@content-desc='Sign up with email']"), "Logout failed!"