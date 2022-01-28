import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class E_Learning_Owndev(Base_methods):
    
    '''By Locators'''
    hyper_link_office = (By.LINK_TEXT, 'Office (365, 2010, 2013, 2016)')
    hyper_link_it_awareness = (By.XPATH, '/html/body/main/div/div/div/ul[2]/li[4]/a')
    hyper_link_sql_basics = (By.LINK_TEXT, 'SQL alapok')


    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.E_LEARNING_OWNDEV_URL)


    ''' Get Title '''
    def get_e_learning_owndev_title(self, title):
        return self.get_title(title)



    ''' Navigations '''
    def nav_to_e_learning_owndev_office(self):
        self.do_click(self.hyper_link_office)

    
    def nav_to_e_learning_owndev_it_awareness(self):
        self.do_click(self.hyper_link_it_awareness)

    
    def nav_to_it_courses_admin_oracle(self):
        self.do_click(self.hyper_link_sql_basics)


    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")