import pytest

from pages.auth.page_auth_login import LoginPage
from pages.auth.page_auth_logout import LogoutPage
def test_mobile_logout(appium_driver):
    
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@") 
    
    logout_page = LogoutPage(appium_driver)
    logout_page.perform_logout() 
    
    assert logout_page.is_logout_successful(), "Logout failed!"
