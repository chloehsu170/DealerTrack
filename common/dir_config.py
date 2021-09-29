# /!/usr/bin/python3
# coding:utf-8
__author__ = "Yanwen Xu"
"""
description:Dealertarck's dir configuration
"""

import os
import sys

syspath = sys.path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# base_dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# sys.path.app
# end(base_dir)
base_dir = base_dir.replace("\\", "/")
syspath.append(base_dir)
print("base_dir", syspath)
testdatas_dir = os.path.join(base_dir, "TestDatas")
testcases_dir = os.path.join(base_dir, "TestCases")
htmlreport_dir = os.path.join(base_dir, "Outputs\\report")
logs_dir = os.path.join(base_dir, "Outputs\\logs")
screenshot_dir = os.path.join(base_dir, "Outputs\\screenshots")
print("base_dir", testdatas_dir)
