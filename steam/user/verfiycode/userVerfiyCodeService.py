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
class WeixinUserVerfiyCodeService(UopService):
    '''
        微信端用户登录
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(WeixinUserVerfiyCodeService, self).__init__("", "", kwargs , reqjsonfile = weixinUserVerfiyCodeReq)
        self.rsp = None
        self.userVerfiyCodeReqjson = self.reqjsondata

    def sendUserVerifyCode(self):
        weixinUserLoginRsp = requests.post(
                                                url    = weixinUserVerifyCodeurl,
                                                json   = self.userVerfiyCodeReqjson,
                                                headers= self.jsonheart,
                                                verify = False
                                              )
        self.rsp = weixinUserLoginRsp.text
        print("userVerfiyCodeReqjson = %s" % self.userVerfiyCodeReqjson)
        print("homePageCnfRsp = %s" % weixinUserLoginRsp.text)
        return weixinUserLoginRsp.text

    @check_rspdata(filepath=weixinUserVerfiyCodeRspFmt)
    def getRetcodeByRsp(self,response = None):
        """
        :param response:
        :return:
        """
        return query_json(json_content = json.loads(response),
                          query        = "code")

    def getVerfiyCodeFromRedisByPhone(self,phoneNum = ""):
        if phoneNum is None or phoneNum == "":
            phoneNum = self.userVerfiyCodeReqjson["phoneNo"]
        curRedis   = RedisOper()
        verfiyCode = curRedis.getSteamVerCodeByPhone(phone  = phoneNum,
                                                     scenes = self.inputKV["scenes"])
        return verfiyCode

    def setInPutData(self):
        if self.rsp is None:
           self.rsp = self.sendUserVerifyCode()
        self.inputKV["verfiyCode"] = self.getVerfiyCodeFromRedisByPhone()


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