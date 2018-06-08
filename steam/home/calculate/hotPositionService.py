#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: hotPositionService.py 
@time: 2018/6/6 17:37 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import hotPositonUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import homePositionReq,homePositionRspFmt
class HomeHotPositionService(UopService):
    '''
        首页热门推荐计算内容
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(HomeHotPositionService, self).__init__("", "", kwargs , reqjsonfile = homePositionReq)
        self.rsp = None
        self.homeHotPostionReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def queryHomeHotPosition(self):
        hotPositionRsp = requests.get(
                                        url=hotPositonUrl+self.homeHotPostionReqjson,
                                        headers=self.jsonheart,
                                        verify=False
                                      )
        self.rsp = hotPositionRsp.text
        print("homePageCnfRsp = %s" % hotPositionRsp.text)
        return hotPositionRsp.text

    #@check_rspdata(filepath=homePositionRspFmt)
    def getRetcodeByActivityRsp(self,response = None):
        print("homePageCnfRsp=" + str(response))
        return query_json(json_content=json.loads(response), query="code")

if __name__ == "__main__":
    kwargs = {
                "phoneNo":"18916899938",
                "memberId":"0e399155-0a89-40e7-8177-e032984bf87c"
             }
    hotPositionSer = HomeHotPositionService(kwargs = kwargs)
    hotRsp = hotPositionSer.queryHomeHotPosition()
    retcode = hotPositionSer.getRetcodeByActivityRsp(response=hotRsp)
    print(retcode)