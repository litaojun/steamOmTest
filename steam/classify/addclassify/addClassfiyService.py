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
from steam.util.configurl import delEntryurl
from opg.util.httptools import httpPost
# from steam.classify.delclassify.delClassifyService import ClassfiyDelService

class ClassfiyAddService(UopService):
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
                                                 sqlvaluedict = kwargs,
                                                 reqjsonfile  = "addClassfiyReq")

    @decorator("tearInterfaceDelOneEntry")
    def delClassfiy(self):
        entryId = self.getEntryIdByRsp(classfiyRsp = self.rsp)
        delclassfiyRsp = requests.post(
									        url=delEntryurl,
									        json={"entryId": entryId},
									        headers=self.jsonheart,
									        verify=False
								      )
        return delclassfiyRsp.text

    def addClassfiy(self):
        self.rsp = httpPost(url         = addentryurl,
                            headers     = self.jsonheart,
                            reqJsonData = self.reqjsondata)
        return self.rsp

    def getRetcodeByClassfiyRsp(self,classfiyRsp = None):
        return query_json(json_content=json.loads(classfiyRsp), query="code")

    def getEntryIdByRsp(self,classfiyRsp = None):
        return query_json(json_content=json.loads(classfiyRsp), query="data")

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