from opg.util.utils import query_json
from opg.bak.uopService import UopService,loadStrFromFile,resultData
from steam.util.formatJsonFile import loadJsonFromFile
from steam.mockhttp.flaskHttpServer import httpData
from opg.util.httptools import httpPost,httpGet,httpDelete,httpPostFile,httpPutGet,httpReqSend
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

      def genCaseByFmtOrInputKV(self,reqJsonDataFmt = None):
          reqData = {}
          if reqJsonDataFmt is not None:
              for caseKey in reqJsonDataFmt :
                  if caseKey in self.inputKV :
                     reqData[caseKey] = self.inputKV[caseKey]
                  elif reqJsonDataFmt.get(caseKey) is not None:
                      reqData[caseKey] = reqJsonDataFmt[caseKey]
          return reqData

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
          reqjsonfile = self.inputKV["reqjsonfile"] if "reqjsonfile" in self.inputKV else "formatone"
          reqFormatPath  = httpData[urlPathSign][1][reqjsonfile][0]
          reqJsonDataFmt = loadJsonFromFile(reqFormatPath)
          self.genReqHeaderByUrl(urlSign=urlPathSign)
          if reqdata is None:
             self.reqjsondata = self.genCaseByFmtOrInputKV(reqJsonDataFmt=reqJsonDataFmt)
          else:
              self.reqjsondata = reqdata
          self.rsp = httpReqSend(url=url,headers=self.jsonheart,reqJson=self.reqjsondata,
                                 fileName=self.inputKV.get('file',None),method=method)
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


if __name__ == "__main__":
    httpPost(url="https://uat-steam-api.opg.cn/operation-manage/course/removeCourse",
             headers={"login_type":"CMS","token":"9e8a038e5bb84cd49fa0e1e35aa8ed35"},
             reqJsonData={"resourceId": 5318})