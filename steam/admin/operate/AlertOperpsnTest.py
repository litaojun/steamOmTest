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
from steam.admin.operate.AlertOperpsnService import OperpsnAlertService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.operate.addOperPsnService import OperpsnAddService
from steam.admin.operate.delOperpsnService import OperpsnDelService
from steam.admin.operate.featuredSearchResourceService import FeaturedSearchResourceService
from steam.admin.operate.queryOperpsnService import OperpsnQueryService
class OperpsnAlertTest(SteamTestCase):
      '''
            admin修改一个运营位配置
      '''
      __interfaceName__ = "/operation-manage/featured/modifyIndexConfig"
      @initAdminInputService( services = [ OperpsnAddService ,
                                      OperpsnDelService ,
                                      FeaturedSearchResourceService ,
                                      OperpsnQueryService ]  ,
                         curser   =   OperpsnAlertService )
      def __init__( self, methodName='runTest', param=None ):
          super(OperpsnAlertTest,self).__init__(methodName , param)

if __name__ == "__main__":
   from steam.admin.operate.addOperPsnTest import OperpsnAddTest
   from steam.admin.operate.delOperpsnTest import OperpsnDelTest
   from steam.admin.operate.featuredSearchResourceTest import FeaturedSearchResourceTest
   from steam.admin.operate.queryOperpsnTest import OperpsnQueryTest
   OperpsnAddTest( methodName = "compareRetcodeTest",
                     param    = [ 1, 2, 3, 4, 5, {}, 7, 8] )
   OperpsnDelTest( methodName = "compareRetcodeTest",
                     param    = [ 1, 2, 3, 4, 5, {}, 7, 8] )
   FeaturedSearchResourceTest( methodName = "compareRetcodeTest",
                                param     = [ 1, 2, 3, 4, 5, {}, 7, 8] )
   OperpsnQueryTest( methodName = "compareRetcodeTest",
                     param      = [ 1, 2, 3, 4, 5, {}, 7, 8] )
   runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\operate\\operation-manageFeaturedModifyIndexConfigs.yml" ,
                    testclse     = OperpsnAlertTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )