#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userCancelThumbUpTest.py 
@time: 2018/7/6 16:38 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.user.thumbUp.userThumbUpService import UserThumbUpService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase

class UserCancelThumbUpTest(SteamTestCase):
      '''
            取消点赞
      '''
      __interfaceName__ = "/resource-service/resource/cancelThumbUp"
      def __init__(self, methodName='runTest', param=None):
          super(UserCancelThumbUpTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.userTbuSer = UserThumbUpService(self.inputdata)
          self.setService(self.userTbuSer)

      def userCancelThumbUp(self):
          userThumbUpRsp = self.userTbuSer.userCancelThumbUp()
          retcode = self.userTbuSer.getRetcodeByThumbUpRsp(response=userThumbUpRsp)
          self.assertTrue(retcode == self.expectdata["code"])


if __name__ == "__main__":
    runTestOneCls(
					casefilepath =  "\\steamcase\\user\\userCancelThumbUpcase.xlsx",
					testclse     =  UserCancelThumbUpTest
				 )