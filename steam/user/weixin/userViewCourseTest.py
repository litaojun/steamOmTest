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
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userViewCourseService import UserViewCourseService
from steam.util.testJsonFormat import initInputService
class UserViewCourseTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__ = "/steam-course/course/queryCourse"
      @initInputService( services = [ WeixinSearchService ],
                         curser   = UserViewCourseService )
      def __init__( self, methodName = 'runTest',
                          param      = None ):
          super(UserViewCourseTest,self).__init__(methodName,param)

      # def userViewCourseNor(self):
      #     rsp        = self.myservice.userViewCourse()
      #     rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
      #     self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   from steam.user.search.weixinSearchTest import WeixinSearchTest
   WeixinSearchTest(methodName="compareRetcodeTest",param = [1,2,3,4,5,{},7,8])
   from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
   from steam.user.login.userLoginTest import UserLoginTest
   UserVerfiyCodeTest(methodName="compareRetcodeTest",
                      param=[1, 2, 3, 4, 5, {}, 7, 8])
   UserLoginTest(methodName="compareRetcodeTest",
                 param=[1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\steam-coursecoursequeryCourses.yml",
                    testclse     = UserViewCourseTest,
                    basepath     = "D:\\litaojun\\steamyml"
                )