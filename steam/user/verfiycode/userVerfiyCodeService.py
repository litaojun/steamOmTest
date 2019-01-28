#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userVerfiyCodeService.py 
@time: 2018/6/5 16:49 
"""
from opg.util.uopService import UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import weixinUserVerifyCodeurl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserVerfiyCodeReq,weixinUserVerfiyCodeRspFmt
from opg.util.redisUtil import RedisOper
from steam.util.httpUopService import  HttpUopService
from opg.util.uopService import UopService,decorator
class WeixinUserVerfiyCodeService(HttpUopService):
    '''
        微信端用户登录
    '''
    __interfaceName__ = "/passport/verifyCode"
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(WeixinUserVerfiyCodeService, self).__init__("",
                                                          "",
                                                          kwargs ,
                                                          reqjsonfile = None)
        self.rsp = None
        self.userVerfiyCodeReqjson = self.reqjsondata

    def sendUserVerifyCode(self):
        self.rsp = self.sendHttpReq()
        return self.rsp

    def getVerfiyCodeFromRedisByPhone(self,phoneNum = "",scenes = ""):
        if phoneNum is None or phoneNum == "":
           phoneNum = self.inputKV["phoneNo"]
        if scenes is None or scenes == "":
           scenes = self.inputKV["scenes"]
        curRedis   = RedisOper()
        verfiyCode = curRedis.getSteamVerCodeByPhone(phone  = phoneNum,
                                                     scenes = scenes)
        return verfiyCode

    @decorator(["setupSendVerifyCode","tearDownSendVerifyCode"])
    def setInPutData(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        self.inputKV["verfiyCode"]           = self.getVerfiyCodeFromRedisByPhone()
        if "newPhoneNo" in self.inputKV:
            self.inputKV["alterPhoneNoVfycode"] = self.getVerfiyCodeFromRedisByPhone(phoneNum = self.inputKV["newPhoneNo"],
                                                                                          scenes = self.inputKV["alertScenes"])

    @decorator(["setupSetRspToNone"])
    def setRspToNone(self):
        self.rsp = None

    @decorator("setupAlertSendVerifyCode")
    def getAlertPhoneVerifyCode(self):
        self.inputKV["alterPhoneNoVfycode"] = self.getVerfiyCodeFromRedisByPhone(phoneNum = self.inputKV["alertPhoneNo"] ,
                                                                                    scenes   = self.inputKV["alertScenes"])


if __name__ == "__main__":
   args = {
              "phoneNo":"18516099506",
              "loginType":"NM",
              "password":"",
              "scenes":"OTP"
          }
   weixinUserVerfiyCodeSer =  WeixinUserVerfiyCodeService(kwargs=args)
   rsp = weixinUserVerfiyCodeSer.sendUserVerifyCode()
   retcode = weixinUserVerfiyCodeSer.getRetcodeByUserLoginRsp(response=rsp)
   if retcode == "000000":
       vercode = weixinUserVerfiyCodeSer.getVerfiyCodeFromRedisByPhone(phoneNum=args["phoneNo"])
       print("verfiycode=%s" % vercode)