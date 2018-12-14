#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryCourseTest.py 
@time: 2018/12/10 11:02 
"""
from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.course.queryCourseService import QueryCourseService
from steam.util.testJsonFormat import initInputService
class QueryCourseTest(SteamTestCase):
      '''
            用户查看课程详情页
      '''
      __interfaceName__ = "/steam-course/course/queryCourse"
      @initInputService( services = [ WeixinSearchService ],
                         curser   = QueryCourseService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(QueryCourseTest,self).__init__(methodName,param)


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
                    casefilepath = "\\steamcase\\user\\steam-coursecoursequeryCourse.yml",
                    testclse     = QueryCourseTest
                )