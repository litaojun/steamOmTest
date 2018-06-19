#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: findCalTest.py 
@time: 2018/6/19 16:31 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.home.calculate.hotPositionService import HomeHotPositionService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase

class FindCalTest(SteamTestCase):
      '''
            首页发现页-热门内容-计算内容
      '''
      __interfaceName__ = "/featured/index/configs/pageQueryPositionShows-home"
      def __init__(self, methodName='runTest', param=None):
          super(FindCalTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.homeHotSer = HomeHotPositionService(self.inputdata)
          self.setService(self.homeHotSer)

      def queryHomeCnf(self):
          userHomeHotRsp = self.homeHotSer.queryHomeHotPosition()
          retcode = self.homeHotSer.getRetcodeByActivityRsp(response=userHomeHotRsp)
          self.assertTrue(retcode == self.expectdata["code"])
          self.assertTrue(self.homeHotSer.compareSerData(response=userHomeHotRsp,
                                                         position=self.inputdata["position"],
                                                         configSqlStr = "select_t_sku_HomePage",
                                                         calSqlStr = "select_t_resource_calculate"))

if __name__ == "__main__":
   runTestOneCls(
					casefilepath =  "\\steamcase\\homepage\\findpositioncase.xlsx",
					testclse     =  FindCalTest
				)