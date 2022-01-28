import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Pages/Navbar/E_Learning')
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from testdata import Testdata
from test_parent import Parent_test
from e_learning import E_Learning
from e_learning_owndev import E_Learning_Owndev
from e_learning_official import E_Learning_Official
from e_learning_unique import E_Learning_Unique
from mentored_courses import Mentored_Courses

class Test_Nav_E_Learning(Parent_test):

    def test_get_e_learning_page_title(self):
        self.browser = E_Learning(self.browser)        
        title = self.browser.get_e_learning_title(Testdata.E_LEARNING_TITLE)
        assert title == Testdata.E_LEARNING_TITLE
    


        ''' Check Elements Exist on Page'''
    def test_hyper_link_owndev_exists(self):
        self.browser = E_Learning(self.browser)

        hyper_link1 = self.browser.hyper_link_owndev_exists()

        assert hyper_link1


    def test_hyper_link_e_learning_lessons_exists(self):
        self.browser = E_Learning(self.browser)

        hyper_link2 = self.browser.hyper_link_e_learning_lessons_exists()

        assert hyper_link2


    def test_hyper_link_official_exists(self):
        self.browser = E_Learning(self.browser)

        hyper_link3 = self.browser.hyper_link_official_exists()

        assert hyper_link3


    def test_hyper_link_mentored_exists(self):
        self.browser = E_Learning(self.browser)

        hyper_link4 = self.browser.hyper_link_mentored_exists()

        assert hyper_link4


    def test_hyper_link_unique_exists(self):
        self.browser = E_Learning(self.browser)

        hyper_link5 = self.browser.hyper_link_unique_exists()

        assert hyper_link5



        ''' Test Navigation & Page Titles Match'''
        # E-Learning/Owndev
    def test_nav_to_e_learning_owndev(self):
        self.browser = E_Learning(self.browser)
        self.browser.nav_to_elearning_owndev()

    
    def test_get_e_learning_owndev_title(self):
        self.browser = E_Learning_Owndev(self.browser)
        
        title = self.browser.get_e_learning_owndev_title(Testdata.E_LEARNING_OWNDEV_TITLE)

        assert title == Testdata.E_LEARNING_OWNDEV_TITLE


    def test_nav_back1(self):
        self.browser = E_Learning_Owndev(self.browser)
        self.browser.go_back()



        # E-Learning/Official
    def test_nav_to_e_learning_official(self):
        self.browser = E_Learning(self.browser)
        self.browser.nav_to_e_learning_official()
    

    def test_get_e_learning_official_title(self):
        self.browser = E_Learning_Official(self.browser)

        title = self.browser.get_e_learning_official_title(Testdata.E_LEARNING_OFFICIAL_TITLE)

        assert title == Testdata.E_LEARNING_OFFICIAL_TITLE
    

    def test_nav_back2(self):
        self.browser = E_Learning_Official(self.browser)
        self.browser.go_back()



        # Mentored Courses
    def test_nav_to_mentored_courses(self):
        self.browser = E_Learning(self.browser)
        self.browser.nav_to_mentored_courses()


    def test_get_mentored_courses_title(self):
        self.browser = Mentored_Courses(self.browser)

        title = self.browser.get_mentored_courses_title(Testdata.MENTORED_COURSES_TITLE)

        assert title == Testdata.MENTORED_COURSES_TITLE

    
    def test_nav_back3(self):
        self.browser = Mentored_Courses(self.browser)
        self.browser.go_back()



        # E-Learning/Unique
    def test_nav_to_e_learning_unique(self):
        self.browser = E_Learning(self.browser)
        self.browser.nav_to_e_learning_unique()


    def test_get_e_learning_unique_title(self):
        self.browser = E_Learning_Unique(self.browser)

        title = self.browser.get_e_learning_unique_title(Testdata.E_LEARNING_UNIQUE_TITLE)

        assert title == Testdata.E_LEARNING_UNIQUE_TITLE

    def test_nav_back4(self):
        self.browser = E_Learning_Unique(self.browser)
        self.browser.go_back()