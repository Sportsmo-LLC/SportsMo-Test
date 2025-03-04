import pytest

from pages.auth.page_auth_signup import AuthPage

def test_mobile_signup(appium_driver):
    signup_page = AuthPage(appium_driver)
    signup_page.signup("shivanijainlunia@gmail.com", "Intelcorei4uv@")

    assert signup_page.is_visible("//android.view.View[@content-desc='Highlights View']"), "Signup failed!"

