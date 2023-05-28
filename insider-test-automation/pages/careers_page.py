from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import time
from utils.locators import *

class CareersPage(BasePage):
    def __init__(self, driver):
        self.locator = CareersPageLocators
        super().__init__(driver)

    def is_locations_block_displayed(self):
        locations_block = self.driver.find_element(*self.locator.LOCATIONS)
        return locations_block.is_displayed()

    def is_teams_block_displayed(self):
        teams_block = self.driver.find_element(*self.locator.TEAMS)
        return teams_block.is_displayed()

    def is_life_at_insider_block_displayed(self):
        life_at_insider_block = self.driver.find_element(*self.locator.LIFEATINSIDER)
        return life_at_insider_block.is_displayed()

    def go_to_qa_jobs(self):
        see_all_teams_button = self.driver.find_element(*self.locator.TEAMSBUTTON)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", see_all_teams_button)
        time.sleep(1)

        qa_team_link = self.driver.find_element(*self.locator.QATEAMLINK)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", qa_team_link)
        time.sleep(1)

        see_all_qa_jobs_button = self.driver.find_element(*self.locator.QATEAMBUTTON)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", see_all_qa_jobs_button)
        time.sleep(1)