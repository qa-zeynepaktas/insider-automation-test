import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from pages.careers_page import *

class TestMainPage(BaseTest):

    def test_main_page_load(self):
       page = MainPage(self.driver)
       self.assertTrue(page.check_page_loaded())