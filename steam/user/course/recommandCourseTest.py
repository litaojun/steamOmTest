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
from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.course.recommandCourseService import RecommandCourseService
class RecommandCourseTest(SteamTestCase):
      '''
            用户查看推荐课程列表
      '''
      __interfaceName__ = "/steam-course/course/queryRecommandCourse"
      @initInput( services = [WeixinSearchService],
                  curser   = RecommandCourseService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(RecommandCourseTest,self).__init__(methodName,param)

      def recommandCourseNor(self):
          rsp        = self.myservice.recommandCourseList()
          rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\recommandCoursecase.xlsx",
                    testclse     = RecommandCourseTest
                )