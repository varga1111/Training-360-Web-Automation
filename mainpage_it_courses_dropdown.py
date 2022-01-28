import sys
sys.path.insert(0, '/Users/openmindschooling/MyStuff/Web/Training360/Automated Tests (Selenium Python)/Configs')

from basemethods import Base_methods

from selenium.webdriver.common.by import By


class Mainpage_It_Courses_Dropdown(Base_methods):
    
    ''' By Locators'''
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

    def __init__(self, browser): 
        super().__init__(browser)

    
    ''' Hovers '''

    def hover_to_btn_it_courses(self):
        self.hover(self.browser.find_element_by_id('MegaMenuIT'))


    def hover_to_btn_office_it(self):
        self.hover(self.browser.find_element_by_id('MegaMenuOffice'))


    def hover_to_btn_to_comp_man(self):
        self.hover(self.browser.find_element_by_id('MegaMenuERP'))


    def hover_to_btn_career_start_programs(self):
        self.hover(self.browser.find_element_by_id('MegaMenuKSP'))


    ''' Is Visible ''' 
    # 1st Column
    def btn_it_courses_exists(self):
        pass

    
    def btn_office_exists(self):
        pass


    def btn_comp_man_exists(self):
        pass


    def btn_car_start_p_exists(self):
        pass



    # 1/a Columns
    def btn_it_courses_admin_exists(self):
        pass


    def btn_it_courses_admin_aws_exists(self):
        pass


    def btn_leader_courses_exists(self):
        pass


    def btn_creating_value_exists(self):
        pass


    def btn_it_courses_admin_microsoft_exists(self):
        pass


    def btn_it_courses_admin_cisco_exists(self):
        pass


    def btn_it_courses_admin_oracle_exists(self):
        pass


    def btn_it_courses_admin_vmware_exists(self):
        pass


    def btn_it_courses_admin_ibm_exists(self):
        pass


    def btn_it_courses_admin_linux_exists(self):
        pass


    def btn_it_courses_admin_other_exists(self):
        pass

    # 1 / b Coluns
    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass


    def _exists(self):
        pass




    