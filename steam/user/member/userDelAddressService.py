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
from opg.bak.uopService import decorator
from steam.user.member.memberAddressService import MemberAddressService
from steam.util.configurl import userAddAddressUrl
from opg.util.httptools import httpPost
from steam.util.httpUopService import  HttpUopService
class UserDelAddressService(HttpUopService):
    '''
        微信端用户获取地址列表
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserDelAddressService, self).__init__(module   = "",
                                                    filename = "",
                                                    sqlvaluedict = kwargs)

    @decorator(["tearDownDelUserAddress"])
    def userDelAddressReq(self):
        self.rsp = self.sendHttpReq()
        return self.rsp

    @decorator(["preInterfaceUserAddAddress"])
    def userAddAddressReq(self):
        reqjson = {
                        "consignee": self.inputKV["consignee"],
                        "phone"    : self.inputKV["phone"],
                        "address"  : self.inputKV["address"],
                        "addressCode": self.inputKV["addressCode"],
                        "province"   : self.inputKV["province"],
                        "city"     : self.inputKV["city"],
                        "county"   : self.inputKV["county"],
                        "isDefault": self.inputKV["isDefault"]
                    }
        self.rsp = httpPost(
                                url         = userAddAddressUrl,
                                reqJsonData = reqjson,
                                headers     = self.jsonheart
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