#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: httpUopService.py 
@time: 2018/11/16 16:09 
"""
from opg.util.utils import query_json
from opg.util.uopService import UopService,loadStrFromFile,decorator,resultData
from steam.mockhttp.flaskHttpServer import httpData
from opg.util.httptools import httpPost,httpGet,httpDelete,httpPostFile,httpPutGet


import json,os
class HttpUopService(UopService):
      """
         增加根据URL发送HTTP请求
      """
      def __init__( self,module    = None ,
                         filename  = None ,
                         sqlvaluedict = None ,
                         reqjsonfile  = None,
                         dbName       = "resource"):
          super(HttpUopService, self).__init__(module    = module  ,
                                               filename  = filename ,
                                               sqlvaluedict = sqlvaluedict ,
                                               reqjsonfile  = reqjsonfile ,
                                               dbName       = dbName)

      # @decorator(["setupUserAppleMatch"])
      def sendHttpReq(self):
          urlPathSign = self.__class__.__interfaceName__
          method        = httpData[urlPathSign][0]
          reqFormatPath = httpData[urlPathSign][1][self.inputKV["reqjsonfile"] if "reqjsonfile" in self.inputKV else "formatone"][1]
          url           = httpData[urlPathSign][2]
          reqDataFmt    = loadStrFromFile(reqFormatPath)
          reqdata       = reqDataFmt % self.inputKV
          self.jsonheart = {
                                  "x-token": "admin",
                                  "memberId": self.inputKV["memberId"] if "memberId" in self.inputKV else "",
                                  "token": self.inputKV["token"] if "token" in self.inputKV else ""
                            }
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
                  self.files = {'file': open(self.filepath % self.inputKV['file'], 'rb')}
                  self.rsp = httpPostFile(url = url , headers=self.jsonheart,file = self.files)
             elif method == "put-get":
                 self.rsp = httpPutGet(url     = url + self.reqjsondata,
                                       headers = self.jsonheart)
          else:
              try:
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
          print("s")
          return query_json(json_content = json.loads(self.rsp),
                                   query = format)