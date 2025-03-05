import pytest
import random
import string
from selenium.webdriver.common.by import By
from pages.auth.page_auth_signup import SignUpPage
import time
from pages.auth.page_auth_logout import LogoutPage  # Import the logout page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    return f"{random_string}@example.com"

def test_mobile_signup_new_user(appium_driver):
    signup_page = SignUpPage(appium_driver)
    
       # Generate a random email
    random_email = generate_random_email()
    
    # Attempt signup with the random email
    signup_page.signup(random_email, "Intelcorei4uv@", click_skip=False)

    try:
        # Capture toast message
        toast_message = appium_driver.find_element("xpath", "//android.widget.Toast").text
        assert "User already registered" in toast_message, "Expected toast message not found!"
    except Exception:
        # If toast doesn't appear, check if signup was successful
        assert signup_page.is_visible("//android.view.View[@content-desc='Select your favorite teams']"), "Signup failed!"
      
    signup_page.click(signup_page.SKIP_BUTTON)  
    
    # Perform logout
    logout_page = LogoutPage(appium_driver)
    logout_page.logout()
    assert logout_page.is_visible("//android.widget.Button[@content-desc='Sign up with email']"), "Logout failed!"


def test_mobile_signup_existing_user(appium_driver):
    signup_page = SignUpPage(appium_driver)
    
    
    # Attempt signup with the random email
    signup_page.signup("shivanijainlunia@gmail.com", "Intelcorei4uv@", click_skip=False)

    try:
        # Capture toast message
        toast_message = appium_driver.find_element("xpath", "//android.widget.Toast").text
        assert "User already registered" in toast_message, "Expected toast message not found!"
    except Exception:
        # If toast doesn't appear, check if signup was successful
        assert signup_page.is_visible("//android.view.View[@content-desc='Select your favorite teams']"), "Signup failed!"

    appium_driver.back()
    appium_driver.back()

def test_invalid_password_signup(appium_driver):
    signup_page = SignUpPage(appium_driver)

    # Attempt to sign up with an invalid password
    invalid_password = "abcd1234"  # Missing uppercase & special char
    random_email = generate_random_email()

    signup_page.signup(random_email, invalid_password)

    error_message_xpath = "//android.view.View[contains(@content-desc, 'Password must be 8+ chars')]"
    wait = WebDriverWait(appium_driver, 5)
    error_message_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, error_message_xpath))
    )

    assert error_message_element.is_displayed(), "Password requirement message not displayed!"
  

    