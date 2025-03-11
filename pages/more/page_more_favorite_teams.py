import time
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

class FavoriteTeamsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.FAVORITE_TEAMS_TAB = "//android.widget.ImageView[@content-desc='Favorite Teams']"
        self.SEARCH_TEAM = "//android.widget.EditText"
        self.CROSS_BUTTON = "//android.widget.EditText[@text='Tigers']/android.widget.ImageView[2]"
        self.ALL_TEAMS_TAB = "//android.view.View[contains(@content-desc, 'ALL TEAMS')]"
        self.AMERICAN_ATHLETIC_CONFERENCE_TAB = "//android.view.View[contains(@content-desc, 'AMERICAN ATHLETIC CONFERENCE')]"
        self.ATLANTIC_COAST_TAB = "//android.view.View[contains(@content-desc, 'ATLANTIC COAST')]"
        self.BIG_12_TAB = "//android.view.View[contains(@content-desc, 'BIG 12')]"
        self.BIG_TEN_TAB = "//android.view.View[contains(@content-desc, 'BIG TEN')]"
        self.CONFERENCE_USA_TAB = "//android.view.View[contains(@content-desc, 'CONFERENCE USA')]"
        self.FBS_INDEPENDENTS_TAB = "//android.view.View[contains(@content-desc, 'INDEPENDENTS (FBS)')]"
        self.MID_AMERICAN_TAB = "//android.view.View[contains(@content-desc, 'MID-AMERICAN')]"
        self.MOUNTAIN_WEST_TAB = "//android.view.View[contains(@content-desc, 'MOUNTAIN WEST')]"
        self.PAC_12_TAB = "//android.view.View[contains(@content-desc, 'PAC-12')]"
        self.SOUTHEASTERN_TAB = "//android.view.View[contains(@content-desc, 'SOUTHEASTERN')]"
        self.SUN_BELT_TAB = "//android.view.View[contains(@content-desc, 'SUN BELT')]"
        # Dynamic team selector using lambda (returns XPath based on team name)
        self.SELECT_TEAM = lambda team_name: f"//android.view.View[@content-desc='{team_name}']"
        self.CONTINUE_BUTTON = "//android.widget.Button[contains(@content-desc, 'Continue with')]"
        self.DISMISS_BUTTON = "//android.widget.Button[@content-desc='Dismiss']"
        self.VERTICAL_SCROLL_VIEW = "//android.widget.ScrollView"

    def select_favorite_teams_tab(self):
        self.go_to_more()
        self.click(self.FAVORITE_TEAMS_TAB)

    def search_team(self, team_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEAM))
        ).click()
        self.type(self.SEARCH_TEAM, team_name)
        print(f"✅ Searched for team: {team_name}")

    def clear_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEAM))
        ).click()
        cross_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CROSS_BUTTON))
        )
        cross_button.click()
        print("✅ Cross button clicked successfully!")

    def select_all_teams_tab(self):
        self.click(self.ALL_TEAMS_TAB)

    def select_team(self, conference_name, team_name):
        """
        Selects a team by first ensuring the correct conference tab is selected 
        using horizontal scrolling, and then scrolling vertically to find the team.
        """
        # Mapping conference names to their dynamic locators
        conference_locators = {
            "ALL TEAMS": self.ALL_TEAMS_TAB,
            "AMERICAN ATHLETIC": self.AMERICAN_ATHLETIC_CONFERENCE_TAB,
            "ATLANTIC COAST": self.ATLANTIC_COAST_TAB,
            "BIG 12": self.BIG_12_TAB,
            "BIG TEN": self.BIG_TEN_TAB,
            "CONFERENCE USA": self.CONFERENCE_USA_TAB,
            "FBS INDEPENDENTS": self.FBS_INDEPENDENTS_TAB,
            "MID AMERICAN": self.MID_AMERICAN_TAB,
            "MOUNTAIN WEST": self.MOUNTAIN_WEST_TAB,
            "PAC 12": self.PAC_12_TAB,
            "SOUTHEASTERN": self.SOUTHEASTERN_TAB,
            "SUN BELT": self.SUN_BELT_TAB
        }
        if conference_name not in conference_locators:
            raise Exception(f"Conference {conference_name} not recognized.")
        # Horizontal scroll to select conference tab
        self.scroll_horizontally_to_element(conference_locators[conference_name]).click()
        # Build team XPath using the lambda
        team_xpath = self.SELECT_TEAM(team_name)
        # Use UiScrollable to scroll vertically to the team
        self.scroll_vertically_to_element(team_xpath).click()
        print(f"✅ Selected team: {team_name}")

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_dismiss(self):
        self.click(self.DISMISS_BUTTON)

    def un_select_team(self):
        print("Attempting to unselect the team...")
        self.click(self.UN_SELECT_TEAM)

    def select_american_athletic_conference_tab(self):
        self.click(self.AMERICAN_ATHLETIC_CONFERENCE_TAB)

    def select_atlantic_coast_tab(self):
        self.click(self.ATLANTIC_COAST_TAB)

    def select_big_12_tab(self):
        self.click(self.BIG_12_TAB)

    def select_big_ten_tab(self):
        self.click(self.BIG_TEN_TAB)

    def select_conference_usa_tab(self):
        self.click(self.CONFERENCE_USA_TAB)

    def select_fbs_independents_tab(self):
        self.click(self.FBS_INDEPENDENTS_TAB)

    def select_mid_american_tab(self):
        self.click(self.MID_AMERICAN_TAB)

    def select_mountain_west_tab(self):
        self.click(self.MOUNTAIN_WEST_TAB)

    def select_pac_12_tab(self):
        self.click(self.PAC_12_TAB)

    def select_southeastern_tab(self):
        self.click(self.SOUTHEASTERN_TAB)

    def select_sun_belt_tab(self):
        self.click(self.SUN_BELT_TAB)

    # --- Scrolling Methods ---
    def scroll_horizontally_to_element(self, locator, attempts=5):
        """
        Scrolls horizontally until the element is found or attempts run out.
        Uses the provided locator.
        """
        for _ in range(attempts):
            try:
                element = self.driver.find_element(AppiumBy.XPATH, locator)
                if element.is_displayed():
                    return element
            except Exception:
                pass
            # Perform a horizontal swipe (adjust coordinates as needed)
            screen_size = self.driver.get_window_size()
            start_x = int(screen_size['width'] * 0.9)
            end_x = int(screen_size['width'] * 0.1)
            y = int(screen_size['height'] * 0.5)
            self.driver.swipe(start_x, y, end_x, y, 800)
        raise Exception(f"Element not found after horizontal scrolling: {locator}")

    def dismiss_selected_team_overlay(self):
        try:
            empty_space = self.driver.find_element(By.XPATH, "//android.widget.FrameLayout")
            TouchAction(self.driver).tap(empty_space).perform()
            print("✅ Dismissed any overlay UI before scrolling.")
        except NoSuchElementException:
            print("ℹ️ No overlay found. Proceeding with scrolling.")

    def scroll_vertically_to_element(self, locator, max_scrolls=15):
        for _ in range(max_scrolls):
            try:
                element = self.driver.find_element(AppiumBy.XPATH, locator)
                if element.is_displayed():
                    print(f"✅ Found element: {locator}")
                    return element  
            except NoSuchElementException:
                print("🔄 Scrolling down to find the element...")
            
            screen_size = self.driver.get_window_size()
            start_x = screen_size['width'] // 2  
            start_y = int(screen_size['height'] * 0.7)  
            end_y = int(screen_size['height'] * 0.3)  
            self.driver.swipe(start_x, start_y, start_x, end_y, 1000)
        raise Exception(f"❌ Element not found after {max_scrolls} scroll attempts: {locator}")