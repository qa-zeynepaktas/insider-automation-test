import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from pages.careers_page import *

class TestCareersPage(BaseTest):

    def test_navigate_careers_page_and_check_relevant_sections(self):
        page = MainPage(self.driver)
        page.go_to_careers()

        careers_page = CareersPage(self.driver)
        self.assertTrue(careers_page.is_locations_block_displayed())
        self.assertTrue(careers_page.is_teams_block_displayed())
        self.assertTrue(careers_page.is_life_at_insider_block_displayed())