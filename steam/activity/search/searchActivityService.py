#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: searchActivityService.py 
@time: 2018/5/7 17:33 
"""
from opg.util.uopService import UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import searchActivityurl

class ActivitySearchService(UopService):
    '''
        查询分类
    '''
    def __init__(self,kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ActivitySearchService, self).__init__("", "", kwargs,reqjsonfile="\\steam\\activity\\jsonfmt\\searchActivityReq.txt")
        self.rsp = None
        self.activityQueryReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def queryActivity(self):
        queryResult = requests.post(url = searchActivityurl,
                                    json=self.activityQueryReqjson,
                                    headers=self.jsonheart,
                                    verify=False
                                    )
        return queryResult.text

    def getFirstActivityIdByRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="data.0.resourceId")

    def getRetcodeByActRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="code")

if __name__ == "__main__":
    queryJsonData = {"currentPage":1,"pageSize":10,"resourceTypeId":12,"title":"QUEENS PALACE高级定制馆C-自动化"}
    aqs = ActivitySearchService(kwargs=queryJsonData)
    queryResultRsp = aqs.queryActivity()
    rsid = aqs.getFirstActivityIdByRsp(queryRsp=queryResultRsp)
    print("rsid = %s" % rsid)