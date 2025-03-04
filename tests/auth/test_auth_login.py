import pytest

from pages.auth.page_auth_login import LoginPage


def test_mobile_login(appium_driver):
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")

    assert login_page.is_visible("//android.view.View[@content-desc='Highlights View']"), "Login failed!"
