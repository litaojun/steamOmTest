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
from opg.bak.uopService import decorator
import requests,json
from opg.util.utils import query_json
#from steam.util.configurl import delEntryurl
from steam.util.httpUopService import  HttpUopService
# from steam.classify.delclassify.delClassifyService import ClassfiyDelService

class ClassfiyAddService(HttpUopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ClassfiyAddService, self).__init__(module       = "",
                                                 filename     = "",
                                                 sqlvaluedict = kwargs)

    @decorator("tearInterfaceDelOneEntry")
    def delClassfiy(self):
        entryId = self.getEntryIdByRsp(classfiyRsp = self.rsp)
        delclassfiyRsp = requests.post(
									        url  = delEntryurl,
									        json = {
                                                      "entryId": entryId
                                                    },
									        headers = self.jsonheart,
									        verify  = False
								      )
        return delclassfiyRsp.text

    @decorator(["setupAddEntry"])
    def addClassfiy(self):
        self.sendHttpReq()

    def getRetcodeByClassfiyRsp(self,classfiyRsp = None):
        return query_json(json_content=json.loads(classfiyRsp), query="code")

    @decorator(["tearDownGetEntryId","setupGetEntryId"])
    def getEntryIdByRsp(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        self.inputKV["entryId"] = int(query_json(json_content = json.loads(self.rsp),
                                              query        = "data"))
        # return query_json(json_content=json.loads(classfiyRsp), query="data")

if __name__ == "__main__":
   args = {
             "entryName":"litaojun",
             "picturePath":"www.sohu.com"
          }
   clsAddSer = ClassfiyAddService(kwargs=args)
   rsp = clsAddSer.addClassfiy()
   retcode = clsAddSer.getRetcodeByClassfiyRsp(classfiyRsp= rsp)
   print(rsp)
   clsAddSer.delClassfiy()