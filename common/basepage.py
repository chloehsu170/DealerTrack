# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's base page 
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import logger
import time
from common.dir_config import screenshot_dir

class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver=driver
        self.mylog = logger.log()

    def wait_eleVisible(self,loc):
        '''
        description: wait until the element is visible
        '''
        start = time.time()
        try:
            # WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located(loc))
            WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(loc))#visibility_of_element_located
            print('visible or not')
        except:
            self.mylog.error("wait until the element {} is visible, but time is out！".format(loc))
            raise
        else:
            end = time.time()
            duration = end-start
            self.mylog.info("wait {} until the element {} is visible".format(duration,loc))

    def wait_valueVisible(self,value,loc):
        '''
        description: wait until the element's value is visible
        '''
        start = time.time()
        try:
            WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element_value(loc,value,))#visibility_of_element_located
        except:
            self.mylog.error("wait until the element {}'s value is visible, but time is out！".format(loc))
            return False
        else:
            end = time.time()
            duration = end-start
            self.mylog.info("wait {} until the element {}'s value is visible".format(duration,loc))
            return True


    def get_element(self,doc,loc):
        '''
        description: find the element's locator
        '''
        try:
            # print((223,loc),*loc)
            return self.driver.find_element(*loc)
        except:
            self.mylog.error("fail to find the element: {}".format(loc))
            self.save_img(doc)
            raise
        else:
            self.mylog.info("succeed to find the element: {} of {}".format(doc,loc))

    def input_text(self,value,doc,loc):
        '''
        description: input the text into the element
        '''
        self.wait_eleVisible(loc)
        ele = self.get_element(doc,loc)
        try:
            ele.clear()
            if value == 'Keys.SPACE':
                ele.send_keys(Keys.SPACE)
            elif value == 'Keys.TAB':
                ele.send_keys(Keys.TAB)
            else:
                ele.send_keys(value)
        except:
            self.mylog.error("fail to input {} into the element: {}".format(value,loc))
            self.save_img(doc)
            raise
        else:
            self.mylog.info("succeed to input {} into the element: {}".format(value,loc))

    def click(self,doc,loc):
        '''
        description: click the element
        '''
        self.wait_eleVisible(loc)
        # ele=self.get_element(loc,doc)
        try:
            self.get_element(doc,loc).click()
        except:
            self.mylog.error("fail to click the element: {}".format(loc))
            self.save_img(doc)
            raise
        else:
            self.mylog.info("succeed to click the element: {}".format(loc))

    def get_element_text(self,doc,loc):
        '''
        description: get element's text
        '''
        self.wait_eleVisible(loc)
        # ele=self.get_element(loc,doc)
        try:
            return self.get_element(doc,loc).text
        except:
            self.mylog.error("fail to click the element: {}".format(loc))
            self.save_img(doc)
            raise
        else:
            self.mylog.info("succeed to click the element: {}".format(loc))

    def get_element_attr_value(self,doc,loc):
        '''
        description: get element's attribute value
        '''
        self.wait_eleVisible(loc)
        try:
            return self.get_element(doc,loc).get_attribute('value')
        except:
            self.mylog.error("fail to click the element: {}".format(loc))
            self.save_img(doc)
            raise
        else:
            self.mylog.info("succeed to click the element: {}".format(loc))

    # def switch_frame(self,locator,timeout):
    #     try:
    #         WebDriverWait(self.driver,timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))
    #     except:
    #         pass

    # def switch_window(self,index):
    #     if index == "new":
    #         pass
    #     elif index == "main":
    #         pass
    #     else:
    #         pass

    def save_img(self,doc=""):
        '''
        description: save the image of the screenshot
        '''
        cur_time = ""
        file = screenshot_dir+"/{}_{}.png".format(doc,cur_time)
        try:
            self.driver.save_screenshot(file)
        except:
            self.mylog.error("fail to take a screenshot")
        else:
            self.mylog.info("succeed to take a screenshot which is saved in the path: {}".format(file))