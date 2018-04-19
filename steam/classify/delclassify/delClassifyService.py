#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: delClassifyService.py 
@time: 2018/4/18 19:06 
"""


from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import delEntryurl
from steam.classify.addclassify.addClassfiyService import ClassfiyAddService
class ClassfiyDelService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ClassfiyDelService, self).__init__("", "", kwargs)
        self.classfiyReqjson = {
							        "entryName": kwargs['entryName'],
							        "picturePath": kwargs['picturePath']
						        }
        self.delEntryIdJson = {"entryId": 35}
        self.jsonheart = {
	                         "x-token":"admin"
                         }
        self.classfiy = ClassfiyAddService(self.classfiyReqjson)

    @decorator("preInterfaceAddOneEntry")
    def addOneClassfiy(self):
        classfiyrsp = self.classfiy.addClassfiy()
        self.delEntryIdJson["entryId"] = self.classfiy.getEntryIdByRsp(classfiyRsp=classfiyrsp)

    def delClassfiyByEntryId(self,entryid):
        self.delEntryIdJson["entryId"] = entryid
        delclassfiyRsp = requests.post(
									        url=delEntryurl,
									        json=self.delEntryIdJson,
									        headers=self.jsonheart,
									        verify=False
								        )

    def delClassfiy(self):
        delclassfiyRsp = requests.post(
		                                   url=delEntryurl,
		                                   json=self.delEntryIdJson,
		                                   headers=self.jsonheart,
		                                   verify=False
                                      )
        print("addclassfiyrsp = %s" % delclassfiyRsp.text)
        return delclassfiyRsp.text

    def getRetcodeByClassfiyRsp(self, classfiyRsp=None):
        print("classfiyRsp" + str(classfiyRsp))
        return query_json(json_content=json.loads(classfiyRsp), query="code")

    def getEntryIdByRsp(self, classfiyRsp=None):
        return query_json(json_content=json.loads(classfiyRsp), query="data")


if __name__ == "__main__":
	pass  