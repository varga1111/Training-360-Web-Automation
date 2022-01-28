import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from testdata import Testdata
from login import Login
from test_parent import Parent_test
from mainp_after_login import Mainp_after_login

class Test_login(Parent_test):

    def test_loginpage_title(self):
        self.browser = Login(self.browser)

        title = self.browser.get_page_title(Testdata.LOGIN_PAGE_TITLE)

        assert title == Testdata.LOGIN_PAGE_TITLE


    def test_signup_link_visible(self):
        self.browser = Login(self.browser)

        visible = self.browser.is_signup_link_exist()

        assert visible  


    def test_login(self):
        self.browser = Login(self.browser)

        self.browser.do_login(Testdata.USERNAME, Testdata.PASSWORD)


    def test_check_login_succesful(self):
        self.browser = Mainp_after_login(self.browser)
        
        title_after_login = self.browser.get_title_after_login(Testdata.AFTER_LOGIN_PAGE_TITLE)

        assert title_after_login == Testdata.AFTER_LOGIN_PAGE_TITLE
