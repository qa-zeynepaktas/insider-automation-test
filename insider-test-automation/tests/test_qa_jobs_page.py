import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from pages.qa_jobs_page import *
from pages.careers_page import *

class TestQaPage(BaseTest):

    def test_filter_quality_assurance_jobs(self):
        main_page = MainPage(self.driver)
        main_page.go_to_careers()

        careers_page = CareersPage(self.driver)
        careers_page.go_to_qa_jobs()

        qa_jobs_page = QAJobsPage(self.driver)
        qa_jobs_page.filter_jobs("Istanbul, Turkey", "Quality Assurance")

        jobs_list = qa_jobs_page.get_jobs_list()
        self.assertTrue(len(jobs_list) > 0)

        for index, job in enumerate(jobs_list, start = 1):
            self.assertTrue(qa_jobs_page.is_job_details_valid(index ,job))

        self.assertTrue(qa_jobs_page.apply_to_job)