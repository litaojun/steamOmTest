#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: AlertOperpsnTest.py 
@time: 2018/4/25 18:53 
"""
from steam.admin.operposition.AlertOperpsnService import OperpsnAlertService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
class OperpsnAlertTest(SteamTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/steam-featured/homeConfig/removeIndexConfig-del"
      @initInputService( services = [],
                         curser   = OperpsnAlertService )
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnAlertTest,self).__init__(methodName,param)

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\operpsnalertcase.xlsx",
                    testclse     = OperpsnAlertTest
                 )
