# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description:Dealertarck's logger configuration
'''
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from common import dir_config

class Log:
    def __init__(self):
        self.logname = "mylog"

    def setMSG(self, level, msg):
        '''
        description: set message for log
        '''
        logger = logging.getLogger()
        # define the Handler that exports logs to the console and file
        curTime = time.strftime(r"%Y-%m-%d",time.localtime())
        fh = logging.FileHandler(dir_config.logs_dir+"\\Web_Autotest_{0}.log".format(curTime))
        ch = logging.StreamHandler()
        # define the format of the log output
        formater = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(funcName)s [line:%(lineno)d ] %(message)s")
        fh.setFormatter(formater) #logging.Formatter(‘% (name)s – %(lineno)d – %(message)s’)
        ch.setFormatter(formater)
        # add the Handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # add log message, export the log above INFO level
        logger.setLevel(logging.INFO)
        if level=='debug':
            logger.debug(msg)
        elif level=='info':
            logger.info(msg)
        elif level=='warning':
            logger.warning(msg)
        elif level=='error':
            logger.error(msg)
        # remove the handler, otherwise the log will be exported repeatedly
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)