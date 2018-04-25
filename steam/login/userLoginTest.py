#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userLoginTest.py 
@time: 2018/3/2 17:01 
"""
from opg.unit.parametrized import ParametrizedTestCase
import logging
logger = logging.getLogger(__name__)
# logger = logging.getLogger("%s.%s" % ( self.__class__.__name__,"__init__"))
class UserLoginTest(ParametrizedTestCase):
	def __init__(self):
		logger = logging.getLogger("%s.%s" % (self.__class__.__name__, "__init__"))
		logger.info("litaojun")

if __name__ == "__main__":
	ult = UserLoginTest()