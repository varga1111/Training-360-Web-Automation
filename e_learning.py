import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from testdata import Testdata
from basemethods import Base_methods

from selenium.webdriver.common.by import By


class E_Learning(Base_methods):

    '''By Locators'''

    hyper_link_owndev = (By.LINK_TEXT, 'Ismerje meg saját fejlesztésű e-learning tananyagainkat!')
    hyper_link_e_learning_lessons = (By.LINK_TEXT, 'Ismerje meg az E-learningtárat!')
    hyper_link_official = (By.LINK_TEXT, 'Ismerje meg hivatalos e-learning tananyagainkat!')
    hyper_link_mentored = (By.LINK_TEXT, 'Ismerje meg induló mentorált képzéseinket!')
    hyper_link_unique = (By.LINK_TEXT, 'Tudjon meg többet egyedi e-learning megoldásainkról!')

    hyper_link_owndev2 = (By.XPATH, '/html/body/main/div/p[2]/a[1]')
    hyper_link_e_learning_lessons2 = (By.XPATH, '/html/body/main/div/p[2]/a[2]')
    hyper_link_official2 = (By.XPATH, '/html/body/main/div/p[4]/a')
    hyper_link_mentored2 = (By.XPATH, '/html/body/main/div/p[6]/a')
    hyper_link_unique2 = (By.XPATH, '/html/body/main/div/p[8]/a')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.E_LEARNING_URL)


        ''' Get Title'''
    def get_e_learning_title(self, title):
        return self.get_title(title)




    ''' Is Visible'''
    def hyper_link_owndev_exists(self):
        return self.is_visible(self.hyper_link_owndev)

    
    def hyper_link_e_learning_lessons_exists(self):
        return self.is_visible(self.hyper_link_e_learning_lessons)


    def hyper_link_official_exists(self):
        return self.is_visible(self.hyper_link_official)


    def hyper_link_mentored_exists(self):
        return self.is_visible(self.hyper_link_mentored)

    
    def hyper_link_unique_exists(self):
        return self.is_visible(self.hyper_link_unique)




    '''Navigations'''
    def nav_to_elearning_owndev(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[2]/a[1]'))
    
    def nav_to_e_learning_lessons(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[2]/a[2]'))


    def nav_to_e_learning_official(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[4]/a'))


    def nav_to_mentored_courses(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[6]/a'))


    def nav_to_e_learning_unique(self):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/p[8]/a'))

    




#self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('//*[@id="sendMessage_submit"]'))
    