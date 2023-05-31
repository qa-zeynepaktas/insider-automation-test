from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from utils.locators import *

class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
            return "Insider" in self.driver.title

    def go_to_careers(self):
        more_menu = self.driver.find_element(*self.locator.MORE)
        time.sleep(1)
        more_menu.click()
        careers_menu = self.driver.find_element(*self.locator.CAREERS)
        time.sleep(1)
        careers_menu.click()
        time.sleep(1)
