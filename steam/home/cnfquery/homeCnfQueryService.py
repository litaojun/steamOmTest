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
pagetype = "0"
def selectFmtPath(sign = "0"):
    filepath = homeConfigQueryRspFmt
    if sign == "0":
        filepath = homeConfigQueryRspFmt
    return filepath

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
                                        url=homeConfigQueryurl+self.homeCnfQueryReqjson,
                                        #json=self.homeCnfQueryReqjson,
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

if __name__ == "__main__":
    kwargs = {
                "phoneNo":"18916899938",
                "memberId":"0e399155-0a89-40e7-8177-e032984bf87c"
             }
    homeCnfSer = HomeCnfQueryService(kwargs=kwargs)
    homeRsp = homeCnfSer.queryHomePageCnf()
    retcode = homeCnfSer.getRetcodeByActivityRsp(response=homeRsp)
    print("retcode=%s" % retcode)