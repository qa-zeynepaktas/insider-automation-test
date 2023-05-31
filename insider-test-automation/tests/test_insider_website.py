import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import *
from pages.careers_page import *
from pages.qa_jobs_page import *

class TestInsiderWebsiteFunctionalityHomepageCareersAndQaJobApplicationFlowVerification(unittest.TestCase):
    """ Test Case List:
    1. Visit https://useinsider.com/ and check Insider home page is opened or not
    2. Select “More” menu in navigation bar, select “Careers” and check Career page, its
    Locations, Teams and Life at Insider blocks are opened or not
    3. Click “See All Teams”, select Quality Assurance, click “See all QA jobs”, filter jobs by
    Location - Istanbul, Turkey and department - Quality Assurance, check presence of
    jobs list
    4. Check that all jobs’ Position contains “Quality Assurance”, Department contains
    “Quality Assurance”, Location contains “Istanbul, Turkey” and “Apply Now” button
    5. Click “Apply Now” button and check that this action redirects us to Lever Application
    form page
    """

    def setUp(self):
       options = Options()
       options.add_argument('--no-sandbox')
       options.add_argument('disable-infobars')
       options.add_argument("--disable-extensions")
       options.add_argument("--start-fullscreen")
       options.add_argument('--disable-gpu')

       self.driver = webdriver.Chrome(options=options)
       self.driver.get("https://useinsider.com/")

    def test_insider_website_functionality_homepage_careers_and_qa_job_application_flow_verification(self):
       """ 1. Visit https://useinsider.com/ and check Insider home page is opened or not """
       page = HomePage(self.driver)
       self.assertTrue(page.check_page_loaded())

       """ 2. Select “More” menu in navigation bar, select “Careers” and check Career page, its
       Locations, Teams and Life at Insider blocks are opened or not """
       page.go_to_careers()

       careers_page = CareersPage(self.driver)
       self.assertTrue(careers_page.is_locations_block_displayed())
       self.assertTrue(careers_page.is_teams_block_displayed())
       self.assertTrue(careers_page.is_life_at_insider_block_displayed())

       """ 3. Click “See All Teams”, select Quality Assurance, click “See all QA jobs”, filter jobs by
       Location - Istanbul, Turkey and department - Quality Assurance, check presence of
       jobs list """
       careers_page.go_to_qa_jobs()

       qa_jobs_page = QAJobsPage(self.driver)
       qa_jobs_page.filter_jobs("Istanbul, Turkey", "Quality Assurance")

       jobs_list = qa_jobs_page.get_jobs_list()
       self.assertTrue(len(jobs_list) > 0)

       """ 4. Check that all jobs’ Position contains “Quality Assurance”, Department contains
       “Quality Assurance”, Location contains “Istanbul, Turkey” and “Apply Now” button """
       for index, job in enumerate(jobs_list, start=1):
           self.assertTrue(qa_jobs_page.is_job_details_valid(index, job))

       """ 5. Click “Apply Now” button and check that this action redirects us to Lever Application
       form page """
       self.assertTrue(qa_jobs_page.apply_to_job)

    def tearDown(self):
       self.driver.close()

    if __name__ == '__main__':
       unittest.main()