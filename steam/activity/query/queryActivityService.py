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
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import queryIdActivityurl
from steam.util.reqFormatPath import fxt,activityQueryReq
class ActivityQueryService(UopService):
    '''
        查询分类
    '''
    def __init__(self,kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ActivityQueryService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(activityQueryReq))
        self.rsp = None
        #self.activityQueryReqjson = self.reqjsondata
        self.queryIdActivityurl =queryIdActivityurl +  self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }
        #self.initReqJsonIdData(kwargs)

    def initReqJsonIdData(self,kwargs):
        skuIdLs = self.getSkuListByFormat(size = kwargs['skulist'])
        imgIdLs = self.getImageListByFormat(size = kwargs["imglist"])
        shareIdLs = self.getShareListByFormat(size=1)
        reqjsondata = eval(self.reqjsondata)
        for i,sku in enumerate(skuIdLs):
            pass

    def queryOneActivity(self):
        queryResult = requests.get(url = self.queryIdActivityurl )
        return queryResult.text

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

    # def getAllAlertId(self,queryRsp = None,skuLen = 2,imageLen =2):
    #     """
    #             data.shareInfoList.0.id
    #             data.skuList.0.skuId
    #             data.skuList.1.skuId
    #             data.imageList.0.id
    #             data.imageList.1.id
    #             data.imageList.2.id
    #             data.imageList.3.id
    #             data.imageList.4.id
    #             data.imageList.5.id
    #     :param queryRsp:
    #     :return:
    #     """
    #     idlist = []
    #     idls = ["data.shareInfoList.0.id"]
    #     skulist = ["data.skuList.%d.skuId" % i for i in range(skuLen)]
    #     imagelist = ["data.imageList.%d.id" % i for i in range(imageLen)]
    #     idls.append(skulist)
    #     idls.append(imagelist)
    #     for idtag in idls:
    #         resouceId = query_json(json_content=json.loads(queryRsp), query=idtag)
    #         idlist.append(resouceId)

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