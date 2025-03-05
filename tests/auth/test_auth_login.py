import pytest

from pages.auth.page_auth_login import LoginPage
from pages.auth.page_auth_logout import LogoutPage

def test_mobile_valid_login_(appium_driver):
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")

    assert login_page.is_visible("//android.view.View[@content-desc='Highlights View']"), "Login failed!"
    
    logout_page = LogoutPage(appium_driver)
    logout_page.logout()
    
def test_mobile_Invalid_login_(appium_driver):
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")

    assert login_page.is_visible("//android.view.View[@content-desc='Highlights View']"), "Login failed!"
    
    logout_page = LogoutPage(appium_driver)
    logout_page.logout()
