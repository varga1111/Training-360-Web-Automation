import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from testdata import Testdata
from basemethods import Base_methods
from contact_popupobj import Contact_Popupobj

from selenium.webdriver.common.by import By


class Contact(Base_methods):
    
    '''Locators'''
    main_page_button =(By.XPATH, '//*[@id="navbar"]/div[1]/a/img')

    
    def __init__(self, browser):
    
        super().__init__(browser)
        self.browser.get(Testdata.CONTACTS_URL)


    def get_contacts_page_title(self, title):
        return self.get_title(title)

    '''Navigations'''
    def nav_to_mainpage(self):
        self.do_click(self.main_page_button)

        
    def nav_to_message_form(self): 
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/div[1]/div/div[1]/div[2]/button'))

        return Contact_Popupobj(self.browser)










        #self.do_click(self.message_btn1)

        '''button = self.browser.find_element_by_xpath('//*[@id="sendMessage_submit"]')

        ActionChains(self.browser).move_to_element(button).click(button).perform()

    def fill_data_form(self, name, email, message):
        
        self.do_send_keys(self.name_input, name)
        
        self.do_send_keys(self.email_input, email)
        
        self.do_send_keys(self.msg_box_input, message)

        self.do_click(self.ticker)'''