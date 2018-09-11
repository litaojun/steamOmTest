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
    def queryHomeHotPosition(self):
        self.rsp =  httpGet(
                                        url     = hotPositonUrl+self.reqjsondata,
                                        headers = self.jsonheart
                                  )
        return  self.rsp

    @check_rspdata(filepath=homePositionRspFmt)
    def getRetcodeByActivityRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    def getAllDataListFromRsp(self,response = None):
        calDataList = query_json(json_content=json.loads(response), query="showInfoPage.targets")
        return [data["resourceId"] for data in calDataList]

    def getAllDataListFromDb(self):
        position = self.inputKV["position"]
        configSqlStr = "select_t_resource_calculate"
        if self.inputKV["position"] == "04":
            configSqlStr = "select_t_resource_calculate_inovn"
        cnfDataList  = self.getDbPageDataBySql(configSqlStr = "select_t_sku_HomePage")
        calaDataList = self.getDbPageDataBySql(configSqlStr = configSqlStr)
        return cnfDataList[position][0:self.pgdc[position]] + calaDataList[position]

    def compareM(self):
        curPage = self.inputKV["currentPage"]
        cnfDataList = self.getAllDataListFromDb()
        rspDataList = self.getAllDataListFromRsp(response=self.rsp)
        start = (curPage-1) * 10
        end   =  curPage*10
        return op.eq(cnfDataList[start:end],rspDataList)

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