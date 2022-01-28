import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Trainings_Softskill(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.TRAININGS_SOFTSKILL_URL)


    '''By Locators'''
    btn_leader_trainings =(By.XPATH, '//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/a')
    btn_salesforce_trainings = (By.XPATH, '//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/a')
    btn_competence_improvement_trainings = (By.XPATH, '//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/a')
    btn_coaching = (By.XPATH, '//*[@id="pagecontent"]/div/div[4]/div/div[2]/div/a')


    ''' Get Title '''
    def get_trainings_softskill_title(self, title):
        return self.get_title(title)


    ''' Is Visible'''
    def btn_leader_trainings_exists(self):
        return self.is_visible(self.btn_leader_trainings)


    def btn_salesforce_trainings_exists(self):
        return self.is_visible(self.btn_salesforce_trainings)


    def btn_competence_improvement_trainings_exists(self):
        return self.is_visible(self.btn_competence_improvement_trainings)

    
    def btn_coaching_exists(self):
        return self.is_visible(self.btn_coaching)
        

    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")


    def nav_to_leader_trainings(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[1]/div/div[2]/div/a'))


    def nav_to_salesforce_trainings(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[2]/div/div[2]/div/a'))


    def nav_to_competence_improvement_trainings(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[3]/div/div[2]/div/a'))


    def nav_to_coaching(self):
        self.browser.execute_script('arguments[0].click();', self.browser.find_element_by_xpath('//*[@id="pagecontent"]/div/div[4]/div/div[2]/div/a'))