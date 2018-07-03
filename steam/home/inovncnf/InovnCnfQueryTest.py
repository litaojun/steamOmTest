#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: InovnCnfQueryTest.py 
@time: 2018/6/14 15:49 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.home.cnfquery.homeCnfQueryService import HomeCnfQueryService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase

class InovnCnfQueryTest(SteamTestCase):
      '''
            用户进入公众号奥林匹克页，获取运营位数据
      '''
      __interfaceName__ = "/featured/index/configs/queryShowConfigs-invoencnf"
      def __init__(self, methodName='runTest', param=None):
          super(InovnCnfQueryTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.homeCnfQuerySer = HomeCnfQueryService(self.inputdata)
          self.setService(self.homeCnfQuerySer)

      def queryFindCnf(self):
          userFindCnfRsp = self.homeCnfQuerySer.queryHomePageCnf()
          retcode = self.homeCnfQuerySer.getRetcodeByActivityRsp(response=userFindCnfRsp)
          self.assertTrue(retcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
					casefilepath =  "\\steamcase\\homepage\\inovnpagecnfcase.xlsx",
					testclse     =  InovnCnfQueryTest
				)