#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: findClassifyTest.py 
@time: 2018/4/18 19:05 
"""
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.classify.findClassifyService import ClassfiySearchService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class ClassfiySearchTest(SteamTestCase):
      '''
            admin查询分类列表
      '''
      __interfaceName__ = "/operation-manage/entry/queryEntries"
      @initAdminInputService(curser   =  ClassfiySearchService ,
                        services = [ ] )
      def __init__(self, methodName='runTest', param=None):
          super(ClassfiySearchTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.classify.addClassfiyTest import ClassfiyAddTest
   ClassfiyAddTest(methodName = "compareRetcodeTest" ,
                   param      = [1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\classify\\resource-serviceresourceSearchEntrys.yml",
                    testclse     = ClassfiySearchTest
                 )