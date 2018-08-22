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

from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import alertentryurl,delEntryurl
from steam.classify.addclassify.addClassfiyService import ClassfiyAddService
from opg.util.httptools import httpPost
from steam.classify.delclassify.delClassifyService import ClassfiyDelService
class ClassfiyAlertService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ClassfiyAlertService, self).__init__(module       = "",
                                                   filename     = "",
                                                   sqlvaluedict = kwargs,
                                                   reqjsonfile  = "alertClassfiyReq")

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