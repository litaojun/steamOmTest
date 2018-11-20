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
from opg.util.uopService import UopService,loadStrFromFile
from steam.mockhttp.flaskHttpServer import httpData
from opg.util.httptools import httpPost,httpGet,httpDelete
import json
class HttpUopService(UopService):
      """
         增加根据URL发送HTTP请求
      """
      def sendHttpReq(self,urlPathSign = None):
          method        = httpData[urlPathSign][0]
          reqFormatPath = httpData[urlPathSign][1]["formatone" if "reqjsonfile" in self.inputKV else self.inputKV["reqjsonfile"]][1]
          url           = httpData[urlPathSign][2]
          reqDataFmt    = loadStrFromFile(reqFormatPath)
          reqdata       = reqDataFmt % self.inputKV
          if method in ("get","delete") :
             self.reqjsondata = reqdata
             if method   == "get":
                self.rsp =  httpGet(url     = url,
                                    headers = self.jsonheart)
             elif method  == "delete":
                 self.rsp =   httpDelete(url     = url ,
                                         headers = self.jsonheart)
          else:
              try:
                  self.reqjsondata = eval(reqdata)
                  if method == "post":
                      self.rsp = httpPost(url         = url ,
                                          headers     = self.jsonheart,
                                          reqJsonData = self.reqjsondata)
                  elif method == "put":
                       self.rsp = httpDelete( url = url )
              except Exception as e:
                  raise e
          return  self.rsp

      def getRetcodeByRsp(rsp,format = "code"):
          """
              :param matchRsp:
              :return:
          """
          return query_json(json_content = json.loads(rsp),
                                   query = format)

