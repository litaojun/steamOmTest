#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: AlertOperpsnService.py 
@time: 2018/4/25 16:37 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import alertOperpositionurl,delOperpositionurl
from steam.classify.addclassify.addClassfiyService import ClassfiyAddService
from steam.operposition.add.addOperPsnService import  OperpsnAddService
class OperpsnAlertService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(OperpsnAlertService, self).__init__("", "", kwargs)
        self.operpsnAlertReqjson = {
								        "title": kwargs['title'],
								        "picPath": kwargs['picPath'],
								        "listOrder": kwargs['listOrder'],
	                                    "oldListOrder": kwargs['oldListOrder'],
								        "itemId": kwargs['itemId'],
								        "position": kwargs['position'],
								        "displayType": kwargs['displayType'],
	                                    "id":kwargs['id']
                                    }

        self.jsonheart = {
	                         "x-token":"admin"
                         }
        self.rsp = None
        self.operpsnAddSer = OperpsnAddService(self.operpsnAlertReqjson)

    @decorator("preInterfaceAddOneOperpsn")
    def addOneOperpsn(self):
        operpsnAddRsp = self.operpsnAddSer.addOperPosition()
        self.rsp = operpsnAddRsp
        self.operpsnAlertReqjson["id"] = self.operpsnAddSer.getOperpsnIdByTitle()
        print("alertOperpsnId = %s" % self.operpsnAlertReqjson["id"])

    @decorator("tearInterfaceDelOneOperpsn")
    def delOperpsn(self):
        rssid = self.operpsnAddSer.getOperpsnIdByTitle()
        delOperpsnRsp = requests.post(
								        url=delOperpositionurl,
								        json={"ids": [rssid]},
								        headers=self.jsonheart,
								        verify=False
							        )
        print("delOperpsnRsp = %s" % delOperpsnRsp.text)
        return delOperpsnRsp.text
    #@decorator("addClassfiyService")
    def alertOperpsn(self):
        addOperpsnRsp = requests.post(
		                                url=alertOperpositionurl,
		                                json=self.operpsnAlertReqjson,
		                                headers=self.jsonheart,
		                                verify=False
                                      )
        print("addclassfiyrsp = %s" % addOperpsnRsp.text)
        return addOperpsnRsp.text

    def getRetCodeOperpsnRsp(self,rsp):
        return query_json(json_content=json.loads(rsp), query="code")

if __name__ == "__main__":
   alertjson = {
					"title": "Makeblock 2017 品牌视频",
					"picPath": "http://uat-steam.opg.cn/_static/admin/images/resource/20180425112224_258421.jpg",
					"position": "03",
					"oldListOrder": 1,
					"listOrder": 1,
					"displayType": "1",
					"itemId": 121,
					"id": 52
				}
   operAlertSer = OperpsnAlertService(alertjson)
   addrsp = operAlertSer.addOneOperpsn()
   alertRsp = operAlertSer.alertOperpsn()
   print(alertRsp)
   code = operAlertSer.getRetCodeAlertRsp(alertRsp)
   print("code=%s" % code)
   delRsp = operAlertSer.delOperpsn()
   print("delRsp=%s" % delRsp)