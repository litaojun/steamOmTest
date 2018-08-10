#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userLoginService.py 
@time: 2018/6/5 14:33 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import weixinUserLoginurl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserLoginReq,weixinUserLoginRspFmt
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from opg.util.httptools import httpGet,httpPost
class WeixinUserLoginService(UopService):
    '''
        微信端用户登录
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(WeixinUserLoginService, self).__init__("", "", kwargs , reqjsonfile = weixinUserLoginReq)
        self.rsp = None
        self.weixinUserLoginReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }
        kwargs["scenes"] = "OTP"
        self.userVerfiyCodeSer = WeixinUserVerfiyCodeService(kwargs=kwargs)

    def weixinUserLogin(self):
        self.rsp = httpPost(url         = weixinUserLoginurl,
                            headers     = self.jsonheart,
                            reqJsonData = self.weixinUserLoginReqjson)
        return self.rsp


    def getMemberIdFromRsp(self,response=None):
        return query_json(json_content=json.loads(response), query="data.memberId")

    def getTokenFromRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="token")

    @check_rspdata(filepath=weixinUserLoginRspFmt)
    def getRetcodeByUserLoginRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

if __name__ == "__main__":
   args = {
              "phoneNo":"18916899938",
              "loginType":"NM",
              "verfiyCode":"",
              "scenes":"OTP"
          }
   userVerfiyCodeSer = WeixinUserVerfiyCodeService(kwargs=args)
   verifyRsp = userVerfiyCodeSer.sendUserVerifyCode()
   vercode = userVerfiyCodeSer.getVerfiyCodeFromRedisByPhone(phoneNum=args["phoneNo"])
   args["verfiyCode"] = vercode
   weixinUserLoginSer =  WeixinUserLoginService(kwargs=args)
   rsp = weixinUserLoginSer.weixinUserLogin()
   memberId = weixinUserLoginSer.getMemberIdFromRsp(response=rsp)
   print("%s,%s,%s,%s")