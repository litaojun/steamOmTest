#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: upActivityService.py 
@time: 2018/5/7 13:58 
"""
from opg.util.uopService import UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import addActivityurl,upActivityurl
from steam.article.query.ArticleQueryService import ArticleQueryService
from opg.util.schemajson import check_rspdata
from steam.activity.query.queryActivityService import ActivityQueryService
from steam.activity.search.searchActivityService import ActivitySearchService
class ActivityPublishService(UopService):
    '''
        活动新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ActivityPublishService, self).__init__("", "", kwargs,reqjsonfile="\\steam\\activity\jsonfmt\\publishActivityReq.txt")
        self.rsp = None
        #self.publisActUrl = upActivityurl + self.reqjsondata
        self.activityUpReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }
        #self.searchActSer = ActivitySearchService(kwargs={"currentPage": 1, "pageSize": 10, "resourceTypeId": kwargs["resourceTypeId"],"title": kwargs["title"]})

    def publishActivitySer(self):
        pubActivityRsp = requests.post(
										    url=upActivityurl,
										    json=self.activityUpReqjson,
										    headers=self.jsonheart,
										    verify=False
									   )
        return pubActivityRsp.text

    def getRetcodeByUpactRsp(self,oneActRsp = None):
        return query_json(json_content=json.loads(oneActRsp), query="code")

if __name__ == "__main__":
   reqdata = {
	            "resourceId": "22",
                "title": "QUEENS PALACE高级定制馆C-自动化",
	            "resourceTypeId":12
              }
   pubActSer = ActivityPublishService(kwargs=reqdata)
   searchRsp = pubActSer.searchActSer.queryActivity()
   ssid = pubActSer.searchActSer.getFirstActivityIdByRsp(queryRsp=searchRsp)
   pubActSer.activityUpReqjson["resourceId"] = ssid
   pubActRsp = pubActSer.publishActivitySer()
   print(pubActRsp)