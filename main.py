# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's test scripts execution entrance
'''
import unittest
import os
from common.HTMLTestRunner import HTMLTestRunner
from common.dir_config import *

ss = unittest.TestSuite()
loader = unittest.TestLoader()
ss.addTests(loader.discover(testcases_dir))  # add testcases into test suite
# unittest.TestSuite().addTests(unittest.TestLoader().discover(testcases_dir))
with open(htmlreport_dir+"\\autoTest_report.html", 'wb') as fp:
    runner = HTMLTestRunner(
        stream=fp,
        title="Dealertarck's Test Report",
        description='Auto UI Test Coding Session',
    )
    runner.run(ss)


# ss=unittest.TestSuite()
# loader=unittest.TestLoader()
# ss.addTests(loader.discover(testcases_dir))
#
# with open(htmlreport_dir+'\\autotest_report.html','wb') as fp:
#     runner=HTMLTestRunner(
#         stream=fp,
#         verbosity=2, #print the error message for debug
#         title="dfd",
#         description="des",
#     )
#     runner.run(ss)
