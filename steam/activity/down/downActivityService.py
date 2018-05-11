#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: downActivityService.py
@time: 2018/5/7 13:57 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import addActivityurl,downActivityurl
from steam.article.query.ArticleQueryService import ArticleQueryService
from opg.util.schemajson import check_rspdata
from steam.activity.query.queryActivityService import ActivityQueryService
from steam.activity.search.searchActivityService import ActivitySearchService
class ActivityUnPublishService(UopService):
    '''
        活动新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ActivityUnPublishService, self).__init__("", "", kwargs,reqjsonfile="\\steam\\activity\jsonfmt\\unPublishActivityReq.txt")
        self.rsp = None
        #self.publisActUrl = upActivityurl + self.reqjsondata
        self.activityDownReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }
        #self.searchActSer = ActivitySearchService(kwargs={"currentPage": 1, "pageSize": 10, "resourceTypeId": kwargs["resourceTypeId"],"title": kwargs["title"]})

    def unPublishActivitySer(self):
        pubActivityRsp = requests.post(
										    url=downActivityurl,
										    json=self.activityDownReqjson,
										    headers=self.jsonheart,
										    verify=False
									   )
        return pubActivityRsp.text

    def getRetcodeByDownactRsp(self,oneActRsp = None):
        return query_json(json_content=json.loads(oneActRsp), query="code")

if __name__ == "__main__":
   reqdata = {
	            "resourceId": "22",
                "title": "QUEEN'S PALACE高级定制馆1-自动化",
	            "resourceTypeId":12
              }
   pubActSer = ActivityUnPublishService(kwargs=reqdata)
   searchRsp = pubActSer.searchActSer.queryActivity()
   ssid = pubActSer.searchActSer.getFirstActivityIdByRsp(queryRsp=searchRsp)
   pubActSer.activityDownReqjson["resourceId"] = ssid
   pubActRsp = pubActSer.unPublishActivitySer()
   print(pubActRsp)