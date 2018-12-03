#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: studyListTest.py 
@time: 2018/10/18 14:50 
"""
from steam.util.testJsonFormat import initInputService
from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.course.studyListService import StudyListService
class StudyListTest(SteamTestCase):
      '''
            用户浏览我的学习列表
      '''
      __interfaceName__ = "/order-service/study/list"
      @initInputService( services = [],
                         curser   = StudyListService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(StudyListTest,self).__init__(methodName,param)

      # def getAliyunVideoAuthTest(self):
      #     rsp        = self.myservice.getStudyListReq()
      #     rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
      #     self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName = "compareRetcodeTest",
                  param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\order-servicestudylists.yml",
                    testclse     = StudyListTest
                 )