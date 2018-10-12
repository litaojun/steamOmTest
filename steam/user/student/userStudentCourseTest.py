#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userStudentCourseTest.py 
@time: 2018/10/12 17:28 
"""

from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.course.recommandCourseService import RecommandCourseService
from steam.user.student.userStudentCourseService import UserStudentCourseService
class UserStudentCourseTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__ = "/order-service/study/list"
      @initInput( services = [WeixinSearchService],
                  curser   = UserStudentCourseService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(UserStudentCourseTest,self).__init__(methodName,param)

      def recommandCourseNor(self):
          rsp        = self.myservice.userStudentCourseList()
          rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\userStudentCourseListcase.xlsx",
                    testclse     = UserStudentCourseTest
                )