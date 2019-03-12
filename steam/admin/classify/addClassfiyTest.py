#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: addClassfiyTest.py 
@time: 2018/4/17 14:41 
"""
from steam.admin.classify.addClassfiyService import ClassfiyAddService
from steam.admin.classify.delClassifyService import ClassfiyDelService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
class ClassfiyAddTest(SteamTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/operation-manage/entry/addEntry"
      @initAdminInputService(curser   = ClassfiyAddService,
                        services = [ ClassfiyDelService ])
      def __init__(self, methodName='runTest', param=None):
          super(ClassfiyAddTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.classify.delClassifyTest import ClassfiyDelTest
   ClassfiyDelTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\classify\\resource-serviceresourceaddEntrys.yml",
                    testclse = ClassfiyAddTest
                 )
