#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: alertClassService.py 
@time: 2018/4/18 19:05 
"""
from steam.util.httpUopService import  HttpUopService
from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.configurl import alertentryurl
from steam.admin.classify.addClassfiyService import ClassfiyAddService
from opg.util.httptools import httpPost
from steam.admin.classify.delClassifyService import ClassfiyDelService
class ClassfiyAlertService(HttpUopService):
    '''
        分类修改
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ClassfiyAlertService, self).__init__(module       = "",
                                                   filename     = "",
                                                   sqlvaluedict = kwargs,
                                                   reqjsonfile  = None)

    @decorator("preInterfaceAddOneEntry")
    def addOneClassfiy(self):
        addClassfiySer = ClassfiyAddService(self.inputKV)
        classfiyrsp = addClassfiySer.addClassfiy()
        entryId = addClassfiySer.getEntryIdByRsp(classfiyRsp=classfiyrsp)
        self.reqjsondata["entryId"] = entryId
        self.inputKV["entryId"]     = entryId

    @decorator("tearInterfaceDelOneEntry")
    def delClassfiy(self):
        delCfySer = ClassfiyDelService(self.inputKV)
        delclassfiyRsp = delCfySer.delClassfiy()
        return delclassfiyRsp
    #@decorator("addClassfiyService")
    def alertClassfiy(self):
        self.rsp = httpPost(url         =  alertentryurl,
                            headers     =  self.jsonheart,
                            reqJsonData =  self.reqjsondata)
        return self.rsp

    def getRetCodeAlertRsp(self,rsp):
        return query_json(json_content=json.loads(rsp), query="code")

if __name__ == "__main__":
   pass