import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Contact_Popupobj(Base_methods):

    '''Locators'''

    name_input = (By.ID,'Name')
    email_input = (By.ID,'Email')
    msg_box_input = (By.ID,'Message')
    ticker = (By.XPATH,'//*[@id="MessageSendingForm"]/div[4]/label')
    message_btn1 = (By.XPATH,'//*[@id="sendMessage_submit"]')

    def __init__(self, browser): 
        super().__init__(browser)


    def fill_data_form(self, name, email, message):
        
        self.do_send_keys(self.name_input, name)
        
        self.do_send_keys(self.email_input, email)
        
        self.do_send_keys(self.msg_box_input, message)

        self.do_click(self.ticker)

    
    def submit_message(self):
        self.do_click(self.message_btn1)

        