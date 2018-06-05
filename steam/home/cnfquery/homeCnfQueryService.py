#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: homeCnfQueryService.py 
@time: 2018/6/4 17:59 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import homeConfigQueryurl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import homeConfigQueryReq,homeConfigQueryRspFmt
class HomeCnfQueryService(UopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(HomeCnfQueryService, self).__init__("", "", kwargs , reqjsonfile = homeConfigQueryReq)
        self.rsp = None
        self.homeCnfQueryReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def queryHomePageCnf(self):
        homePageCnfRsp = requests.get(
                                        url=homeConfigQueryurl,
                                        json=self.homeCnfQueryReqjson,
                                        headers=self.jsonheart,
                                        verify=False
                                      )
        self.rsp = homePageCnfRsp.text
        print("homePageCnfRsp = %s" % homePageCnfRsp.text)
        return homePageCnfRsp.text

    @check_rspdata(filepath=homeConfigQueryRspFmt)
    def getRetcodeByActivityRsp(self,response = None):
        print("homePageCnfRsp=" + str(response))
        return query_json(json_content=json.loads(response), query="code")