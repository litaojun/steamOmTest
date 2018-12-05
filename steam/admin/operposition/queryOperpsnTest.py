#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryOperpsnTest.py 
@time: 2018/4/25 19:24 
"""
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.operposition.queryOperpsnService import OperpsnQueryService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
class OperpsnQueryTest(SteamTestCase):
      '''
            admin删除分类
      '''
      __interfaceName__ = "/steam-featured/homeConfig/listData"
      @initInputService(services=OperpsnQueryService)
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnQueryTest,self).__init__(methodName,param)


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\operpsnquerycase.xlsx",
                    testclse = OperpsnQueryTest
                 )