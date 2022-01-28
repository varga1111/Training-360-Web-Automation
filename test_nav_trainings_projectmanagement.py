import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_ProjectManagement')

from testdata import Testdata
from test_parent import Parent_test

from trainings_projectmanagement import Trainings_Projectmanagement
from trainings_projectmanagement_traditional import Trainings_Projectmanagement_Traditional
from trainings_projectmanagement_agile import Trainings_Projectmanagement_Agile
from trainings_projectmanagement_lean import Trainings_Projectmanagement_Lean


class Test_Nav_Trainings_Projectmanagement(Parent_test):
    
    def test_get_trainings_projectmanagement_title(self):
        self.browser = Trainings_Projectmanagement(self.browser)

        title = self.browser.get_trainings_projectmanagement_title(Testdata.TRAININGS_PROJECTMANAGEMENT_TITLE)

        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_TITLE


        # Check Trainings/Projectmanagement Page Elements Exist
    def test_btn_projectmanagement_traditional_exists(self):
        self.browser = Trainings_Projectmanagement(self.browser)
        self.browser.btn_projectmanagement_traditional_exists()
        

    def test_btn_projectmanagement_agile_exists(self):
        self.browser = Trainings_Projectmanagement(self.browser)
        self.browser.btn_projectmanagement_agile_exists()


    def test_btn_projectmanagement_lean_exists(self):
        self.browser = Trainings_Projectmanagement(self.browser)
        self.browser.btn_projectmanagement_lean_exists()


 

        ''' Test Navigations & Page Titles Match & Elements Exist'''
        # Trainings Dropdown
        # Navigate to Projectmanagement/Traditional Page
    def test_nav_to_projectmanagement_traditional(self):
        self.browser = Trainings_Projectmanagement(self.browser)

        self.browser.nav_to_projectmanagement_traditional()


    def test_get_projectmanagement_traditional_title(self):
        self.browser = Trainings_Projectmanagement_Traditional(self.browser)

        title = self.browser.get_trainings_projectmanagement_traditional_title(Testdata.TRAININGS_PROJECTMANAGEMENT_TRADITIONAL_TITLE)

        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_TRADITIONAL_TITLE

    def test_nav_back1(self):
        self.browser = Trainings_Projectmanagement_Traditional(self.browser)

        self.browser.go_back()




        # Navigate to Projectmanagement/Agile Page
    def test_nav_to_projectmanagement_agile(self):
        self.browser = Trainings_Projectmanagement(self.browser)

        self.browser.nav_to_projectmanagement_agile()


    def test_get_projectmanagement_agile_title(self):
        self.browser = Trainings_Projectmanagement_Agile(self.browser)

        title = self.browser.get_trainings_projectmanagement_agile_title(Testdata.TRAININGS_PROJECTMANAGEMENT_AGILE_TITLE)

        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_AGILE_TITLE


    def test_nav_back2(self):
        self.browser = Trainings_Projectmanagement_Agile(self.browser)
        
        self.browser.go_back()




        # Navigate to Projectmanagement/Lean Page
    def test_nav_to_projectmanagement_lean(self):
        self.browser = Trainings_Projectmanagement(self.browser)

        self.browser.nav_to_projectmanagement_lean()


    def test_get_projectmanagement_lean_title(self):
        self.browser = Trainings_Projectmanagement_Lean(self.browser)

        title = self.browser.get_trainings_projectmanagement_lean_title(Testdata.TRAININGS_PROJECTMANAGEMENT_LEAN_TITLE)

        assert title == Testdata.TRAININGS_PROJECTMANAGEMENT_LEAN_TITLE

    
    def test_nav_back3(self):
        self.browser = Trainings_Projectmanagement_Lean(self.browser)

        self.browser.go_back()


