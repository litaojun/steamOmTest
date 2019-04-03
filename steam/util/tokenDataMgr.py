from opg.util.httptools import httpPost,httpGet,httpDelete,httpPostFile,httpPutGet
from steam.mockhttp.util.initFile import generateUrlToFilePath
from steam.util.configIni import basePath,phoneCf
from steam.util.steamRedisData import getVerifyCodeUserType
import json
from opg.util.utils import query_json
from collections import defaultdict
urldata = generateUrlToFilePath()
class TokenData():
      sign = True
      def __init__(self):
          self.urlDict = {
                            "weixin":{ "codeurl":"/passport/verifyCode",
                                        "loginurl":"/member/login/memberLogin"},
                            "admin": { "codeurl": "/operation-manage/permission/admin/SmsCodeSend",
                                        "loginurl": "/operation-manage/permission/admin/login"},
                            "merchants": { "codeurl": "/merchant/passport/verifyCode",
                                            "loginurl": "/merchant-service/merchant/login" },
                         }
          self.tkdict =  defaultdict(lambda x:{})
          if TokenData.sign:
             self.initTokenData()
             TokenData.sign = False

      #根据用户类型获取配置的手机号码
      def getPhoneNumByUserType(self,urlSign="weixin",adminType="admin"):
          userType = urldata[urlSign][5]
          if userType in ["weixin","merchants"]:
              phoneNum = phoneCf.get(userType, "phoneNums")
          else:
              phoneNum = phoneCf.get(userType,adminType)
          return phoneNum

      #根据配置的手机号初始化Token
      def initTokenData(self):
          wx_token = self.weixinLogin(phoneNum=phoneCf.get("weixin","phoneNums"))
          cms_admin_token = self.cmsLogin(phoneNum=phoneCf.get("admin","admin"))
          cms_operate_token = self.cmsLogin(phoneNum=phoneCf.get("admin", "operate"))
          cms_merchants_token = self.cmsLogin(phoneNum=phoneCf.get("admin", "merchants"))
          hx_merchants_token = self.merchantsLogin(phoneNum=phoneCf.get("merchants","phoneNums"))
          self.tkdict["weixin"][phoneCf.get("weixin","phoneNums")] = wx_token
          self.tkdict["cms"]["admin"] = {}
          self.tkdict["cms"]["operate"] = {}
          self.tkdict["cms"]["merchants"] = {}
          self.tkdict["cms"]["admin"][phoneCf.get("admin","admin")] = cms_admin_token
          self.tkdict["cms"]["operate"][phoneCf.get("admin", "operate")] = cms_operate_token
          self.tkdict["cms"]["merchants"][phoneCf.get("admin", "merchants")] = cms_merchants_token
          self.tkdict["merchants"][phoneCf.get("merchants", "phoneNums")] = hx_merchants_token

      #根据Url获取默认登录的token
      def getTokenByUserType(self,urlSign='',adminType="admin"):
          token = "sssssssssssssssss"
          phoneNum = self.getPhoneNumByUserType(urlSign,adminType)
          userType = urldata[urlSign][5]
          if userType in ["weixin","merchants"]:
             token = self.tkdict[userType][phoneNum]
          elif userType == "admin":
               token = self.tkdict[userType][adminType][phoneNum]
          return token

      #根据手机号码获取token，针对CMS
      def getTokenBytUserPhone(self,userPhone=""):
          if userPhone == phoneCf.get("admin","admin"):
              token = self.tkdict["cms"]["admin"][userPhone]
          elif userPhone == phoneCf.get("admin", "operate"):
              token = self.tkdict["cms"]["operate"][userPhone]
          elif userPhone == phoneCf.get("admin", "merchants"):
              token = self.tkdict["cms"]["merchants"][userPhone]
          else:
              token = self.cmsLogin(phoneNum=userPhone)
          return token

      def login(self,phoneNum="",vfyUrl="",lgUrl="",lgDataBy={},vfyCodeName="code",queryTokenFmt="data.token"):
          dataBody = { "phoneNo": phoneNum }
          rsp = httpPost(url=vfyUrl , reqJsonData=dataBody)
          print("phoneNum=%s,vfyUrl-rsp:%s" % (phoneNum,rsp) )
          retcode = query_json(json_content=json.loads(rsp),query="code")
          if retcode == "000000":
              verifyCode = getVerifyCodeUserType("admin",phoneNum)
              print("verifyCode:%s" % verifyCode)
              lgDataBy[vfyCodeName] = verifyCode
              rsp = httpPost(url=lgUrl, reqJsonData=lgDataBy)
              print("lgDataBy-rsp:%s" % rsp)
              return query_json(json_content=json.loads(rsp),query=queryTokenFmt)

      def cmsLogin(self,phoneNum=""):
          print("cmsLogin")
          vfySign = self.urlDict["admin"]["codeurl"]
          lgSign = self.urlDict["admin"]["loginurl"]
          vfyUrl = urldata[vfySign][2]
          lgUrl  = urldata[lgSign][2]
          lgDataBy = { "phoneNo":"18916899938","code":"430280" }
          vfyCodeName = "code"
          queryTokenFmt = "data.token"
          return self.login(phoneNum=phoneNum,
                            vfyUrl=vfyUrl,
                            lgUrl=lgUrl,
                            lgDataBy=lgDataBy,
                            vfyCodeName=vfyCodeName,
                            queryTokenFmt=queryTokenFmt)

      def weixinLogin(self,phoneNum=""):
          print("weixinLogin")
          vfySign = self.urlDict["weixin"]["codeurl"]
          lgSign = self.urlDict["weixin"]["loginurl"]
          vfyUrl = urldata[vfySign][2]
          lgUrl  = urldata[lgSign][2]
          lgDataBy = {
                            "loginName": "15221874610",
                            "loginType": "NM",
                            "password": "000000",
                            "inviterId": "",
                            "partnerInfo": {
                                "partnerName": "WX",
                                "partnerMemberId": "oJ3wwxO7th7tBYDVGTbZWkqdLt2A"
                            },
                            "adInfo": {
                                "source": "",
                                "medium": "",
                                "campaign": "",
                                "content": "",
                                "term": "",
                                "sourceType": ""
                            }
                    }
          vfyCodeName = "password"
          queryTokenFmt = "token"
          return self.login(phoneNum=phoneNum,
                            vfyUrl=vfyUrl,
                            lgUrl=lgUrl,
                            lgDataBy=lgDataBy,
                            vfyCodeName=vfyCodeName,
                            queryTokenFmt=queryTokenFmt)

      def merchantsLogin(self,phoneNum=""):
          print("merchantsLogin")
          vfySign  = self.urlDict["merchants"]["codeurl"]
          lgSign   = self.urlDict["merchants"]["loginurl"]
          vfyUrl   = urldata[vfySign][2]
          lgUrl    = urldata[lgSign][2]
          lgDataBy = { "phoneNo":"18916899938","code":"430280" }
          vfyCodeName   = "code"
          queryTokenFmt = "token"
          return self.login(phoneNum=phoneNum,
                            vfyUrl=vfyUrl,
                            lgUrl=lgUrl,
                            lgDataBy=lgDataBy,
                            vfyCodeName=vfyCodeName,
                            queryTokenFmt=queryTokenFmt)
tokenData = TokenData()

if __name__ == "__main__":
    token = tokenData["weixin"]["18916899938"]
    print("token=%s" % token)