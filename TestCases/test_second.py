# # /!/usr/bin/python3
# # coding:utf-8
# __author__ = 'Yanwen Xu'
# '''
# description:Dealertarck's second page test script
# '''
# from selenium import webdriver
# import unittest
# import ddt
# from PageObjects.third_page import ThirdPage
# from PageObjects.second_page import SecondPage
# from TestDatas import Global_Datas as gd
# from TestDatas import second_page_datas as spd


# @ddt.ddt
# class TestSecond(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.driver=webdriver.Chrome()
#         cls.driver.get(gd.second_page)
#         cls.sp=SecondPage(cls.driver)

#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.driver.quit()

#     def tearDown(self) -> None:
#         self.driver.refresh()

#     @ddt.data(*spd.success_numbers)
#     def test_001_substract_success(self,data):
#         """positive cases of substract"""
#         self.sp.substract(data["first_number"],data["second_number"])
#         self.assertTrue(self.sp.get_resultOfSubstract(str(data['check'])))

#     @ddt.data(*spd.wrong_numbers)
#     def test_002_substract_wrong(self,data):
#         """negative cases of substract"""
#         self.sp.substract(data["first_number"],data["second_number"])
#         self.assertTrue(self.sp.get_resultOfSubstract(str(data['check'])))

#     def test_003_pop_up_message(self):
#         """check pop up message"""
#         text=self.sp.click_pop_up_window()
#         self.assertIn('This is a popup.', text)

#     def test_004_link_success(self):
#         """check the third page link"""
#         self.sp.click_third_page_link()
#         self.assertTrue(ThirdPage(self.driver).check_user_ele_exists())
    

