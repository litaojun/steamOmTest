#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: delOperpsnService.py 
@time: 2018/4/25 18:12 
"""
from opg.util.uopService import decorator
import json
from opg.util.utils import query_json
from steam.admin.operate.addOperPsnService import  OperpsnAddService
from steam.util.httpUopService import  HttpUopService
class OperpsnDelService(HttpUopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(OperpsnDelService, self).__init__(sqlvaluedict = kwargs)
        self.operpsnAddSer = OperpsnAddService(self.inputKV)

    @decorator(["setupDelOneOperpsn","tearDownDelOneOperpsn"])
    def delOperpsn(self):
        self.sendHttpReq()

if __name__ == "__main__":
   alertjson = {
					"title"         :  "Makeblock 2017 品牌视频",
					"picPath"       : "http://uat-steam.opg.cn/_static/admin/images/resource/20180425112224_258421.jpg",
					"position"      : "03",
					"oldListOrder"  : 1,
					"listOrder"     : 1,
					"displayType"   : "1",
                    "resourceId"    : 121,
					"itemId"         : 121,
					"id"              :  52,
                    "token"          :  "69a42b2f9ebd4275a04a602648d857c1"
			    }
   operAlertSer = OperpsnAlertService(alertjson)
   addrsp = operAlertSer.addOneOperpsn()
   alertRsp = operAlertSer.alertOperpsn()
   print(alertRsp)
   code = operAlertSer.getRetCodeOperpsnRsp(alertRsp)
   print("code=%s" % code)
   delRsp = operAlertSer.delOperpsn()
   print("delRsp=%s" % delRsp)