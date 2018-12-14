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
from steam.admin.operposition.delOperpsnService import OperpsnDelService
from steam.admin.operposition.queryOperpsnService import OperpsnQueryService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
class OperpsnAddTest(SteamTestCase):
      '''
            admin新增首页配置
      '''
      __interfaceName__ = "/operation-manage/featured/createConfig"
      @initInputService( services = [ OperpsnDelService ,OperpsnQueryService ] ,
                         curser   = OperpsnAddService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(OperpsnAddTest,self).__init__(methodName,param)


if __name__ == "__main__":
   from steam.admin.operposition.queryOperpsnTest import OperpsnQueryTest
   from steam.admin.operposition.delOperpsnTest import OperpsnDelTest
   # OperpsnAddTest(methodName = "compareRetcodeTest",
   #                 param     = [ 1, 2, 3, 4, 5, {}, 7, 8])
   OperpsnQueryTest(methodName = "compareRetcodeTest",
                   param     = [ 1, 2, 3, 4, 5, {}, 7, 8])
   OperpsnDelTest(methodName = "compareRetcodeTest",
                   param     = [ 1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\operposition\\steam-featuredhomeConfigcreateConfigs.yml",
                    testclse     = OperpsnAddTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )