import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from testdata import Testdata
from contact import Contact
from contact_popupobj import Contact_Popupobj
from test_parent import Parent_test


class Test_msg_to_comp(Parent_test):

    def test_get_contacts_page_title(self):
        self.browser = Contact(self.browser)

        title = self.browser.get_contacts_page_title(Testdata.CONTACTS_TITLE)

        assert title == Testdata.CONTACTS_TITLE


    def test_nav_to_message_form(self):

        self.browser = Contact(self.browser)

        self.browser.nav_to_message_form()

    def test_fill_dataform(self):

        self.browser = Contact_Popupobj(self.browser)

        self.browser.fill_data_form(Testdata.NAME, Testdata.EMAIL, Testdata.MESSAGE)