#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userCancelCollectionTest.py 
@time: 2018/10/18 16:01 
"""

from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class UserCancelCollectionTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__    = "/resource-service/resource/cancelCollect"
      @initInput( services = [],
                  curser   = UserCancelCollectionService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(UserCancelCollectionTest,self).__init__(methodName,param)

      def userCancelCollectTest(self):
          rsp        = self.myservice.userCancelCollectionReq()
          rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
          self.assertTrue(rspcode == self.expectdata["code"],msg="rspcode=%s,expectcode=%s" % (rspcode,self.expectdata["code"]))

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\userCancelCollectioncase.xlsx",
                    testclse     = UserCancelCollectionTest
                )