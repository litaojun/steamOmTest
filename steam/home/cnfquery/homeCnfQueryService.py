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
from opg.util.utils import query_json,del_json_data
from steam.util.configurl import homeConfigQueryurl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import homeConfigQueryReq,homeConfigQueryRspFmt
from opg.util.httptools import httpGet
from opg.util.lginfo import  logger
import operator as op
class HomeCnfQueryService(UopService):
    '''
        首页配置数据
    '''
    def __init__(self,
                 kwarg={},
                 modul="weixin",
                 filename= "cnfDataDb.xml",
                 reqjsonfile = homeConfigQueryReq):
        """
            :param entryName:
            :param picturePath:
        """
        super(HomeCnfQueryService, self).__init__(module       = modul,
                                                  filename     = filename,
                                                  sqlvaluedict = kwarg ,
                                                  reqjsonfile  = reqjsonfile)
        self.pgdc = {
                        "01":6,  #首页轮播图
                        "02":6,  #首页今日推荐,应该为5个，但前端现状了，未出现BUG
                        "05":7,  #首页分类
                        "07":4,  #首页动态
                        "10":1,   #首页单独运营
                        "09":10, #发现页热门推荐
                        "03":10, #首页更多精彩
                        "04":10  #创新大赛页
                    }

    def queryHomePageCnf(self):
        homePageCnfRsp =  httpGet(
                                        url     = homeConfigQueryurl + self.reqjsondata,
                                        headers = self.jsonheart
                                  )
        self.rsp = homePageCnfRsp
        return homePageCnfRsp

    @check_rspdata(filepath=homeConfigQueryRspFmt)
    def getRetcodeByActivityRsp(self,response = None):
        #print("homePageCnfRsp=" + str(response))
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
        # num = len(showInfos)
        # retdata = {}
        # for i in range(num):
        #     positionQuery = "showInfos.%d.position" % i
        #     infosQuery = "showInfos.%d.showSummaryInfos" % i
        #     curposition = query_json(json_content=json.loads(response), query=positionQuery)
        #     curinfos = query_json(json_content=json.loads(response), query=infosQuery)
        #     retdata[curposition] = curinfos
        # return retdata

    def dataDictFilterFields(self,dictData = {},fields = []):
        rdt = {}
        for key in dictData.keys():
            lsdata = self.dataListFilterFields(listData=dictData[key],fields=fields)
            rdt[key] = lsdata
        return rdt

    def dataListFilterFields(self, listData=[], fields=[]):
        retls = []
        #allFields = ["collectState", "sales", "visits", "collects", "state", "holdingTime", "activityAddress", "subHead", 'minPrice', 'originalPrice']
        allFields = ["resourceId"]
        if fields is not None and len(fields) > 0:
            allFields = fields
        for i in range(len(listData)):
             dicta = {}
             for field in allFields:
                dicta[field] = listData[i][field]
             retls.append(dicta)
        return retls

    def getDbPageDataBySql(self,configSqlStr = "select_t_sku_HomePage"):
        homePageDbDataList = self.selectAllDataBySqlName(configSqlStr)
        dbDataDict = {}
        fields = ['resourceId', 'specificType', 'bannerUrl', 'thumbUrl', 'resourceType', 'title', 'position']
        def funa(x):
            if dbDataDict[6] in dbDataDict:
                dbDataDict[x[6]].append(x[0])
            else:
                dbDataDict[x[6]] = []
        self.filterLenByOrder(dbDataDict)
        map(funa,homePageDbDataList)
        return dbDataDict

    #根据需求，每个运营位显示最大数量截取
    def filterLenByOrder(self,dictData = {}):
        for data in dictData:
            dictData[data] = dictData[data][0:self.pgdc[data]]



    def compareData(self,response = None,removePositionLs = [],configSqlStr = "select_t_sku_HomePage"):
        """
        :param response: 获取配置信息的json内容
        :param positionLs: 配置页删除的position列表
        :return:
        """
        filtls = removePositionLs
        pageDataDict = self.getAllCnfListDataFromRSP(response = response)
        for p in filtls:
            del pageDataDict[p]
        pageDict = self.dataDictFilterFields(dictData=pageDataDict)
        dbDataDict = self.getDbPageDataBySql(configSqlStr = configSqlStr)
        self.filterLenByOrder(dictData=dbDataDict)
        dbDataDict = self.dataDictFilterFields(dictData=dbDataDict)
        sign = op.eq(dbDataDict, pageDict)
        return sign

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