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
class ClassfiyAlertService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ClassfiyAlertService, self).__init__("", "", kwargs)
        self.classfiyAlertReqjson = {
		                                 "entryId":11,
	                                     "entryName":kwargs['entryName'],
	                                     "picturePath": kwargs['picturePath'],
	                                     "order":3,
	                                     "state":kwargs['state']
                                    }
        self.classfiyReqjson = {
							        "entryName": kwargs['entryName'],
							        "picturePath": kwargs['picturePath']
						        }
        self.jsonheart = {
	                         "x-token":"admin"
                         }
        self.rsp = None
        self.classfiy = ClassfiyAddService(self.classfiyReqjson)

    @decorator("preInterfaceAddOneEntry")
    def addOneClassfiy(self):
        classfiyrsp = self.classfiy.addClassfiy()
        self.rsp = classfiyrsp
        self.classfiyAlertReqjson["entryId"] = self.classfiy.getEntryIdByRsp(classfiyRsp=classfiyrsp)

    @decorator("tearInterfaceDelOneEntry")
    def delClassfiy(self):
        entryId = self.classfiy.getEntryIdByRsp(classfiyRsp=self.rsp)
        delclassfiyRsp = requests.post(
										        url=delEntryurl,
										        json={"entryId": entryId},
										        headers=self.jsonheart,
										        verify=False
									  )
        print("delclassfiyRsp = %s" % delclassfiyRsp.text)
        return delclassfiyRsp.text
    #@decorator("addClassfiyService")
    def alertClassfiy(self):
        addclassfiyRsp = requests.post(
		                                   url=alertentryurl,
		                                   json=self.classfiyAlertReqjson,
		                                   headers=self.jsonheart,
		                                   verify=False
                                      )
        print("addclassfiyrsp = %s" % addclassfiyRsp.text)
        return addclassfiyRsp.text

    def getRetCodeAlertRsp(self,rsp):
        return query_json(json_content=json.loads(rsp), query="code")

if __name__ == "__main__":
   pass