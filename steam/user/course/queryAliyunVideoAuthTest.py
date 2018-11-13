#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryAliyunVideoAuthTest.py 
@time: 2018/10/15 10:51 
"""
from steam.util.testJsonFormat import initInput
from steam.util.steamLog       import SteamTestCase
from opg.unit.testcaseRunMgr   import runTestOneCls
from steam.user.search.weixinSearchService         import WeixinSearchService
from steam.user.weixin.userViewCourseService       import UserViewCourseService
from steam.user.course.queryAliyunVideoAuthService import QueryAliyunVideoAuthService
class QueryAliyunVideoAuthTest(SteamTestCase):
      '''
            用户获取观看权限字符串
      '''
      __interfaceName__ = "/steam-course/course/queryAliyunVideoAuth"
      @initInput( services = [ WeixinSearchService , UserViewCourseService ],
                  curser   = QueryAliyunVideoAuthService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(QueryAliyunVideoAuthTest,self).__init__(methodName,param)

      def getAliyunVideoAuthTest(self):
          rsp        = self.myservice.getAliyunVideoAuthReq()
          rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\aliyunVideoAuthcase.xlsx",
                    testclse     = QueryAliyunVideoAuthTest
                )