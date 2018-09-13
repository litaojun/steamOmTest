#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: memberAddressService.py 
@time: 2018/7/10 16:08 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import memberAddressUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import memberAddressRspFmt
from opg.util.httptools import httpGet
class MemberAddressService(UopService):
    '''
        微信端用户新增一个地址
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(MemberAddressService, self).__init__("", "", kwargs )

    def memberAddressReq(self):
        self.rsp = httpGet(url     = memberAddressUrl,
                           headers = self.jsonheart)
        return self.rsp

    def getMemberAddressIdFromRsp(self,response=None):
        if response is None:
            response = self.memberAddressReq()
        return query_json(json_content = json.loads(response),
                          query        = "data.0.id")

    def getMemberAddressIdByNameOrTel(self,response = None,conName="",conTel=""):
        if response is None:
            response = self.memberAddressReq()
        id = None
        adsLs = query_json(json_content = json.loads(response),
                           query        = "data")
        for address in adsLs:
            if address["consignee"] == conName and address["phone"] == conTel:
                id = address["id"]
                break
        return id

    @check_rspdata(filepath=memberAddressRspFmt)
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

    def setInPutData(self):
        memberAddrId               = self.getMemberAddressIdFromRsp()
        self.inputKV["addressId"] = memberAddrId

if __name__ == "__main__":
    kwargs = {
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4"
             }
    mass = MemberAddressService(kwargs=kwargs)
    rsp = mass.memberAddressReq()
    retcode = mass.getRetcodeByRsp(response=rsp)
    print(retcode)
    addressId = mass.getMemberAddressIdFromRsp(response=rsp)
    print(addressId)
