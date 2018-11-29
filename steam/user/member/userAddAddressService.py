#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userAddAddressService.py 
@time: 2018/7/24 15:35 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userAddAddressUrl
from opg.util.schemajson import check_rspdata
from opg.util.httptools import httpGet,httpPost
from steam.util.httpUopService import  HttpUopService
class UserAddAddressService(HttpUopService):
    '''
        微信端用户获取地址列表
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserAddAddressService, self).__init__("", "", kwargs)

    @decorator(["setupUserAddAddress"])
    def userAddAddressReq(self):
        self.rsp = self.sendHttpReq()
        return self.rsp

    # @check_rspdata(filepath="userAddAddressRspFmt")
    # def getRetcodeByRsp(self,response = None):
    #     return query_json(json_content= json.loads(response),
    #                       query       = "code")

if __name__ == "__main__":
    kwargs = {
                    "consignee": "李菠萝",
                    "phone": "18916899938",
                    "address": "空空",
                    "addressCode": "110000,110100,110101",
                    "province": "北京市",
                    "city": "市辖区",
                    "county": "东城区",
                    "isDefault": "01",
                     "memberId": "e99abfeb-1ae5-41d8-a422-63bc108026d4"
                }
    mass = UserAddAddressService(kwargs=kwargs)
    rsp = mass.userAddAddressReq()
    retcode = mass.getRetcodeByRsp(response=rsp)
    print(retcode)