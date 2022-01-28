import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from testdata import Testdata
from basemethods import Base_methods
from mainp_after_login import Mainp_after_login

from selenium.webdriver.common.by import By


class Login(Base_methods):

    '''By Locators'''
    
    to_close_popup = (By.ID,'NewsletterModalCloseButton')
    nav_login_button = (By.XPATH, '//*[@id="navbar"]/div[3]/ul/li[3]')
    email = (By.ID,'Username')
    password = (By.ID,'Password')
    login_button = (By.ID,'LoginButton')
    signup_link = (By.LINK_TEXT,'Regisztráció')
    nav_bar_contacts = (By.XPATH,'//*[@id="PrimaryNavMainMenu"]/li[7]/a')
    message_btn1 = (By.XPATH,'//*[@id="sendMessage_submit"]')
    
    '''Constructor of the Parent class'''
    def __init__(self, browser):

        super().__init__(browser)
        self.browser.get(Testdata.URL_LOGIN)


        '''Page actions for login'''
    def get_page_title(self, title):

        return self.get_title(title)

    
    def is_signup_link_exist(self):

        return self.is_visible(self.signup_link)


    def do_login(self, username, password):

        self.do_send_keys(self.email, username)

        self.do_send_keys(self.password, password)

        self.do_click(self.login_button)

        return Mainp_after_login(self.browser)


