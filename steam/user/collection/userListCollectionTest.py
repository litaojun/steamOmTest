#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userListCollectionTest.py 
@time: 2018/10/18 16:10 
"""

from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.collection.userListCollectionService import UserListCollectionService
class UserListCollectionTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__    = "/member/collection/queryPage"
      @initInput( services = [],
                  curser   = UserListCollectionService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(UserListCollectionTest,self).__init__(methodName,param)

      def userListCollectTest(self):
          rsp        = self.myservice.userListCollectionReq()
          rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\userListCollectioncase.xlsx",
                    testclse     = UserListCollectionTest
                )