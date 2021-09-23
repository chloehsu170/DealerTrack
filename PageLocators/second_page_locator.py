# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's second page locator
'''
from selenium.webdriver.common.by import By

class SecondPageLocator:
    second_page_text_loc = (By.ID,"header")
    first_number_loc = (By.ID,'minuend')
    second_number_loc = (By.ID,'subtrahend')
    result_of_substract_loc = (By.ID,'difference')
    substract_button_loc = (By.ID,'subtractionButton')
    third_page_link_loc = (By.LINK_TEXT,'Go to third page.')
    pop_up_window_button_loc = (By.ID,"popupButton")

