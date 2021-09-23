# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's first page locator
'''
from selenium.webdriver.common.by import By

class FirstPageLocator:
    first_page_text_loc = (By.ID,"header")
    user_loc = (By.ID,'userName')
    login_button_loc = (By.ID,'loginButton')
    loginArea_loc = (By.ID,'loggedInUser') #p
    first_number_loc = (By.ID,'addend1')
    second_number_loc = (By.ID,'addend2')
    result_of_addition_loc = (By.ID,'sum')
    add_button_loc = (By.ID,'additionButton')
    second_page_link_loc = (By.LINK_TEXT,'Go to second page.')