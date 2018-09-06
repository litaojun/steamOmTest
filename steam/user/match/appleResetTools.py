#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: appleResetTools.py 
@time: 2018/9/4 14:59 
"""
from opg.util.httptools import httpPost
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
import json,time
reqjson = {
    "envContext": {
        "ipAddress": "string",
        "traceInfo": {
            "spanId": "string",
            "traceId": "string"
        },
        "webToken": {
            "header": {
                "encryptType": "string",
                "tokenType": "string"
            },
            "payload": {
                "audience": "string",
                "expires": "string",
                "invalidBeforeTime": "string",
                "issuedTime": "string",
                "issuer": "string",
                "jsonWebTokenId": "string",
                "subjectId": "string"
            },
            "signature": "string"
        }
    }
}
args = {
    "phoneNo": "14988822212",
    "loginType": "NM",
    "verfiyCode": "000000",
    "scenes": "OTP",
}
appleJson = {
                "matchId": 22,
                "subMatchId": 1087,
                "subjectIdList": [1, 4, 6],
                "contactName": "李陶军",
                "contactPhone": "14988822212",
                "studentName": "5854990",
                "province": "上海",
                "city": "上海市",
                "country": "黄浦区",
                "group": "幼儿园",
                "school": "文庙路幼儿园",
                "nationality": "",
                "subMatchName": "自动化测试专用-勿动"
            }

cancelAppleMatchReq = {
                            "applyId":5854990
                      }
tokena = None

def appleRest():
    httpPost(url     = "http://10.205.248.165:20000/tool/applyNumsReset",
             headers = {},
             reqJsonData = reqjson)

def getTokenReset(phoneNo = None):
    if phoneNo is not None:
        args["phoneNo"] = phoneNo
    if tokena is None:
        WeixinUserVerfiyCodeService(kwargs=args).sendUserVerifyCode()
        userLoginSer = WeixinUserLoginService(kwargs=args)
        rsp          = userLoginSer.weixinUserLogin()
        return userLoginSer.getTokenFromRsp(response=rsp)
    return  tokena

def userAppleMatch(phoneNo = None,memberId = None,ip = None):
    #token = getTokenReset()
    #print("token=%s" % token)
    heartJson = {"memberId":memberId,"Content-Type":"application/json"}
    appleJson["contactPhone"] = phoneNo
    print(appleJson)
    rsp = httpPost(url         = "http://%s/match-service/member/apply" % ip ,
                   headers     = heartJson ,
                   reqJsonData = appleJson)
    print(rsp)

def userAppleMatchTwo():
    m = [{
           "phoneNo":"14776006716",
           "memberId":"00033c93-0b95-4610-af41-466620f245e4",
           "ip":"10.205.248.99:20000"
         },{
           "phoneNo":"14776042732",
           "memberId":"00070862-934a-463c-a7a6-61af09c1eb2c",
           "ip":"10.205.248.165:20000"
         }
        ]
    time.sleep(60)
    for a in m:
        userAppleMatch(phoneNo=a["phoneNo"],
                       memberId=a["memberId"],
                       ip=a["ip"])

def getUserAppleMatchCode():
    token = getTokenReset()
    print("token=%s" % token)
    heartJson = {
                   "token":token,
                   "Content-Type":"application/json"
                }
    rsp = httpPost(url         = "https://uat-steam-api.opg.cn/match-service/member/mp/query" ,
                   headers     = heartJson ,
                   reqJsonData = {"matchId":22})
    print(rsp)
    rsp = json.loads(rsp)
    if len(rsp["applyInfoList"]) > 0:
        cancelAppleMatchReq["applyId"] = rsp["applyInfoList"][0]["applyCode"]
        return rsp["applyInfoList"][0]["applyCode"]

def userCancelAppleMatch():
    token = getTokenReset()
    print("token=%s" % token)
    heartJson = {"token":token,"Content-Type":"application/json"}
    getUserAppleMatchCode()
    rsp = httpPost(url         = "https://uat-steam-api.opg.cn/match-service/member/apply/cancel" ,
                   headers     = heartJson ,
                   reqJsonData = cancelAppleMatchReq)
    print(rsp)

def userCancelAppleMatchByMatchId(appleMatchId = None):
    cancelAppleMatchReq["applyId"] = appleMatchId
    userCancelAppleMatch()




if __name__ == "__main__":
    # userAppleMatch()
    # applecode = getUserAppleMatchCode()
    # userCancelAppleMatch()
    #appleRest()
    #userCancelAppleMatchByMatchId(appleMatchId=5855041)
    # appleRest()
    # userAppleMatch()
    # matchCode = getUserAppleMatchCode()
    # print(matchCode)
    # import time
    # time.sleep(60)
    userAppleMatchTwo()