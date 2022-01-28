import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class Mentored_Courses(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.MENTORED_COURSES_URL)


    ''' Get Title '''
    def get_mentored_courses_title(self, title):
        return self.get_title(title)
    

    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")