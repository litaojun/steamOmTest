#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: steamLog.py 
@time: 2018/6/5 14:14 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from steam.admin.login.userLoginService import UserLoginService
from steam.user.login.QueryMemberIdService import QueryMemberIdService

class SteamTestCase(ParametrizedTestCase):
    '''
          用户进入公众号首页，获取运营位数据
    '''
    __interfaceName__ = "/featured/index/configs/queryShowConfigs"
    memberIdDict      = {}

    def __init__(self, methodName='runTest', param=None):
        super(SteamTestCase, self).__init__(methodName, param)

    def getInputData(self):
        inputData = super(SteamTestCase, self).getInputData()
        if "phoneNo" in inputData:
            if inputData["phoneNo"] in SteamTestCase.memberIdDict:
               inputData["token"]    = SteamTestCase.memberIdDict[inputData["phoneNo"]][0]
               inputData["memberId"] = SteamTestCase.memberIdDict[inputData["phoneNo"]][1]
            else:
               inputData["scenes"] = "OTP"
               userVerCodeSer = WeixinUserVerfiyCodeService(kwargs=inputData)
               sedCodeRsp     = userVerCodeSer.sendUserVerifyCode()
               retcode        = userVerCodeSer.getRetcodeByRsp(response=sedCodeRsp)
               if retcode == "000000":
                  verfiyCode               = userVerCodeSer.getVerfiyCodeFromRedisByPhone(phoneNum=inputData["phoneNo"])
                  inputData["verfiyCode"] = verfiyCode
                  userLoginSer             = WeixinUserLoginService(kwargs=inputData)
                  rsp  = userLoginSer.weixinUserLogin()
                  code = userLoginSer.getRetcodeByUserLoginRsp(response=rsp)
                  if code  == "000000":
                     token = userLoginSer.getTokenFromRsp(response=rsp)
                     inputData["token"] = token
                     qmIdSer = QueryMemberIdService(kwargs=inputData)
                     rsp     = qmIdSer.userMemberIdReq()
                     memberId               = qmIdSer.getMemberIdFromRsp(response=rsp)
                     inputData["memberId"] = memberId
                     SteamTestCase.memberIdDict[inputData["phoneNo"]] = (token,memberId)
        else:
             token               = UserLoginService.getTokenData()
             inputData["token"] = token
        return inputData

    def compareRetcodeTest(self):
        self.rsp     = self.myservice.sendHttpReq()
        retcode = self.myservice.getRetcodeByRsp(response = self.rsp)
        self.assertTrue(retcode == self.expectdata["code"])

    @classmethod
    def clearPhoneData(cls):
        cls.memberIdDict = {}

if __name__ == "__main__":
    args = {"phoneNo":"18916899938"}
    # testcase = SteamTestCase(args = )
    print(dir(SteamTestCase))


