# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's first page object
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.first_page_locator import FirstPageLocator as loc
from common.basepage import BasePage

class FirstPage(BasePage):
    def check_user_ele_exists(self):
        '''
        description:check the page message
        '''
        # WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(loc.loginArea_loc))

        # try:
        #     self.driver.find_element(loc.loginArea_loc)
        # except Exception as e:
        #     return e
        # else:
        #     return self.get_element_text("check the login message", loc.loginArea_loc)
        self.wait_eleVisible(loc.loginArea_loc)
        return self.get_element_text("check the page message",loc.loginArea_loc)

    def addition(self, first, second):
        '''
        description: input first number and second number of the addition 
        '''
        # waiting for the element
        # WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located(loc.first_number_loc))
        # print('element showd up:',*loc.first_number_loc)
        self.wait_eleVisible(loc.first_number_loc)
        # input text
        self.input_text(first,"input first number in the first page",loc.first_number_loc)
        # waiting for the element
        self.wait_eleVisible(loc.second_number_loc)
        # input text
        self.input_text(second,"input second number in the first page",loc.second_number_loc)
        self.click("click addition button",loc.add_button_loc)

    def login(self,username):
        '''
        description: check the login function
        '''
        # waiting for the element
        self.wait_eleVisible(loc.user_loc)
        # input text
        self.input_text(username,"first page input username",loc.user_loc)
        self.click("click login button",loc.login_button_loc)
    
    def get_loginName(self):
        '''
        description: get login name
        '''
        self.wait_eleVisible(loc.loginArea_loc)
        return self.get_element_text("get login name",loc.loginArea_loc)
    
    def get_resultOfAddition(self):
        '''
        description: get result of addition
        '''
        self.wait_eleVisible(loc.result_of_addition_loc)
        return self.get_element_attr_value("get result of addition",loc.result_of_addition_loc)
    
    def get_errorMsg(self):
        '''
        description: get login error message
        '''
        #accept the alert info
        try:
            alert = self.driver.switch_to_alert()
            message = alert.text
            alert.accept()
            return message
        except:
            pass

    # def get_error_pageMsg(self):
    #     WebDriverWait(self.driver,30,0.1).until(EC.visibility_of_element_located(loc.pageCenter_loc))
    #     return self.driver.find_element(loc.pageCenter_loc).text

    def click_second_page_link(self):
        '''
        description: click second page link

        '''
        self.click("second_page_link_loc", loc.second_page_link_loc)
