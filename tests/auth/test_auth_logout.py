import pytest

from pages.auth.page_auth_login import LoginPage
from pages.auth.page_auth_logout import LogoutPage
def test_mobile_logout(appium_driver):
    """Test case to verify logout functionality."""
    
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")  # Perform login
    
    logout_page = LogoutPage(appium_driver)
    logout_page.perform_logout()  # Perform logout
    
    assert logout_page.is_logout_successful(), "Logout failed!"
