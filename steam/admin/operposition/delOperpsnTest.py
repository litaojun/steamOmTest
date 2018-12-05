#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: delOperpsnTest.py 
@time: 2018/4/25 19:20 
"""
from steam.admin.classify.delClassifyService import ClassfiyDelService
from steam.admin.operposition.delOperpsnService import OperpsnDelService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
class OperpsnDelTest(SteamTestCase):
      '''
            admin删除分类
      '''
      __interfaceName__ = "/steam-featured/homeConfig/removeIndexConfig"

      @initInputService(services = [],
                        curser   = OperpsnDelService)
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnDelTest,self).__init__(methodName,param)

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\operpsnalertcase.xlsx",
                    testclse = OperpsnDelTest
                 )

