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
from steam.admin.operate.addOperPsnService import OperpsnAddService
from steam.admin.operate.delOperpsnService import OperpsnDelService
from steam.admin.operate.queryOperpsnService import OperpsnQueryService
from steam.admin.operate.featuredSearchResourceService import FeaturedSearchResourceService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
class OperpsnAddTest(SteamTestCase):
      '''
            admin新增一个运营位配置
      '''
      __interfaceName__ = "/operation-manage/featured/createConfig"
      @initAdminInputService( services = [ OperpsnDelService ,OperpsnQueryService,FeaturedSearchResourceService ] ,
                         curser   = OperpsnAddService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(OperpsnAddTest,self).__init__(methodName,param)


if __name__ == "__main__":
   from steam.admin.operate.queryOperpsnTest import OperpsnQueryTest
   from steam.admin.operate.delOperpsnTest import OperpsnDelTest
   from steam.admin.operate.featuredSearchResourceTest import FeaturedSearchResourceTest
   OperpsnQueryTest( methodName = "compareRetcodeTest",
                     param     = [ 1, 2, 3, 4, 5, {}, 7, 8] )
   OperpsnDelTest(  methodName = "compareRetcodeTest",
                    param     = [ 1, 2, 3, 4, 5, {}, 7, 8] )
   FeaturedSearchResourceTest( methodName = "compareRetcodeTest",
                                param     = [ 1, 2, 3, 4, 5, {}, 7, 8] )
   runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\operate\\steam-featuredhomeConfigcreateConfigs.yml",
                    testclse     = OperpsnAddTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )