#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryOperpsnTest.py 
@time: 2018/4/25 19:24 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.classify.delclassify.delClassifyService import ClassfiyDelService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.operposition.query.queryOperpsnService import OperpsnQueryService

class OperpsnQueryTest(ParametrizedTestCase):
      '''
            admin删除分类
      '''
      __interfaceName__ = "/steam-featured/homeConfig/listData"
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnQueryTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.operpsnQuerySer = OperpsnQueryService(self.inputdata)
          self.setService(self.operpsnQuerySer)

      def testOperpsnQueryNor(self):
          clsrsp = self.operpsnQuerySer.queryOperpsnListdata()
          rspcode = self.operpsnQuerySer.getRetCodeByRsp(clsrsp)
          title = self.operpsnQuerySer.getFirstResourceTitleByRsp(queryRsp=clsrsp)
          self.assertTrue(rspcode == self.expectdata["code"])
          self.assertTrue(title == self.inputdata["title"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\operpsnquerycase.xlsx",
                    testclse = OperpsnQueryTest
                 )