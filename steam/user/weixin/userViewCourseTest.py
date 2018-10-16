#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userViewCourseTest.py 
@time: 2018/10/12 15:20 
"""
from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userViewCourseService import UserViewCourseService
class UserViewCourseTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__ = "/steam-course/course/queryCourse"
      @initInput( services = [WeixinSearchService],
                  curser   = UserViewCourseService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(UserViewCourseTest,self).__init__(methodName,param)

      def userViewCourseNor(self):
          rsp        = self.myservice.userViewCourse()
          rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\userViewCoursecase.xlsx",
                    testclse     = UserViewCourseTest
                )