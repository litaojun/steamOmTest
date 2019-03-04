#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryActivityTest.py 
@time: 2018/5/10 16:38 
"""
from steam.util.testJsonFormat import initInput
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.activity.searchActivityService import ActivitySearchService
from steam.admin.activity.queryActivityService import ActivityQueryService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
class ActivityQueryTest(SteamTestCase):
      '''
            根据ID搜索活动
            使用和微信端相同接口
      '''
      __interfaceName__   = "/operation-manage/product/query"
      @initAdminInputService(services = [ ActivitySearchService ] ,
                             curser   =   ActivityQueryService   )
      def __init__(self, methodName =  'runTest',
                         param      =  None      ):
          super(ActivityQueryTest,self).__init__(methodName , param)

if __name__ == "__main__":
         from steam.admin.activity.searchActivityTest import ActivitySearchTest
         ActivitySearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
         runTestOneCls(
				          casefilepath =  "\\steamcase\\admin\\activity\\operation-manageproductquerys.yml",
				          testclse     =  ActivityQueryTest,
                          basepath     = "D:\\litaojun\\steamyml"
			           )