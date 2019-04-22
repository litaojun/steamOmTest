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
import requests,json
from opg.util.utils import query_json
#from steam.util.configurl import upActivityurl
from steam.util.httpUopService import  HttpUopService
class ActivityPublishService(HttpUopService):
    '''
        活动新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ActivityPublishService, self).__init__("", "", kwargs)
        # self.activityUpReqjson = self.reqjsondata

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