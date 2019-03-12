#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: alertClassTest.py 
@time: 2018/4/18 19:06 
"""
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.classify.alertClassService import ClassfiyAlertService
from steam.admin.classify.delClassifyService import ClassfiyDelService
from steam.admin.classify.addClassfiyService import ClassfiyAddService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class ClassfiyAlertTest(SteamTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/operation-manage/entry/modifyEntry"
      @initAdminInputService( curser   = ClassfiyAlertService,
                         services = [ClassfiyAddService,ClassfiyDelService] )
      def __init__(self, methodName='runTest', param=None):
          super(ClassfiyAlertTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.classify.addClassfiyTest import ClassfiyAddTest
   from steam.admin.classify.delClassifyTest import ClassfiyDelTest
   ClassfiyAddTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
   ClassfiyDelTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\classify\\resource-serviceresourcemodifyEntrys.yml" ,
                    testclse     = ClassfiyAlertTest
                 )
