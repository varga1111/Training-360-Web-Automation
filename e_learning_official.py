import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from selenium.webdriver.common.by import By

from testdata import Testdata
from basemethods import Base_methods


class E_Learning_Official(Base_methods):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.E_LEARNING_OFFICIAL_URL)


        ''' Get Title '''
    def get_e_learning_official_title(self, title):
        return self.get_title(title)




    ''' Navigations '''
    def go_back(self):
        self.browser.execute_script("window.history.go(-1)")


    