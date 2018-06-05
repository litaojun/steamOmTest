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
from opg.util.redisUtil import redisOper
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

    def weixinUserLogin(self):
        weixinUserLoginRsp = requests.get(
                                        url=weixinUserLoginurl,
                                        json=self.weixinUserLoginReqjson,
                                        headers=self.jsonheart,
                                        verify=False
                                      )
        self.rsp = weixinUserLoginRsp.text
        print("homePageCnfRsp = %s" % weixinUserLoginRsp.text)
        return weixinUserLoginRsp.text

    @check_rspdata(filepath=weixinUserLoginRspFmt)
    def getRetcodeByUserLoginRsp(self,response = None):
        print("homePageCnfRsp=" + str(response))
        return query_json(json_content=json.loads(response), query="code")

if __name__ == "__main__":
   args = {
              "loginName":"18916899938",
              "loginType":"NM",
              "password":""
          }
   weixinUserLoginSer =  WeixinUserLoginService(kwargs=args)
   weixinUserLoginSer.weixinUserLogin()