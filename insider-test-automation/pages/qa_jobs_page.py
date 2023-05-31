from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import time

class QAJobsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def filter_jobs(self, location, department):
        time.sleep(1)
        location_filter = self.driver.find_element(By.XPATH,
                                                   f"//select[@name='filter-by-location']/option[text()='{location}']")
        time.sleep(1)
        location_filter.click()

        department_filter = self.driver.find_element(By.XPATH,
                                                     f"//select[@name='filter-by-department']/option[text()='{department}']")
        time.sleep(1)
        department_filter.click()
        time.sleep(1)

    def get_jobs_list(self):
        time.sleep(1)
        jobs_list = self.driver.find_elements(By.XPATH, "//div[contains(@id, 'jobs-list')]/div")
        return jobs_list

    def is_job_details_valid(self, index, job):
        position = job.find_element(By.XPATH, f"//*[@id='jobs-list']/div[{index}]/div/span").text
        department = job.find_element(By.XPATH, f"//*[@id='jobs-list']/div[{index}]/div/span").text
        location = job.find_element(By.XPATH, f"//*[@id='jobs-list']/div[{index}]/div/div").text
        apply_button = job.find_element(By.XPATH, f"//*[@id='jobs-list']/div[{index}]/div/a").get_attribute('text')

        return "Quality Assurance" in position and "Quality Assurance" in department and "Istanbul, Turkey" in location and "Apply Now" in apply_button

    def apply_to_job(self, job):
        time.sleep(1)
        apply_button = job.find_element(By.XPATH, "//*[@id='jobs-list']/div[1]/div/a")
        time.sleep(1)
        apply_button.click()
        time.sleep(1)
        return "lever.co" in self.driver.current_url