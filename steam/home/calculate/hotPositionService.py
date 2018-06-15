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
from opg.util.httptools import httpGet
from steam.home.cnfquery.homeCnfQueryService import HomeCnfQueryService
import operator as op
class HomeHotPositionService(HomeCnfQueryService):
    '''
        首页热门推荐计算内容
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(HomeHotPositionService, self).__init__(modul       = "weixin",
                                                     filename    = "cnfDataDb.xml",
                                                     kwarg       = kwargs,
                                                     reqjsonfile = homePositionReq)
        self.rsp = None
        self.homeHotPostionReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def queryHomeHotPosition(self):
        hotPositionRsp =  httpGet(
                                        url     = hotPositonUrl+self.homeHotPostionReqjson,
                                        headers = self.jsonheart
                                  )
        self.rsp = hotPositionRsp
        return hotPositionRsp

    @check_rspdata(filepath=homePositionRspFmt)
    def getRetcodeByActivityRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    def getAllCalculateDataByRsp(self,response = None):
        infosQuery = "showInfoPage.targets"
        curinfos = query_json(json_content=json.loads(response), query=infosQuery)
        return curinfos

    def getAllCnfListData(self,response = None):
        return self.getAllCalculateDataByRsp(response=response)

    def compareSerData(self,response=None,position="01",configSqlStr="select_t_sku_HomePage",calSqlStr = "select_t_resource_calculate"):
        rspDataLs = self.getAllCalculateDataByRsp(response=response)
        #self.dataFilterFields(dictData=rspDataLs)
        cnfDbdata = self.getDbPageDataBySql(configSqlStr=configSqlStr)
        calculateData = self.getDbPageDataBySql(configSqlStr=calSqlStr)
        a = rspDataLs[0:len(cnfDbdata)]
        x = cnfDbdata[position]
        sign = op.eq(a,x)
        b = rspDataLs[len(cnfDbdata):10]
        c = calculateData[position][0,len(b)]
        csign = op.eq(b,c)
        return sign & csign




if __name__ == "__main__":
    kwargs = {
                "phoneNo":"18916899938",
                "memberId":"0e399155-0a89-40e7-8177-e032984bf87c",
                 "position":"03"
             }
    hotPositionSer = HomeHotPositionService(kwargs = kwargs)
    hotRsp = hotPositionSer.queryHomeHotPosition()
    retcode = hotPositionSer.getRetcodeByActivityRsp(response=hotRsp)
    curinfos = hotPositionSer.getAllCnfListData(response=hotRsp)
    a = hotPositionSer.getDbPageDataBySql(configSqlStr="select_t_sku_HomePage")
    b = hotPositionSer.getDbPageDataBySql(configSqlStr="select_t_resource_calculate")
    print(retcode)
    print(curinfos)