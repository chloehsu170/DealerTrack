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

s=unittest.TestSuite()
loader=unittest.TestLoader()
s.addTests(loader.discover(testcases_dir))
with open(htmlreport_dir+"\\autoTest_report.html",'wb') as fp:
    runner=HTMLTestRunner(
        stream=fp,
        title="Dealertarck's Test Report",
        description='Auto UI Test Coding Session',
    )
    runner.run(s)