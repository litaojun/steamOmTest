#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: competitionAlertService.py 
@time: 2018/4/20 15:06 
"""
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import alertMatchurl
from opg.util.timeTool import getTimeIntByInPut
from steam.util.httpUopService import  HttpUopService
class CompetitionAlertService(HttpUopService):
    '''
        admin修改赛事场次
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CompetitionAlertService, self).__init__( module       = "",
                                                       filename     = "",
                                                       sqlvaluedict = kwargs,
                                                       reqjsonfile  = None)

    #@decorator("addClassfiyService")
    def alertMatch(self):
        alertMatchRsp = requests.post(
		                                   url     = alertMatchurl,
		                                   json    = self.reqjsondata,
		                                   headers = self.jsonheart,
		                                   verify  = False
                                      )
        return alertMatchRsp.text

    def getRetCodeAlertRsp(self,rsp):
        return query_json(json_content=json.loads(rsp), query="code")

    def alertMatchTime(self,s=1,e=1):
        starttime = getTimeIntByInPut(s)
        endtime   =  getTimeIntByInPut(e)
        self.reqjsondata["applyStartTime"] = starttime
        self.reqjsondata["applyEndTime"] = endtime
        print("set - starttime = %s,endtime=%s" % (starttime, endtime))
        self.alertMatch()


if __name__ == "__main__":
   pass