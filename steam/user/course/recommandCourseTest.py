#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: recommandCourseTest.py 
@time: 2018/10/12 16:58 
"""
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.course.recommandCourseService import RecommandCourseService
from steam.util.testJsonFormat import initInputService
class RecommandCourseTest(SteamTestCase):
      '''
            用户查看推荐课程列表
      '''
      __interfaceName__ = "/steam-course/course/queryRecommandCourse"
      @initInputService( services = [WeixinSearchService],
                         curser   = RecommandCourseService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(RecommandCourseTest,self).__init__(methodName,param)
      #
      # def recommandCourseNor(self):
      #     rsp        = self.myservice.recommandCourseList()
      #     rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
      #     self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   from steam.user.search.weixinSearchTest import WeixinSearchTest
   WeixinSearchTest(methodName="compareRetcodeTest",param = [1,2,3,4,5,{},7,8])
   from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
   from steam.user.login.userLoginTest import UserLoginTest
   UserVerfiyCodeTest( methodName = "compareRetcodeTest",
                       param      = [1, 2, 3, 4, 5, {}, 7, 8] )
   UserLoginTest(methodName="compareRetcodeTest",
                 param=[1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\steam-coursecoursequeryRecommandCourses.yml",
                    testclse     = RecommandCourseTest
                )