#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: addClassfiyService.py 
@time: 2018/4/17 14:41 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import addentryurl
class ClassfiyAddService(UopService):
    '''
        分类新增
    '''

    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ClassfiyAddService, self).__init__("", "", kwargs)
        self.classfiyReqjson = {
	                                "entryId": None,
							        "entryName": kwargs['entryName'],
							        "picturePath": kwargs['picturePath'],
	                                "state": "UNVISIBLE",
							        "fileListThumb": [],
							        "order": 100
						       }
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    #@decorator("addClassfiyService")
    def addClassfiy(self):
        addclassfiyRsp = requests.post(
		                                   url=addentryurl,
		                                   json=self.classfiyReqjson,
		                                   headers=self.jsonheart,
		                                   verify=False
                                      )
        print("addclassfiyrsp = %s" % addclassfiyRsp.text)
        return addclassfiyRsp.text

    def getRetcodeByClassfiyRsp(self,classfiyRsp = None):
        print("classfiyRsp" + str(classfiyRsp))
        return query_json(json_content=json.loads(classfiyRsp), query="code")

if __name__ == "__main__":
   pass