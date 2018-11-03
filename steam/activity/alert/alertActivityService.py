#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: alertActivityService.py 
@time: 2018/5/7 13:57 
"""
from opg.util.httptools import httpGet,httpPost
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json,setValue_json
from steam.util.configurl import alertActivityurl
from steam.activity.query.queryActivityService import ActivityQueryService
from steam.activity.add.addActivityService import ActivityAddService
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.util.reqFormatPath import fxt,activityAlertReq,activityAlertRspFmt
class ActivityAlertService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(ActivityAlertService, self).__init__(module="",
                                                   filename="",
                                                   sqlvaluedict =  kwargs,
                                                   reqjsonfile  =  kwargs["reqjsonfile"])

    def alertActivity(self):
        self.rsp = httpPost(url         = alertActivityurl,
                            headers     = self.jsonheart,
                            reqJsonData = self.reqjsondata)
        return self.rsp

    def alertReqIdToValue(self,skulist = [],imglist = [],sharelist = []):
        self.idToValueByFormat(formatstr = "skuList.%d.skuId",
							   idlist    = skulist)
        self.idToValueByFormat(formatstr = "imageList.%d.id",
							   idlist    = imglist)
        self.idToValueByFormat(formatstr = "shareInfoList.%d.id",
							   idlist    = sharelist)

    def idToValueByFormat(self,formatstr = "" ,idlist = []):
        for i,idvalue in enumerate(idlist):
            setValue_json(json_content=self.activityAlertReqjson,query=formatstr % i,setvalue=idvalue)


    def getRetcodeByRsp(self,articleRsp = None):
        return query_json(json_content = json.loads(articleRsp),
						  query        = "code")

    def getActivityIdByTitle(self,title = None):
        articleQs = ActivitySearchService(kwargs={"title":title,"resourceTypeId":self.activityAlertReqjson["resourceTypeId"]})
        queryRsp = articleQs.queryActivity()
        rssid = articleQs.getFirstActivityIdByRsp(queryRsp = queryRsp)
        return rssid


if __name__ == "__main__":
   reqdata = {
					"resourceId": "",
					"title": "QUEENS PALACE高级定制馆1-自动化",
					"subTitle": "QUEEN'S PALACE高级定制馆-活动副标题",
					"deliverType": 0,
					"vendorIdList": [3],
					"resourceTypeId": 12,
					"content": "<!DOCTYPE html><html><head></head><body><p>fQueen’s Palace于2011年9月创立，是一家国内高级定制婚纱礼服奢侈品牌。自品牌创立以来，Queen’s Palace在沪上高定婚纱品牌的殿堂一直雄踞顶端，专注于婚纱定制的每一处细节。</p></body></html>",
					"shareType": 1,
					"shareTitle": "QUEEN'S PALACE高级定制馆-分享标题",
					"shareDescription": "QUEEN'S PALACE高级定制馆-分享描述",
					"sharePicturePath": "http://uat-steam.opg.cn/_static/admin/images/resource/20180507101830_796382.jpg",
					"province": "重庆市",
					"city": "重庆郊县",
					"addressDetail": "肇嘉浜路356号(襄阳南路路口)",
					"thumbUrl": "http://uat-steam.opg.cn/_static/admin/images/resource/20180507101738_928360.jpg",
					"bannerUrl": "http://uat-steam.opg.cn/_static/admin/images/resource/20180507101741_710087.jpg",
					"imgListpicturePath1": "http://uat-steam.opg.cn/_static/admin/images/resource/20180507101747_909470.jpg",
					"imgListpicturePath2": "http://uat-steam.opg.cn/_static/admin/images/resource/20180507101749_880315.jpg",
					"cornerMask": "商品",
					"offShelfTime": 2764800000,
					"entryIdList": [7],
					"tagIdList": [2],
					"skuName1": "套餐1",
					"skuId1": None,
					"order1": 1,
					"price1": "0.01",
					"originPrice1": "1000",
					"inventory1": "1000",
					"limitCount1": "2",
					"postPrice1": "0.01",
					"skuName2": "套餐2",
					"skuId2": None,
					"order2": 2,
					"price2": "0.02",
					"originPrice2": "1200",
					"inventory2": "2000",
					"limitCount2": "3",
					"postPrice2": "0.01",
					"state": 1,
	                "skulist":2,
	                "imglist":2,
	                "sharelist":1
				}
   activitySer = ActivityAlertService(kwargs=reqdata)
   addrsp = activitySer.addArticle()
   activityid = activitySer.getActivityIdByTitle(title=reqdata['title'])
   #articleQs = ActivityQueryService(kwargs={"title": reqdata['title'], "resourceTypeId":reqdata["resourceTypeId"]})
   #queryRsp = articleQs.queryOneActivity()
   # query_json(json_content= queryRsp,query="")
   alertRsp = activitySer.alertActivity(kwargs=reqdata)
   retcode  = activitySer.getRetcodeByActivityRsp(articleRsp = alertRsp)
