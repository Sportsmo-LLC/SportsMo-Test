import pytest
from pages.auth.page_auth_login import LoginPage
from pages.auth.page_auth_logout import LogoutPage
from config import EMAIL, PASSWORD, INVALID_PASSWORD

def test_mobile_valid_login(appium_driver):
    login_page = LoginPage(appium_driver)
    logout_page = LogoutPage(appium_driver)

    login_page.login(EMAIL, PASSWORD)

    assert login_page.verify_login_success(), "Login failed!"

    logout_page.perform_logout()
    assert logout_page.is_logout_successful(), "Logout after valid login failed!"


def test_mobile_invalid_login(appium_driver):
    login_page = LoginPage(appium_driver)
    login_page.login(EMAIL, INVALID_PASSWORD)

    print("Page source after invalid login attempt:")
    print(appium_driver.page_source)

    assert not login_page.is_visible("//android.view.View[@content-desc='Highlights View']"), "Invalid login test failed!"
