#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: addOperPsnService.py 
@time: 2018/4/25 14:06 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import addOperpositionurl
from steam.util.configurl import delOperpositionurl
from steam.operposition.query.queryOperpsnService import OperpsnQueryService

class OperpsnAddService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(OperpsnAddService, self).__init__("", "", kwargs,reqjsonfile="userOperAddReq")


    @decorator("tearInterfaceDelOneOperPsn")
    def delOperPosition(self):
        operpsnqySer = OperpsnQueryService(self.inputKV)
        rspdata = operpsnqySer.queryOperpsnListdata()
        rssid = operpsnqySer.getFirstResourceIdByRsp(rspdata)
        delOperpsnRsp = requests.post(
									    url  =  delOperpositionurl,
									    json = {"ids":[rssid]},
									    headers = self.jsonheart,
									    verify  =  False
								      )
        print("delOperpsnRsp = %s" % delOperpsnRsp.text)
        return delOperpsnRsp.text

    def addOperPosition(self):
        addOperpositionfiyRsp = requests.post(
				                                   url=addOperpositionurl,
				                                   json=self.reqjsondata,
				                                   headers=self.jsonheart,
				                                   verify=False
		                                      )
        self.rsp = addOperpositionfiyRsp.text
        return addOperpositionfiyRsp.text

    def getRetcodeByOperpsnRsp(self,operpsnRsp = None):
        return query_json(json_content=json.loads(operpsnRsp), query="code")

    def getOperpsnIdByTitle(self,title = "",position = ""):
        operQuerySer = OperpsnQueryService(self.inputKV)
        rsplistdataRsp = operQuerySer.queryOperpsnListdata()
        rssid = operQuerySer.getFirstResourceIdByRsp(rsplistdataRsp)
        return rssid

if __name__ == "__main__":
   addOperPsnReqjson = {
							"title"        :   "风靡全球的少儿编程",
							"picPath"      : "http://uat-steam.opg.cn/_static/admin/images/resource/20180425150543_430837.jpg",
							"listOrder"    :  3,
							"resourceId"   :  2027,
	                        "position"     : "03",
	                        "displayType"  : "2",
	                        "oldListOrder" : 0,
                            "token": "69a42b2f9ebd4275a04a602648d857c1"
					   }
   operpsnSer = OperpsnAddService(addOperPsnReqjson)
   rsp = operpsnSer.addOperPosition()
   code = operpsnSer.getRetcodeByOperpsnRsp(operpsnRsp=rsp)
   print("code = %s" % code)
   id = operpsnSer.getOperpsnIdByTitle(rsp)
   print("id = %s" % id)
   operpsnSer.delOperPosition()