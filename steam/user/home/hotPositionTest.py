#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: hotPositionTest.py 
@time: 2018/6/6 19:24 
"""
from steam.user.home.hotPositionService import HomeHotPositionService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
class HotPositionTest(SteamTestCase):
      '''
            计算内容
      '''
      __interfaceName__ = "/featured/index/configs/pageQueryPositionShows"
      @initInputService(services = [],
                        curser   = HomeHotPositionService)
      def __init__(self, methodName='runTest', param=None):
          super(HotPositionTest,self).__init__(methodName,param)
          # self.homeHotSer = HomeHotPositionService(self.inputdata)
          # self.setService(self.homeHotSer)

      # #首页热门推荐计算内容
      # def queryHomeCnf(self):
      #     userHomeHotRsp = self.homeHotSer.queryHomeHotPosition()
      #     retcode = self.homeHotSer.getRetcodeByActivityRsp(response=userHomeHotRsp)
      #     self.assertTrue(retcode == self.expectdata["code"])
      #     self.assertTrue(self.homeHotSer.compareM())

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest

    UserVerfiyCodeTest( methodName="compareRetcodeTest" ,
                        param=[1, 2, 3, 4, 5, {}, 7, 8] )
    UserLoginTest( methodName="compareRetcodeTest" ,
                   param=[1, 2, 3, 4, 5, {}, 7, 8] )
    runTestOneCls(
					casefilepath =  "\\steamcase\\homepage\\featuredindexconfigspageQueryPositionShowss.yml",
					testclse     =  HotPositionTest
				)