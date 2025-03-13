import pytest

from pages.auth.page_auth_login import LoginPage
from pages.auth.page_auth_logout import LogoutPage
from config import EMAIL, PASSWORD
def test_mobile_logout(appium_driver):
    
    login_page = LoginPage(appium_driver)
    login_page.login(EMAIL, PASSWORD)
    
    logout_page = LogoutPage(appium_driver)
    logout_page.perform_logout() 
    
    assert logout_page.is_logout_successful(), "Logout failed!"
