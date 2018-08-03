#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryActivityService.py 
@time: 2018/5/7 14:06 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import queryIdActivityurl
from steam.util.reqFormatPath import fxt,activityQueryReq
from opg.util.httptools import httpGet,httpPost
class ActivityQueryService(UopService):
    '''
        查询活动文章
    '''
    def __init__(self,kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(ActivityQueryService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(activityQueryReq))
        self.queryIdActivityurl =queryIdActivityurl +  self.reqjsondata

    def initReqJsonIdData(self,kwargs):
        skuIdLs = self.getSkuListByFormat(size = kwargs['skulist'])
        imgIdLs = self.getImageListByFormat(size = kwargs["imglist"])
        shareIdLs = self.getShareListByFormat(size=1)
        reqjsondata = eval(self.reqjsondata)
        for i,sku in enumerate(skuIdLs):
            pass

    def queryOneActivity(self):
        queryResult = httpGet(url=self.queryIdActivityurl,headers={})
        return queryResult

    def getListIdByFormat(self,formatstr = "" ,size = 2):
        idls = [formatstr % i for i in range(size)]
        return idls

    def getSkuListByFormat(self,size=2):
        idls = self.getListIdByFormat("data.skuList.%d.skuId",size)
        return idls

    def getImageListByFormat(self,size=2):
        idls = self.getListIdByFormat("data.imageList.%d.id",size)
        return idls

    def getShareListByFormat(self,size =1):
        idls =  self.getListIdByFormat("data.shareInfoList.%d.id",size)
        return idls

    def getIdValueListByRsp(self,ids=[],rsp = None):
        idvls = []
        for idtag in ids:
            idvlaue = query_json(json_content=json.loads(rsp), query=idtag)
            idvls.append(idvlaue)
        return idvls

    def getRetcodeByOneactRsp(self,oneActRsp = None):
        return query_json(json_content=json.loads(oneActRsp), query="code")


if __name__ == "__main__":

    queryJsonData = {
                       "resourceId":1469,
                       "skulist":2,
                       "imglist":1,
                       "sharelist":1,
                       "resourceTypeId":11,
                       "title":"QUEENS PALACE高级定制馆C-自动化"
                    }
    aqs = ActivityQueryService(kwargs=queryJsonData)
    aqs.getSkuListByFormat(size=2)
    queryResultRsp = aqs.queryOneActivity()
    idlsformat = aqs.getImageListByFormat(size = queryJsonData["imglist"])
    ids = aqs.getIdValueListByRsp(ids=idlsformat,rsp=queryResultRsp)
    idlsformat = aqs.getShareListByFormat(size=1)
    ids = aqs.getIdValueListByRsp(ids=idlsformat,rsp=queryResultRsp)
    idlsformat = aqs.getSkuListByFormat(size=queryJsonData["skulist"])
    ids = aqs.getIdValueListByRsp(ids=idlsformat, rsp=queryResultRsp)
    print("rsid = %s" % ids)