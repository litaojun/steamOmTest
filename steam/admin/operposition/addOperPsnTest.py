#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: addOperPsnTest.py 
@time: 2018/4/25 18:14 
"""
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.operposition.addOperPsnService import OperpsnAddService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
class OperpsnAddTest(SteamTestCase):
      '''
            admin新增首页配置
      '''
      __interfaceName__ = "/operation-manage/featured/createConfig"
      @initInputService(services = [],
                        curser   = OperpsnAddService)
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(OperpsnAddTest,self).__init__(methodName,param)


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\steam-featuredhomeConfigcreateConfigs.yml",
                    testclse = OperpsnAddTest
                 )