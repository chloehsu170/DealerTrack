# /!/usr/bin/python3
# coding:utf-8
__author__ = "Yanwen Xu"
"""
description:Dealertarck's first page test script
"""
from selenium import webdriver
import unittest
import ddt
from PageObjects.first_page import FirstPage
from PageObjects.second_page import SecondPage
from TestDatas import Global_Datas as gd
from TestDatas import first_page_datas as fpd
from common.dir_config import *
from selenium.webdriver.chrome.options import Options


@ddt.ddt
class TestFirst(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        chrome_options = Options()
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless")
        # chrome_options.headless = True # also works
        cls.driver = webdriver.Chrome(options=chrome_options)
        # cls.driver = webdriver.PhantomJS(base_dir)
        cls.driver.get(gd.first_page)
        cls.fp = FirstPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()

    def test_001_login_guest(self):
        """check original login message"""
        self.assertEqual(self.fp.get_loginName(), "guest")

    @ddt.data(*fpd.success)
    def test_002_login_success(self, data):
        """positive cases of login"""
        self.fp.login(data["user"])
        self.assertEqual(self.fp.get_loginName(), str(data["user"]).strip())

    @ddt.data(*fpd.wrong_datas)
    def test_003_login_negative(self, data):
        """negative cases of login"""
        self.fp.login(data["user"])
        self.assertEqual(
            self.fp.get_errorMsg(), "Username is empty. Please enter user."
        )


@ddt.data(*fpd.success_numbers)
def test_004_addition_success(self, data):
    """positive cases of addition"""
    self.fp.addition(data["first_number"], data["second_number"])
    self.assertEqual(self.fp.get_resultOfAddition(), str(data["check"]))


@ddt.data(*fpd.wrong_numbers)
def test_005_addition_wrong(self, data):
    """negative cases of addition"""
    self.fp.addition(data["first_number"], data["second_number"])
    self.assertEqual(self.fp.get_resultOfAddition(), str(data["check"]))


def test_006_link_success(self):
    """check the second page link"""
    self.fp.click_second_page_link()
    self.assertTrue(SecondPage(self.driver).check_user_ele_exists())
