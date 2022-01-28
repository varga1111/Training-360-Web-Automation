from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



from testdata import Testdata

'''This class is the parent of all pages.'''
'''It contains all the generic methods and utilities for all pages.'''
class Base_methods(Testdata):

    def __init__(self, browser):
        self.browser = browser
        self.browser.maximize_window()


    def do_click(self, by_locator):
         wait(self.browser, 20).until(EC.element_to_be_clickable(by_locator)).click()


    def do_send_keys(self, by_locator, text):
        wait(self.browser, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)


    def is_visible(self, by_locator):
        element = wait(self.browser, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    
    def get_title(self, title):
        wait(self.browser, 10).until(EC.title_is(title))
        return self.browser.title

    
    def hover(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element)
        actions.perform()
    
    '''def go_back(self):
        self.browser.execute_script("window.history.go(-1)")'''
    
    '''def execute_script(self, by_locator):
        wait(self.browser, 10).until(EC.presence_of_element_located(by_locator))
        self.browser.execute_script('arguments[0].click();' , by_locator)'''


    '''def get_element_text(self, by_locator):
        element = wait(self.browser, 10).until(EC.presence_of_element_located(by_locator))
        
        return element.text'''

    