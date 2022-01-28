from logging import raiseExceptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException 

from testdata import Testdata
from basemethods import Base_methods

#Pages
from course_schedules import Course_Schedules
from discounts import Discounts
from contact import Contact
from cart import Cart
from login import Login
#from mainpage_it_courses_dropdown import Mainpage_It_Courses_Dropdown


class MainPage(Base_methods):
    
    '''Locators(By.)'''
    to_close_popup = (By.ID,'NewsletterModalCloseButton')


    # Nav Bar Buttons
    main_page_button = (By.XPATH, '//*[@id="navbar"]/div[1]/a/img')
    nav_bar_trainings = (By.ID, 'PrimaryNavTraining')
    nav_bar_e_learning = (By.LINK_TEXT, 'E-learning')
    nav_bar_it_courses = (By.ID, 'PrimaryNavCourses')
    nav_bar_course_schedules = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[5]/a')
    nav_bar_discounts = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[6]/a')
    nav_bar_contacts = (By.XPATH,'//*[@id="PrimaryNavMainMenu"]/li[7]/a')
    nav_bar_cart = (By.XPATH, '//*[@id="navbar"]/div[3]/ul/li[2]/a')
    nav_to_login = (By.XPATH, '//*[@id="navbar"]/div[3]/ul/li[3]/a/i')

    # From Trainings Dropdown Buttons
    btn_trainings = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[3]/h4[1]/a')
    btn_open_training_schedule = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[3]/h4[2]/a')
    btn_training_catalogue = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[3]/h4[3]/a')

    btn_project_management = (By.LINK_TEXT, 'Projektmenedzsment')
    btn_traditional_pm = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[2]/a[1]')
    btn_agile_pm = (By.LINK_TEXT, ' Agilis projekt­menedzsment ')
    btn_lean = (By.LINK_TEXT, ' LEAN ')

    btn_soft_skill = (By.LINK_TEXT, 'Soft skill')
    btn_leader_training = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[1]/a[1]')
    btn_salesforce_training = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[1]/a[2]')
    btn_competence_training = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[1]/div/div/div[1]/a[3]')
    btn_coaching = (By.LINK_TEXT, ' Coaching ')

    # From IT Courses Dropdown Buttons
    btn_it_courses = (By.ID, 'MegaMenuIT') # 1
    btn_it_courses_xpath = (By.XPATH, '//*[@id="MegaMenuIT"]')
    btn_it_courses_admin = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/h4/a') # 1/a
    btn_it_courses_dev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/h4/a')   # 1/b
    btn_leader_courses = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[3]/h4/a')   # 1/c
    btn_creating_value = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[4]/h4/a')   # 1/d
    btn_office = (By.ID, 'MegaMenuOffice')        # 2
    btn_comp_man = (By.ID, 'MegaMenuERP')         # 3
    btn_car_start_p = (By.ID, 'MegaMenuKSP')      # 4/a
    btn_car_fy = (By.LINK_TEXT, 'Neked')           
    btn_for_emp = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/h4/a')           # 4/b

    # 1/a
    btn_it_courses_admin_aws = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[1]')
    btn_it_courses_admin_microsoft = (By.LINK_TEXT, ' Microsoft ')
    btn_it_courses_admin_cisco = (By.LINK_TEXT, ' Cisco ')
    btn_it_courses_admin_oracle = (By.LINK_TEXT, ' Oracle ')
    btn_it_courses_admin_vmware = (By.LINK_TEXT, ' VMware ')
    btn_it_courses_admin_ibm = (By.LINK_TEXT, ' IBM ')
    btn_it_courses_admin_linux = (By.LINK_TEXT, ' Linux ')
    btn_it_courses_admin_other = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[1]/a[8]')

    # 1/b
    btn_it_courses_dev_aws = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[1]')
    btn_it_courses_dev_micr = (By.LINK_TEXT, ' Microsoft (C#, ASP.NET, stb.) ')
    btn_it_courses_dev_java = (By.LINK_TEXT, ' Java ')
    btn_it_courses_dev_webdev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[4]')
    btn_it_courses_dev_mobdev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[5]')
    btn_it_courses_dev_pyth = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[6]')
    btn_it_courses_dev_other = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[2]/a[7]')

    # 1/c
    btn_leader_courses_itil = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[3]/a[1]')
    btn_leader_courses_risk = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[3]/a[2]')
    btn_leader_courses_busn_an = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[1]/div/div[3]/a[3]')

    # 1/d
    btn_creating_value_agile = (By.LINK_TEXT, ' Agilis ')
    btn_creating_value_devops = (By.LINK_TEXT, ' DevOps ')

    # 2
    btn_office_mo = (By.LINK_TEXT, ' Microsoft Office ')
    btn_office_mo365 = (By.LINK_TEXT, ' Microsoft Office 365 ')
    btn_office_da = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[2]/div/div/a[3]')
    btn_office_gwc = (By.LINK_TEXT, ' Google Workspace tanfolyamok ')

    # 3
    btn_comp_man_sap = (By.LINK_TEXT, ' SAP tanfolyamok ')
    btn_comp_man_sfc = (By.LINK_TEXT, ' Salesforce tanfolyamok ')

    # 4/a
    btn_car_fy_jun_dev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[1]')
    btn_car_fy_app_ad = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[2]')
    btn_car_fy_soft_test = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[3]')
    btn_car_fy_hir_proc = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[4]')
    btn_car_fy_apply = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[1]/a[5]')
    btn_car_fy_faq = (By.LINK_TEXT, ' GYIK ')

    # 4/b
    btn_for_emp_prog = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[1]')
    btn_for_emp_jun_dev = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[2]')
    btn_for_emp_fin = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[3]')
    btn_for_emp_select = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[4]')
    btn_for_emp_grnt = (By.XPATH, '//*[@id="PrimaryNavMainMenu"]/li[3]/div/div/div[2]/div[4]/div/div[2]/a[5]')


    '''Bottom Page Buttons'''
    # 1st Column
    btn_apply = (By.XPATH, '/html/body/footer/nav/div/div/div[1]/ul/li[1]/a/span')
    btn_gen_course_grt_cond = (By.XPATH, '/html/body/footer/nav/div/div/div[1]/ul/li[2]/a/span')
    btn_online_service_cond = (By.XPATH, '/html/body/footer/nav/div/div/div[1]/ul/li[3]/a/span')
    btn_proms_and_discounts = (By.XPATH, '/html/body/footer/nav/div/div/div[1]/ul/li[4]/a/span')
    # 2nd Column
    btn_news = (By.XPATH, '/html/body/footer/nav/div/div/div[2]/ul/li[1]/a/span')
    btn_careers = (By.XPATH, '/html/body/footer/nav/div/div/div[2]/ul/li[2]/a/span')
    btn_about_us = (By.XPATH, '/html/body/footer/nav/div/div/div[2]/ul/li[3]/a/span')
    btn_impressum = (By.XPATH, '/html/body/footer/nav/div/div/div[2]/ul/li[4]/a/span')
    # 3rd Column
    btn_lvc = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[1]/a/span')
    btn_mentored_courses = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[2]/a/span')
    btn_edu_advice = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[3]/a/span')
    btn_pre_asess = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[4]/a/span')
    btn_unique_edu_services = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[5]/a/span')
    btn_accomodations = (By.XPATH, '/html/body/footer/nav/div/div/div[3]/ul/li[6]/a/span')
    # 4th Column
    btn_privacy_inf = (By.XPATH, '/html/body/footer/nav/div/div/div[4]/ul/li[1]/a/span')
    btn_busn_policies = (By.XPATH, '/html/body/footer/nav/div/div/div[4]/ul/li[2]/a/span')
    btn_adult_tutor_laws = (By.XPATH, '/html/body/footer/nav/div/div/div[4]/ul/li[3]/a/span')
    btn_about_tenders = (By.XPATH, '/html/body/footer/nav/div/div/div[4]/ul/li[4]/a/span')
    # 5th Column
    btn_phone_skype = (By.XPATH, '/html/body/footer/nav/div/div/div[5]/ul/li[1]/a/span[2]')
    btn_email = (By.XPATH, '/html/body/footer/nav/div/div/div[5]/ul/li[2]/a/span[2]')
    btn_map_addr = (By.XPATH, '/html/body/footer/nav/div/div/div[5]/ul/li[4]/a/address')
    # 6th Column
    btn_fb = (By.XPATH, '')
    btn_linkedin = (By.XPATH, '')
    btn_spotify = (By.XPATH, '')
    btn_callback = (By.XPATH, '')
    btn_subscribe = (By.XPATH, '')
    # The Bottom Bottom
    btn_certificate1 = (By.XPATH, '')
    btn_certificate2 = (By.XPATH, '')

    '''Constructor of the Parent class'''
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(Testdata.URL)
        

    '''MainPage actions'''
    def get_main_page_title(self, title):
        return self.get_title(title)


    def close_popup(self):
        try:
            self.do_click(self.to_close_popup)

        except TimeoutException:
            print('No popup found.')
            pass


    def search_from_main(self):
        pass

    
    '''Navigation from Trainings Dropdown Bar'''
    # Trainings
    def nav_to_trainings(self):
        self.do_click(self.nav_bar_trainings)
        pass

    def nav_to_trainings_open_trainings_schedule(self):
        self.do_click(self.nav_bar_trainings)
        pass


    def nav_to_trainings_training_catalogue(self):
        self.do_click(self.nav_bar_trainings)
        pass

    # Project Management
    def nav_to_trainings_projectmanagement(self):
        self.do_click(self.nav_bar_trainings)
        pass


    def nav_to_trainings_projectmanagement_traditional(self):
        self.do_click(self.nav_bar_trainings)
        pass


    def nav_to_trainings_projectmanagement_agile(self):
        self.do_click(self.nav_bar_trainings)
        pass


    def nav_to_trainings_projectmanagement_lean(self):
        self.do_click(self.nav_bar_trainings)
        pass


    # Soft Skill
    def nav_to_softskill(self):
        self.do_click(self.nav_bar_trainings)
        pass
    

    def nav_to_softskill_leader_trainings(self):
        self.do_click(self.nav_bar_trainings)
        pass


    def nav_to_softskill_salesforce_trainings(self):
        self.do_click(self.nav_bar_trainings)
        pass


    def nav_to_softskill_competence_improvement(self):
        self.do_click(self.nav_bar_trainings)
        pass


    def nav_to_softskill_coaching(self):
        self.do_click(self.nav_bar_trainings)
        pass


    ''' Navigation from IT Courses Dropdown Navigation Bar'''
    # IT Courses
    def nav_to_navbar_it_courses(self):
        self.do_click(self.nav_bar_it_courses)

    
    # IT Courses/Admin
    def nav_to_it_courses_admin(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_aws(self):
        self.do_click(self.nav_bar_it_courses)
        pass
    

    def nav_to_it_courses_admin_microsoft(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_cisco(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_oracle(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_vmware(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_ibm(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_linux(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_admin_other(self):
        self.do_click(self.nav_bar_it_courses)
        pass

    
    # IT Courses/Developer
    def nav_to_it_courses_developer(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_aws(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_microsoft(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_java(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_webdev(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_mobile(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_python(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_developer_other(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    # IT Courses/Leader
    def nav_to_it_courses_leader(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_leader_itil_princ2(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_leader_risk_management_inf_security_importer_management(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_leader_business_analyst(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    # IT Courses/Creating Value
    def nav_to_it_courses_creating_value(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_creating_value_agile(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_it_courses_creating_value_devops(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    # Office IT
    def nav_to_office_it(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_office_it_microsoft_office(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_office_it_microsoft_office_365(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_office_it_dataanalyst_courses(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_office_it_workspace_courses(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    # Company Management
    def nav_to_company_management(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_company_management_sap_courses(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_company_management_salesforce_courses(self):
        self.do_click(self.nav_bar_it_courses)
        pass

    
    # Career Start Program/For You
    def nav_to_career_start_program_for_you(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_junior_dev_course(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_application_admin(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_software_tester(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_hiring_process(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_applying(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_you_faq(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    # Career Start Program/For Employers
    def nav_to_career_start_program_for_employers(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_employers_about_the_program(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_employers_what_a_junior_knows(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_employers_fin_and_emp_modell(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    def nav_to_career_start_program_for_employers_guarantee(self):
        self.do_click(self.nav_bar_it_courses)
        pass


    '''Navigation from rest of the Navigation Bar'''
    # Course Schedules
    def nav_to_course_schedules(self):
        self.do_click(self.nav_bar_course_schedules)

        return Course_Schedules(self.browser)

    # Discounts
    def nav_to_discounts(self):
        self.do_click(self.nav_bar_discounts)
        
        return Discounts(self.browser)
    
    # Contacts
    def nav_to_contacts(self):       
        self.do_click(self.nav_bar_contacts)

        return Contact(self.browser) 

    # Cart
    def nav_to_cart(self):
        self.do_click(self.nav_bar_cart)
        
        return Cart(self.browser)
    
    # Login
    def nav_to_login(self):
        self.do_click(self.nav_to_login)
        return Login(self.browser)

    '''Bottom Page Navigations'''
    def nav_to_news(self):
        self.do_click(self.nav_bar_news)

        return News(self.browser)


    def nav_to_(self):
        pass

    
    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass


    def nav_to_(self):
        pass

    '''def nav_to_message_form(self):
        
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath('/html/body/main/div/div[1]/div/div[1]/div[2]/button'))

        return Popupobj(self.browser)
        #self.do_click(self.message_btn1)

        button = self.browser.find_element_by_xpath('//*[@id="sendMessage_submit"]')

        ActionChains(self.browser).move_to_element(button).click(button).perform()
        
        
    def fill_data_form(self, name, email, message):
        
        self.do_send_keys(self.name_input, name)
        
        self.do_send_keys(self.email_input, email)
        
        self.do_send_keys(self.msg_box_input, message)

        self.do_click(self.ticker)'''
