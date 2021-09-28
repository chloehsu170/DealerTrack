# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's third page test script
'''
from selenium import webdriver
import unittest
import ddt
from PageObjects.third_page import ThirdPage
from PageObjects.first_page import FirstPage
from TestDatas import Global_Datas as gd
from TestDatas import third_page_datas as tpd

@ddt.ddt
class TestThird(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.get(gd.third_page)
        cls.tp=ThirdPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def tearDown(self) -> None:
        self.driver.refresh()

    @ddt.data(*tpd.success_numbers)
    def test_001_multiply_success(self,data):
        """positive cases of multiply"""
        self.tp.multiply(data["first_number"],data["second_number"])
        self.assertEqual(self.tp.get_resultOfMultiply(),str(data['check']))

    @ddt.data(*tpd.wrong_numbers)
    def test_002_multiply_wrong(self,data):
        """negative cases of multiply"""
        self.tp.multiply(data["first_number"],data["second_number"])
        self.assertEqual(self.tp.get_resultOfMultiply(),str(data['check']))

    def test_004_link_success(self):
        """check the first page link"""
        self.tp.click_first_page_link()
        self.assertTrue(FirstPage(self.driver).check_user_ele_exists())
    
    def test_003_pop_up_message(self):
        """check pop up message"""
        text=self.tp.click_pop_up_window()
        self.assertIn('This is a popup.', text)

   

