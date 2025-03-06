import pytest
from utils.utils import Utils  # Import utility class
from pages.auth.page_auth_signup import SignUpPage
from pages.auth.page_auth_logout import LogoutPage

def test_mobile_signup_new_user(appium_driver):
    signup_page = SignUpPage(appium_driver)
    logout_page = LogoutPage(appium_driver)

    # Generate a random email using the utility
    random_email = Utils.generate_random_email()  
    signup_page.signup(random_email, "Intelcorei4uv@")

    # Verify that signup was successful by checking for the 'Select your favorite teams' screen
    signup_page.verify_signup_success()
    
    # Now skip the initial setup after successful signup
    signup_page.skip_initial_setup()
    
    # Perform logout verification
    logout_page.perform_logout()

    assert logout_page.is_logout_successful(), "Logout failed!"


def test_mobile_signup_existing_user(appium_driver):
    signup_page = SignUpPage(appium_driver)

    # Attempt signup with an email that is already registered
    signup_page.signup("shivanijainlunia@gmail.com", "Intelcorei4uv@")
    
    # Verify that the error toast for an already registered user is displayed
    signup_page.verify_user_already_registered()

    appium_driver.back()
    appium_driver.back()

def test_invalid_password_signup(appium_driver):
    signup_page = SignUpPage(appium_driver)
    random_email = Utils.generate_random_email()

    # Attempt signup with an invalid password (missing uppercase and special char)
    signup_page.signup(random_email, "abcd1234")
    
    # Verify that the password requirement error message is displayed
    signup_page.verify_password_requirement_message()
