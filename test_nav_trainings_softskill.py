import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_Softskill')

from testdata import Testdata
from test_parent import Parent_test

from trainings_softskill import Trainings_Softskill
from trainings_softskill_leader_trainings import Trainings_Softskill_Leader_Trainings
from trainings_softskill_salesforce_trainings import Trainings_Softskill_Salesforce_Trainings
from trainings_softskill_competence_improvement_trainings import Trainings_Softskill_Competence_Improvement_Trainings
from trainings_softskill_coaching import Trainings_Softskill_Coaching

class Test_Nav_Trainings_Softskill(Parent_test):
    
    def test_get_trainings_softskill_title(self):
        self.browser = Trainings_Softskill(self.browser)

        title = self.browser.get_trainings_softskill_title(Testdata.TRAININGS_SOFTSKILL_TITLE)

        assert title == Testdata.TRAININGS_SOFTSKILL_TITLE


        # Check Trainings/Softskill Page Elements Exist
    def test_btn_leader_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        self.browser.btn_leader_trainings_exists()
        

    def test_btn_salesforce_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        self.browser.btn_salesforce_trainings_exists()


    def test_btn_competence_improvement_trainings_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        self.browser.btn_competence_improvement_trainings_exists()


    def test_btn_coaching_exists(self):
        self.browser = Trainings_Softskill(self.browser)
        self.browser.btn_coaching_exists()




        ''' Test Navigations & Page Titles Match & Elements Exist'''
        # Trainings Dropdown
        # Navigate to Leader Trainings
    def test_nav_to_leader_trainings(self):
        self.browser = Trainings_Softskill(self.browser)

        self.browser.nav_to_leader_trainings()


    def test_get_trainings_softskill_leader_trainings_title(self):
        self.browser = Trainings_Softskill_Leader_Trainings(self.browser)

        title = self.browser.get_trainings_softskill_leader_trainings_title(Testdata.TRAININGS_SOFTSKILL_LEADER_TITLE)

        assert title == Testdata.TRAININGS_SOFTSKILL_LEADER_TITLE

    def test_nav_back1(self):
        self.browser = Trainings_Softskill_Leader_Trainings(self.browser)

        self.browser.go_back()




        # Navigate to Salesforce Trainings
    def test_nav_to_salesforce_trainings(self):
        self.browser = Trainings_Softskill(self.browser)

        self.browser.nav_to_salesforce_trainings()


    def test_get_trainings_softskill_salesforce_trainings_title(self):
        self.browser = Trainings_Softskill_Salesforce_Trainings(self.browser)

        title = self.browser.get_trainings_softskill_salesforce_trainings_title(Testdata.TRAININGS_SOFTSKILL_SALESFORCE_TITLE)

        assert title == Testdata.TRAININGS_SOFTSKILL_SALESFORCE_TITLE


    def test_nav_back2(self):
        self.browser = Trainings_Softskill_Salesforce_Trainings(self.browser)
        
        self.browser.go_back()




        # Navigate to Competence Improvement Trainings
    def test_nav_to_competence_improvement_trainings(self):
        self.browser = Trainings_Softskill(self.browser)

        self.browser.nav_to_competence_improvement_trainings()


    def test_get_trainings_softskill_competenve_improvement_trainings_title(self):
        self.browser = Trainings_Softskill_Competence_Improvement_Trainings(self.browser)

        title = self.browser.get_trainings_softskill_competence_improvement_trainings_title(Testdata.TRAININGS_SOFTSKILL_COMPETENCE_TITLE)

        assert title == Testdata.TRAININGS_SOFTSKILL_COMPETENCE_TITLE

    
    def test_nav_back3(self):
        self.browser = Trainings_Softskill_Competence_Improvement_Trainings(self.browser)

        self.browser.go_back()




        # Navigate to Coaching
    def test_nav_to_coaching(self):
        self.browser = Trainings_Softskill(self.browser)

        self.browser.nav_to_coaching()


    def test_get_trainings_softskill_coaching_title(self):
        self.browser = Trainings_Softskill_Coaching(self.browser)

        title = self.browser.get_trainings_softskill_coaching_title(Testdata.TRAININGS_SOFTSKILL_COACHING_TITLE)

        assert title == Testdata.TRAININGS_SOFTSKILL_COACHING_TITLE


    def test_nav_back4(self):
        self.browser = Trainings_Softskill_Coaching(self.browser)

        self.browser.go_back()