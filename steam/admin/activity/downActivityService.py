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
from opg.util.uopService import UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import downActivityurl
from steam.util.reqFormatPath import fxt,activityDownReq

from steam.util.httpUopService import  HttpUopService
class ActivityUnPublishService(HttpUopService):
    '''
        活动下线
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ActivityUnPublishService, self).__init__(module       = "",
                                                       filename     = "",
                                                       sqlvaluedict = kwargs,
                                                       reqjsonfile  = None)

    def unPublishActivitySer(self):
        pubActivityRsp = requests.post(
										    url     = downActivityurl,
										    json    = self.reqjsondata,
										    headers = self.jsonheart,
										    verify  = False
									  )
        return pubActivityRsp.text

    # def getRetcodeByRsp(self,oneActRsp = None):
    #     return query_json(json_content = json.loads(oneActRsp),
    #                       query        = "code")

if __name__ == "__main__":
   reqdata = {
	            "resourceId": "22",
                "title": "QUEENS PALACE高级定制馆C-自动化",
	            "resourceTypeId":12
              }
   pubActSer = ActivityUnPublishService(kwargs=reqdata)
   searchRsp = pubActSer.searchActSer.queryActivity()
   ssid = pubActSer.searchActSer.getFirstActivityIdByRsp(queryRsp=searchRsp)
   pubActSer.activityDownReqjson["resourceId"] = ssid
   pubActRsp = pubActSer.unPublishActivitySer()
   print(pubActRsp)