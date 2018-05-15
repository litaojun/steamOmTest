#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: li.taojun
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006
@software: PyCharm
@file: queryActivityTest.py
@time: 2018/5/10 16:38
"""


from opg.unit.parametrized import ParametrizedTestCase
from steam.article.add.ArticleAddService import ArticleAddService
from steam.activity.add.addActivityService import ActivityAddService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.activity.query.queryActivityService import ActivityQueryService

class GoodsQueryTest(ParametrizedTestCase):
      '''
            根据ID搜索活动
      '''
      __interfaceName__ = "/steam-resource/admin/product/query-activity"
      def __init__(self, methodName='runTest', param=None):
          super(GoodsQueryTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.activitySer = ActivitySearchService(self.inputdata)
          self.setService(self.activitySer)

      def queryActivityDetail(self):
          activityRsp = self.activitySer.queryActivity()
          code = self.activitySer.getRetcodeByActRsp(queryRsp=activityRsp)
          self.assertTrue(code == self.expectdata["code"])
          rssid = self.activitySer.getFirstActivityIdByRsp(queryRsp=activityRsp)
          queryReqJson = {"resourceId":rssid}
          queryActSer = ActivityQueryService(kwargs=queryReqJson)
          oneActRsp = queryActSer.queryOneActivity()
          code = queryActSer.getRetcodeByOneactRsp(oneActRsp = oneActRsp)
          self.assertTrue(code == self.expectdata["code"])




if __name__ == "__main__":
          runTestOneCls(
				          casefilepath="\\steamcase\\goods\\goodsquerycase.xlsx",
				          testclse=GoodsQueryTest
			           )