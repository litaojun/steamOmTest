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
        rspDataLs = self.dataListFilterFields(listData=rspDataLs)
        #self.dataFilterFields(dictData=rspDataLs)
        #获取DB配置数据
        cnfDbdata = self.getDbPageDataBySql(configSqlStr=configSqlStr)
        #获取DB计算数据
        calculateData = self.getDbPageDataBySql(configSqlStr=calSqlStr)
        a = cnfDbdata[position]
        b = rspDataLs[0:len(a)]
        sign = op.eq(a,b)
        c = rspDataLs[len(cnfDbdata):10]
        d = calculateData[position][0:len(c)]
        csign = op.eq(c,d)
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