from opg.util.utils import query_json
from opg.bak.uopService import UopService,loadStrFromFile,resultData
from steam.mockhttp.flaskHttpServer import httpData
from opg.util.httptools import httpPost,httpGet,httpDelete,httpPostFile,httpPutGet
import json,os
from opg.util.lginfo import logger

from steam.util.tokenDataMgr import tokenData
class HttpUopService(UopService):
      """
         增加根据URL发送HTTP请求
      """
      def __init__( self,module    = None ,
                         filename  = None ,
                         sqlvaluedict = None ,
                         reqjsonfile  = None,
                         dbName       = None):
          super(HttpUopService, self).__init__(module    = module  ,
                                               filename  = filename ,
                                               sqlvaluedict = sqlvaluedict ,
                                               reqjsonfile  = reqjsonfile ,
                                               dbName       = dbName)
          self.jsonheart = {}

      def structReqData(self):
          urlPathSign = self.__class__.__interfaceName__
          reqFormatPath  = httpData[urlPathSign][1][ self.inputKV["reqjsonfile"] if "reqjsonfile" in self.inputKV else "formatone" ][1]
          reqDataFmt     = loadStrFromFile(reqFormatPath)
          reqdata        = reqDataFmt % self.inputKV
          return reqdata

      def genReqHeader(self,urlSign = None):
          userType   = httpData[urlSign][5]
          permission = httpData[urlSign][6]
          phoneNum = self.inputKV.get("phoneNum",None)
          if userType in ("weixin","merchants"):
             if permission is None and phoneNum is None:
                self.jsonheart["token"] = tokenData.getTokenByUrl(urlsign=urlSign)
             elif phoneNum is not None and permission is None:
                 self.jsonheart["token"] = tokenData.getTokenBytUserPhone(userPhone=phoneNum)
             elif phoneNum is not None and permission is not None:
                 pass
          elif userType == "admin":
              pass

      def genReqHeaderByUrl(self,urlSign = None):
          utToTokenType = { "admin":"CMS","weixin":"","merchants":"MERCHANT" }
          userType = httpData[urlSign][5]
          permission = httpData[urlSign][6]
          phoneNum = self.inputKV.get("phoneNum", None)
          token = None
          if userType in ["admin","merchants"]:
             self.jsonheart["login_type"] = utToTokenType[userType]
          if phoneNum is not None and permission is not None and permission == "kong":
              token = None
          elif phoneNum is not None:
              token = tokenData.getTokenBytUserPhone(userPhone=phoneNum,userType=userType)
          elif phoneNum is None:
              token = tokenData.getTokenByUrl(urlSign=urlSign,adminType=permission)
          if userType in ("weixin", "admin"):
              if token is not None:
                  self.jsonheart["token"] = token
              if userType == "weixin":
                  memberId = tokenData.getMemberIdByToken(token=token)
                  self.jsonheart["memberId"] = memberId
                  self.inputKV["memberId"] = memberId
          elif userType == "merchants":
              if token is not None:
                  self.jsonheart["merchant_token"] = token




      def sendHttpReq(self,reqdata=None):
          urlPathSign    = self.__class__.__interfaceName__
          method         = httpData[urlPathSign][0]
          url            = httpData[urlPathSign][2]
          reqFormatPath  = httpData[urlPathSign][1][ self.inputKV["reqjsonfile"] if "reqjsonfile" in self.inputKV else "formatone" ][1]
          reqDataFmt     = loadStrFromFile(reqFormatPath)
          self.genReqHeaderByUrl(urlSign=urlPathSign)
          if reqdata is None:
             reqdata        = reqDataFmt % self.inputKV
          else:
              self.reqjsondata = reqdata
          # if "userType" in self.inputKV :
          #     if self.inputKV["userType"] == "admin":
          #        token = self.inputKV["admin-token"]
          #     elif self.inputKV["userType"] == "weixin":
          #         token = self.inputKV["user-token"]
          # else:
          #     token = self.inputKV["token"] if "token" in self.inputKV else ""
          # self.jsonheart = {
          #                         "x-token": "admin",
          #                         "memberId": self.inputKV["memberId"] if "memberId" in self.inputKV else "",
          #                         "token": token ,
          #                         "merchant_token": self.inputKV["merchant_token"] if "merchant_token" in self.inputKV else ""
          #                   }
          # self.jsonheart={}
          if method in ("get","delete","file","put-get") :
             self.reqjsondata = reqdata
             if method   == "get":
                self.rsp =  httpGet(url     = url + self.reqjsondata ,
                                    headers = self.jsonheart)
             elif method  == "delete":
                  self.rsp =   httpDelete(url     = url + self.reqjsondata ,
                                          headers = self.jsonheart)
             elif method  == "file":
                  self.filepath = os.getcwd() + os.path.sep + "steamcase" + os.path.sep + "%s"
                  self.files = {'file': open(self.inputKV['file'], 'rb')}
                  self.rsp = httpPostFile(url = url , headers=self.jsonheart,file = self.files)
             elif method == "put-get":
                 self.rsp = httpPutGet(url     = url + self.reqjsondata,
                                       headers = self.jsonheart)
          else:
              try:
                  if  type(reqdata) == str :
                      self.reqjsondata = eval(reqdata)
                  if method == "post":
                     self.rsp = httpPost( url         = url ,
                                          headers     = self.jsonheart,
                                          reqJsonData = self.reqjsondata )
                  elif method == "put":
                       self.rsp = httpDelete( url = url )
              except Exception as e:
                  raise e
          return  self.rsp

      @resultData(param="getRetcodeByRsp")
      def getRetcodeByRsp( self,
                           response = None ,
                           format   = "code" ):
          """

              :param matchRsp:
              :return:
          """
          retcode = "000000"
          try:
             retcode = query_json(json_content = json.loads(self.rsp),
                                   query       = format)
          except Exception as e:
             print("返回报文异常")
             print(e)
             logger.info("返回报文异常")
             logger.info(e)
             retcode = "2000001"
          finally:
              return retcode