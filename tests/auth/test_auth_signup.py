import pytest
from utils.utils import Utils  # Import utility class
from pages.auth.page_auth_signup import SignUpPage
from pages.auth.page_auth_logout import LogoutPage

def test_mobile_signup_new_user(appium_driver):
    signup_page = SignUpPage(appium_driver)
    logout_page = LogoutPage(appium_driver)
  
    random_email = Utils.generate_random_email()  
    signup_page.signup(random_email, "Intelcorei4uv@")

    signup_page.verify_signup_success()
    
    signup_page.skip_initial_setup()
    
    logout_page.perform_logout()

    assert logout_page.is_logout_successful(), "Logout failed!"


def test_mobile_signup_existing_user(appium_driver):
    signup_page = SignUpPage(appium_driver)

    signup_page.signup("shivanijainlunia@gmail.com", "Intelcorei4uv@")
    
    signup_page.verify_user_already_registered()

    appium_driver.back()
    appium_driver.back()


def test_invalid_password_signup(appium_driver):
    signup_page = SignUpPage(appium_driver)
    random_email = Utils.generate_random_email()

    signup_page.signup(random_email, "abcd1234")
    
    signup_page.verify_password_requirement_message()
