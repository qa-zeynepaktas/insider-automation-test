from selenium.webdriver.common.by import By

class MainPageLocators(object):
    MORE = (By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[6]/a")
    CAREERS = (By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[6]/div/div[1]/div[3]/div/a")

class CareersPageLocators(object):
    LOCATIONS = (By.XPATH, "//*[@id='career-our-location']/div/div/div/div[1]/h3")
    TEAMS = (By.XPATH, "//a[text()='See all teams']")
    TEAMSBUTTON = (By.XPATH, "//*[@id='career-find-our-calling']/div/div/a")
    LIFEATINSIDER = (By.XPATH, "//h2[text()='Life at Insider']")
    QATEAMLINK = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/div[2]/div[12]/div[2]/a")
    QATEAMBUTTON = (By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")