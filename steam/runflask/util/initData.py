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
from opg.unit.flaskRunMgr import getRunTestTokenId,initAllTestCase,initAllTestClass,genAllTestCase,runAllTestCase
from steam.mockhttp.util.initFile import casepath
sign = True
testSuite = None
if sign :
    allTestClass = initAllTestClass()
    allTestCase  = initAllTestCase( casePath   = casepath )
    testSuite    = genAllTestCase( allCase      = allTestCase ,
                                  allTestClass  = allTestClass )
    tokenList    = []
    sign         = False