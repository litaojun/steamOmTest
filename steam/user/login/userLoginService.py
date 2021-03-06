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
import json
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserLoginRspFmt
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from steam.user.login.QueryMemberIdService import QueryMemberIdService
from steam.util.httpUopService import  HttpUopService
from opg.bak.uopService import decorator
class WeixinUserLoginService(HttpUopService):
    '''
        微信端用户登录
    '''
    __interfaceName__ = "/member/login/memberLogin"
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(WeixinUserLoginService, self).__init__( module    = "" ,
                                                      filename  = "" ,
                                                      sqlvaluedict = kwargs ,
                                                      reqjsonfile  = None )
        self.weixinUserLoginReqjson = self.reqjsondata
        kwargs["scenes"] = "OTP"
        self.userVerfiyCodeSer = WeixinUserVerfiyCodeService(kwargs=kwargs)

    def weixinUserLogin(self):
        self.rsp = self.sendHttpReq()
        return self.rsp

    def getMemberIdFromRsp(self,response=None):
        return query_json(json_content = json.loads(response),
                          query        = "data.memberId")

    def getTokenFromRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "token")

    @check_rspdata(filepath=weixinUserLoginRspFmt)
    def getRetcodeByUserLoginRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

    @decorator(["setupGetPassportIdByPhoneNo"])
    def getPassportIdByPhoneNo(self):
        self.inputKV["passportId"] = self.selectBySqlName("setupDBselect_t_accessBy_phoneNo")

if __name__ == "__main__":
   args = {
              "phoneNo":"14988822212",
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
   print("login rsp=%s" % rsp)
   token = weixinUserLoginSer.getTokenFromRsp(response=rsp)
   print("token is %s" % (token))
   args["token"] = token
   a = QueryMemberIdService(kwargs = args)
   rsp = a.userMemberIdReq()
   memberId = a.getMemberIdFromRsp(response=rsp)
   print("memberId is %s" % (memberId))