import pytest
from pages.auth.page_auth_login import LoginPage
from pages.more.page_more_favorite_teams import FavoriteTeamsPage
from pages.auth.page_auth_logout import LogoutPage
from utils.utils import Utils

def test_favorite_teams_search(appium_driver):
    # Log in to the app
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")
    
    # Navigate to Favorite Teams page
    fav_teams_page = FavoriteTeamsPage(appium_driver)
    fav_teams_page.select_favorite_teams_tab()

    # Search for a team
    fav_teams_page.search_team("Tigers")
    # Assert that the search result is visible
    assert fav_teams_page.is_visible("(//android.view.View[@content-desc='Tigers'])[1]"), "Team search failed!"
    
    # Clear the search
    fav_teams_page.clear_search()
    
    # Navigate back to previous screen(s)
    appium_driver.back()
    appium_driver.back()
    
    # Log out
    logout_page = LogoutPage(appium_driver)
    logout_page.perform_logout()
    assert logout_page.is_logout_successful(), "Logout failed!"

def test_favorite_teams_tabs(appium_driver):
    # Log in to the app
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")
    
    # Navigate to Favorite Teams page
    fav_teams_page = FavoriteTeamsPage(appium_driver)
    fav_teams_page.select_favorite_teams_tab()
    
    # Navigate through each conference tab
    fav_teams_page.select_all_teams_tab()
    fav_teams_page.select_american_athletic_conference_tab()
    fav_teams_page.select_atlantic_coast_tab()
    fav_teams_page.select_big_12_tab()
    fav_teams_page.select_big_ten_tab()
    fav_teams_page.select_conference_usa_tab()
    fav_teams_page.select_fbs_independents_tab()
    fav_teams_page.select_mid_american_tab()
    fav_teams_page.select_mountain_west_tab()
    fav_teams_page.select_pac_12_tab()
    fav_teams_page.select_southeastern_tab()
    fav_teams_page.select_sun_belt_tab()
    
    appium_driver.back()  # Return to previous screen
    
    # Log out
    logout_page = LogoutPage(appium_driver)
    logout_page.perform_logout()
    assert logout_page.is_logout_successful(), "Logout failed!"

def test_adding_all_teams_in_favorites(appium_driver):
    # Log in to the app
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")
    
    # Navigate to Favorite Teams page
    fav_teams_page = FavoriteTeamsPage(appium_driver)
    fav_teams_page.select_favorite_teams_tab()
    
    # In "ALL TEAMS" conference, add two teams
    fav_teams_page.select_all_teams_tab()
    fav_teams_page.select_team("ALL TEAMS", "Bears")
    fav_teams_page.click_continue()
    
    # Verify that the "Favorite teams updated!" pop-up appears and then dismiss it
    assert fav_teams_page.is_visible("//android.widget.ImageView[contains(@content-desc, 'Favorite teams updated!')]"), "Favorite teams update failed!"
    fav_teams_page.click_dismiss()
    
    # Log out
    logout_page = LogoutPage(appium_driver)
    logout_page.perform_logout()
    assert logout_page.is_logout_successful(), "Logout failed!"

def test_adding_atlantic_coast_teams_in_favorites(appium_driver):
    # Log in to the app
    login_page = LoginPage(appium_driver)
    login_page.login("shivanijainlunia@gmail.com", "Intelcorei3uv@")
    
    # Navigate to Favorite Teams page
    fav_teams_page = FavoriteTeamsPage(appium_driver)
    fav_teams_page.select_favorite_teams_tab()
    


    # Select the "ATLANTIC COAST" conference and then add a team
    fav_teams_page.select_team("ATLANTIC COAST", "Demon Deacons")
    fav_teams_page.click_continue()
    
    # Verify that the "Favorite teams updated!" pop-up appears and then dismiss it
    assert fav_teams_page.is_visible("//android.widget.ImageView[contains(@content-desc, 'Favorite teams updated!')]"), "Favorite teams update failed!"
    fav_teams_page.click_dismiss()
    
    # Log out
    logout_page = LogoutPage(appium_driver)
    logout_page.perform_logout()
    assert logout_page.is_logout_successful(), "Logout failed!"
