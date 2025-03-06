import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.options import ArgOptions
@pytest.fixture(scope="session")
def appium_driver():
    desired_caps = {
       "platformName": "Android",
       "appium:automationName": "UiAutomator2",
       "appium:deviceName": "RZCX2243L1M",
       "appium:udid": "RZCX2243L1M",
       "appium:appPackage": "com.example.sportsmo.dev",
       "appium:appActivity": "com.example.sportsmo.MainActivity",
       "appium:noReset": True
    }

    options = AppiumOptions()
    options.load_capabilities(desired_caps)

    driver = webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options  # Use AppiumOptions instead of directly passing desired_caps
    )
 
    yield driver  # Provide the driver to tests
 
    driver.quit()  # Cleanup after tests are done


