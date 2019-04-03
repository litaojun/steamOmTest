#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: initData.py 
@time: 2018/10/25 17:28 
"""
from opg.unit.loader import initAllTestCase,initAllTestClass,genAllTestCase
# from steam.mockhttp.util.initFile import casepath
from steam.util.configIni import casepath
sign      = True
testSuite = None
if sign :
    allTestClass = initAllTestClass()
    allTestCase  = initAllTestCase( casePath     = casepath )
    tokenList    = []
    sign         = False