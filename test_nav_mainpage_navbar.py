import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_Trainings_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_Softskill')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_ProjectManagement')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_Trainings_Dropdown/Trainings_Trainings')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/E_Learning')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/E_Learning/E_Learning_Owndev')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/Office_IT')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/Company_Management')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/Career_Start_Program')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Admin')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Developer')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Leader')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/IT_Courses/IT_Courses_Creating_Value')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Exams')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Discounts')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/Career_Start_Program/For_You')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/Navbar_IT_Courses_Dropdown/Career_Start_Program/For_Employers')

sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from testdata import Testdata
from test_parent import Parent_test

from mainpage import MainPage
from course_schedules import Course_Schedules
from discounts import Discounts
from contact import Contact

class Test_Nav_MainPage(Parent_test):
    
    def test_close_popup(self):
        self.browser = MainPage(self.browser)
        
        self.browser.close_popup()
    

    def test_get_main_page_title(self):
        self.browser = MainPage(self.browser)

        title = self.browser.get_main_page_title(Testdata.MAIN_PAGE_TITLE)

        assert title == Testdata.MAIN_PAGE_TITLE




        ''' Test Navigations & Page Titles Match'''
        # Trainings Dropdown
    def test_nav_to_trainings_softskill(self):
        pass
    

    def test_nav_to_trainings_projectmanagement(self):
        pass


    def test_nav_to_trainings_trainings(self):
        pass

    
    def test_nav_to_trainings_softskill_leader_trainings(self):
        pass
    

    def test_nav_to_trainings_softskill_salesforce_trainings(self):
        pass


    def test_nav_to_trainings_softskill_competence_improvement_trainings(self):
        pass


    def test_nav_to_trainings_softskill_coaching(self):
        pass


    def test_nav_to_trainings_projectmanagement_traditional(self):
        pass


    def test_nav_to_trainings_projectmanagement_agile(self):
        pass


    def test_nav_to_trainings_projectmanagement_lean(self):
        pass

    
    def test_nav_to_trainings_trainings_open_trainings_schedule(self):
        pass
    

    def test_nav_to_trainings_trainings_catalogue(self):
        pass
    
        # E-Learning


        # IT-Courses Dropdown


        # Exams Dropdown


        # Course Schedules
    def test_nav_to_course_schedules(self):
        self.browser = MainPage(self.browser)

        self.browser.nav_to_course_schedules()


    def test_get_course_schedules_page_title(self):
        self.browser = Course_Schedules(self.browser)

        title = self.browser.get_course_schedules_page_title(Testdata.COURSE_SCHEDULES_TITLE)

        assert title == Testdata.COURSE_SCHEDULES_TITLE
    

    def test_nav_to_mainpage_from_course_schedules(self):
        self.browser = Course_Schedules(self.browser)    

        self.browser.nav_to_mainpage()



        # Discounts
    def test_nav_to_discounts(self):
        self.browser = MainPage(self.browser)

        self.browser.nav_to_discounts()


    def test_get_discount_page_title(self):
        self.browser = Discounts(self.browser)

        title = self.browser.get_discount_page_title(Testdata.DISCOUNTS_TITLE)

        assert title == Testdata.DISCOUNTS_TITLE
    
    def test_nav_to_mainpage_from_discounts(self):
        self.browser = Discounts(self.browser) 

        self.browser.nav_to_mainpage()



        # Contacts
    def test_nav_to_contacts(self):
        self.browser = MainPage(self.browser)

        self.browser.nav_to_contacts()


    def test_get_contacts_page_title(self):
        self.browser = Contact(self.browser)
        
        title = self.browser.get_contacts_page_title(Testdata.CONTACTS_TITLE)

        assert title == Testdata.CONTACTS_TITLE


    def test_nav_to_mainpage_from_contacts(self):
        self.browser = Contact(self.browser)

        self.browser.nav_to_mainpage()




    