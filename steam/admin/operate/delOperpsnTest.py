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
from steam.admin.operate.delOperpsnService import OperpsnDelService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
from steam.admin.operate.addOperPsnService import OperpsnAddService
from steam.admin.operate.queryOperpsnService import OperpsnQueryService
class OperpsnDelTest(SteamTestCase):
      '''
            admin删除一个运营位配置
      '''
      __interfaceName__ = "/operation-manage/featured/removeIndexConfig"
      @initInputService( services = [ OperpsnAddService , OperpsnQueryService ] ,
                         curser   = OperpsnDelService )
      def __init__( self, methodName = 'runTest' ,
                          param      = None ):
          super(OperpsnDelTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.operate.queryOperpsnTest import OperpsnQueryTest
   from steam.admin.operate.addOperPsnTest import OperpsnAddTest
   OperpsnAddTest(methodName = "compareRetcodeTest",
                   param     = [ 1, 2, 3, 4, 5, {}, 7, 8])
   OperpsnQueryTest(methodName = "compareRetcodeTest",
                   param     = [ 1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\steam-featuredhomeConfigremoveIndexConfigs.yml"  ,
                    testclse     = OperpsnDelTest
                 )