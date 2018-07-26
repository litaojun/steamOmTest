#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userDelAddressService.py 
@time: 2018/7/24 16:13 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.user.member.memberAddressService import MemberAddressService
from steam.util.configurl import userDelAddressUrl,userAddAddressUrl
from opg.util.schemajson import check_rspdata
from opg.util.httptools import httpDelete,httpPost
class UserDelAddressService(UopService):
    '''
        微信端用户获取地址列表
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserDelAddressService, self).__init__("", "", kwargs ,reqjsonfile="userDelAddressReq")

    def userDelAddressReq(self):
        self.rsp = httpDelete(url     = userDelAddressUrl + self.reqjsondata,
                              headers = self.jsonheart)
        return self.rsp

    @check_rspdata(filepath="userDelAddressRspFmt")
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    @decorator(["preInterfaceUserAddAddress"])
    def userAddAddressReq(self):
        reqjson = {
                        "consignee": self.inputKV["consignee"],
                        "phone": self.inputKV["phone"],
                        "address": self.inputKV["address"],
                        "addressCode": self.inputKV["addressCode"],
                        "province": self.inputKV["province"],
                        "city": self.inputKV["city"],
                        "county": self.inputKV["county"],
                        "isDefault": self.inputKV["isDefault"]
                    }
        self.rsp = httpPost(
                                url     = userAddAddressUrl,
                                reqJsonData = reqjson,
                                headers = self.jsonheart
                            )
        addressId = MemberAddressService(kwargs=self.inputKV).getMemberAddressIdByNameOrTel(conName=reqjson["consignee"],
                                                                                             conTel=reqjson["phone"])
        self.inputKV["addressId"]=addressId
        self.reqjsondata = "?id=%(addressId)s" % self.inputKV



if __name__ == "__main__":
    kwargs = {
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "addressId":"25d0c849-8f18-11e8-9033-02a7e93155ea"
             }
    mass = UserDelAddressService(kwargs=kwargs)
    rsp = mass.userDelAddressReq()
    retcode = mass.getRetcodeByRsp(response=rsp)
    print(retcode)