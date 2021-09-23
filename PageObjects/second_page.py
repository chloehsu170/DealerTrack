# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's second page object
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.second_page_locator import SecondPageLocator as loc
from common.basepage import BasePage

class SecondPage(BasePage):
    def substract(self, first, second):
        '''
        description: input first number and second number of the substract 
        '''
        # waiting for the element
        self.wait_eleVisible(loc.first_number_loc)
        # input text
        self.input_text(first, "input the first number in the second page", loc.first_number_loc)
        # waiting for the element
        self.wait_eleVisible(loc.second_number_loc)
        # input text
        self.input_text(second,"input the second number in the second page",loc.second_number_loc)
        self.click("click substract button", loc.substract_button_loc)
    
    def get_resultOfSubstract(self,value):
        '''
        description: get result of Substract
        '''
        return self.wait_valueVisible(value,loc.result_of_substract_loc)
        # import time
        # time.sleep(2)
        # return self.get_element_attr_value("get result of Substract", loc.result_of_substract_loc)
    
    def click_third_page_link(self):
        '''
        description: check third page link
        '''
        self.click("third page link loc", loc.third_page_link_loc)

    def click_pop_up_window(self):
        '''
        description:check the pop up window
        '''
        self.click("click pop-up window", loc.pop_up_window_button_loc)
        #accept the alert info
        try:
            alert = self.driver.switch_to_alert()
            message = alert.text
            alert.accept()
            return message
        except:
            pass
        
    def check_user_ele_exists(self):
        '''
        description: see if it is the second page
        '''
        self.wait_eleVisible(loc.second_page_text_loc)
        try:
            self.driver.find_element(loc.second_page_text_loc)
        except Exception as e:
            return e
        else:
            return self.get_element_text("get_element_text", loc.second_page_text_loc)
