# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's third page object
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.third_page_locator import ThirdPageLocator as loc
from common.basepage import BasePage

class ThirdPage(BasePage):

    def multiply(self, first, second):
        '''
        description: input first number and second number of the multiply 
        '''
        # waiting for the element
        self.wait_eleVisible(loc.first_number_loc)
        # input text
        self.input_text(first, "input the first number in the third page", loc.first_number_loc)
        # waiting for the element
        self.wait_eleVisible(loc.second_number_loc)
        # input text
        self.input_text(second, "input the first number in the third page", loc.second_number_loc)
        self.click("click multiply button",loc.multiply_button_loc)
    
    def get_resultOfMultiply(self):
        '''
        description: get result of Multiply
        '''
        self.wait_eleVisible(loc.result_of_multiply_loc)
        return self.get_element_attr_value("get result of Multiply", loc.result_of_multiply_loc)
    
    def click_first_page_link(self):
        '''
        description: click first page link
        '''
        self.click("first page link loc", loc.first_page_link_loc)

    def click_pop_up_window(self):
        '''
        description: click the pop up window
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
        description: check the third page
        '''
        # import time
        # time.sleep(2)
        self.wait_eleVisible(loc.third_page_text_loc)
        try:
            self.driver.find_element(loc.third_page_text_loc)
        except Exception as e:
            return e
        else:
            return self.get_element_text("get_element_text", loc.third_page_text_loc)

    def click_home_link(self):
        '''
        description: check the home link
        '''
        self.click("home link loc", loc.home_link_loc)

    def click_news_link(self):
        '''
        description: check the news link
        '''
        self.click("news link loc", loc.news_link_loc)

    def click_contact_link(self):
        '''
        description: check the contact link
        '''
        self.click("contact link loc", loc.contact_link_loc)

    def click_help_link(self):
        '''
        description: check the help link
        '''
        self.click("help link loc", loc.help_link_loc)
