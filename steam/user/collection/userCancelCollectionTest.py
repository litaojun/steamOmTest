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

from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCollectionService import UserCollectionService
class UserCancelCollectionTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__    = "/resource-service/resource/cancelCollect"
      @initInputService( services = [ WeixinSearchService ,UserCollectionService ],
                         curser   = UserCancelCollectionService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(UserCancelCollectionTest,self).__init__(methodName,param)

      # def userCancelCollectTest(self):
      #     rsp        = self.myservice.userCancelCollectionReq()
      #     rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
      #     self.assertTrue(rspcode == self.expectdata["code"],
      #                     msg     =  "rspcode=%s,e  expectcode=%s" % (rspcode,self.expectdata["code"]))

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.collection.userCollectionTest import UserCollectionTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserCollectionTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\resource-serviceresourcecancelCollects.yml",
                    testclse     = UserCancelCollectionTest
                 )