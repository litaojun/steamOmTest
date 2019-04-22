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
import json
from opg.util.utils import query_json
# from steam.util.configurl import homeConfigQueryurl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import homeConfigQueryRspFmt
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
import operator as op
class HomeCnfQueryService(HttpUopService):
    '''
        首页配置数据
    '''
    def __init__(self,
                 kwargs      = {},
                 modul       = "weixin",
                 filename    = "cnfDataDb.xml",
                 reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(HomeCnfQueryService, self).__init__(module       = modul,
                                                  filename     = filename,
                                                  sqlvaluedict = kwargs ,
                                                  reqjsonfile  = reqjsonfile,
                                                  dbName       = "allin")
        self.pgdc = {
                        "01":6,    #首页轮播图
                        "02":6,    #首页今日推荐,应该为5个
                        "03":10,  # 首页更多精彩
                        "04":10,  # 创新大赛页
                        "05":7,   #首页分类
                         "06":1 ,  #创新大赛独立运营位
                        "07":4,   #首页动态
                        "08":10,    #创新大赛轮播图
                        "10":1,   #首页单独运营
                        "09":10,  #发现页热门推荐
                    }

    def queryHomePageCnf(self):
        self.rsp =  httpGet(
                                        url     = homeConfigQueryurl + self.reqjsondata,
                                        headers = self.jsonheart
                            )
        return self.rsp

    @check_rspdata(filepath=homeConfigQueryRspFmt)
    def getRetcodeByActivityRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    #从返回中提取{位置：ID列表}
    def getAllCnfListDataFromRSP(self,response = None):
        """
            :param response:
            :return:
        """
        showInfos = query_json(json_content=json.loads(response), query="showInfos")
        return dict([(data["position"],
                      [ m["resourceId"]
                                         for i,m in enumerate(data["showSummaryInfos"]) ]
                      )
                     for data in showInfos])

    def getEntryIdByNameFromRsp(self,response = None,entryName = None):
        if response is None:
            response = self.queryHomePageCnf()
        showInfos = query_json(json_content = json.loads(response),
                               query        = "showInfos")
        for t in showInfos:
            if t["position"] == "05":
               for data in t["showSummaryInfos"]:
                   if data["title"] == entryName:
                      return data["resourceId"]

    def getDbPageDataBySql(self,configSqlStr = "select_t_sku_HomePage"):
        homePageDbDataList = self.selectAllDataBySqlName(configSqlStr)
        position = self.inputKV["position"]
        return {position:[data[0] for data in homePageDbDataList]}

    #根据需求，每个运营位显示最大数量截取
    def filterLenByOrder(self,dbDataList = [],rspDataList = []):
        position = self.inputKV["position"]
        dbDataList  = dbDataList[0:self.pgdc[position]]
        rspDataList = rspDataList[0:len(dbDataList)]
        return dbDataList,rspDataList



    def compareData(self,response = None,configSqlStr = "select_t_sku_HomePage"):
        """
        :param response: 获取配置信息的json内容
        :param positionLs: 配置页删除的position列表
        :return:
        """
        pageDataDict = self.getAllCnfListDataFromRSP(response = response)
        dbDataDict = self.getDbPageDataBySql(configSqlStr=configSqlStr)
        position = self.inputKV["position"]
        d,p = self.filterLenByOrder(rspDataList = pageDataDict[position],
                                    dbDataList  = dbDataDict[position])

        sign = op.eq(d, p)
        return sign

    def setInPutData(self):
        entryId = self.getEntryIdByNameFromRsp(entryName = self.inputKV["entryName"])
        if entryId is not None:
            self.inputKV["entryId"] = entryId

if __name__ == "__main__":
    kwargs = {
                "phoneNo":"18916899938",
                "memberId":"0e399155-0a89-40e7-8177-e032984bf87c",
                "pageType":"0"
             }
    homeCnfSer = HomeCnfQueryService(kwargs=kwargs)
    homeRsp = homeCnfSer.queryHomePageCnf()
    retcode = homeCnfSer.getRetcodeByActivityRsp(response=homeRsp)
    retdata = homeCnfSer.getAllCnfListDataFromRSP(response=homeRsp)
    data01 = retdata['01']
    data02 = retdata['02']
    data05 = retdata['05']
    data07 = retdata['07']
    data10 = retdata['10']
    homeCnfSer.dataDictFilterFields(dictData=retdata,fields=[])
    homeCnfSer.compareData(response=homeRsp)
    print(retdata)
    print("retcode=%s" % retcode)
    funa = lambda x:funa(x-2)+funa(x-1) if x>2 else 1
    funb = lambda x:x+1 if x>10 else x