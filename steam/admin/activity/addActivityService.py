from opg.util.uopService import decorator, UopService
import requests
import json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from steam.util.configurl import addActivityurl
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import HttpUopService


class ActivityAddService(HttpUopService):
    '''
        活动新增
    '''

    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ActivityAddService, self).__init__(module="activity",
                                                 filename="activityDb.xml",
                                                 sqlvaluedict=kwargs,
                                                 reqjsonfile=None,
                                                 dbName="resource")

    def getActivityIdByRsp(self):
        if self.rsp is None:
            self.rsp = self.sendHttpReq()
        rssId = query_json(json_content=json.loads(self.rsp),
                           query="data.resourceId")
        return rssId


if __name__ == "__main__":
    reqjson = {
        "resourceId": "",
        "title": "QUEEN'S PALACE高级定制馆1-自动化",
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
        "state": 1}
    actSer = ActivityAddService(reqjson)
    rsp = "{\"code\": \"000000\",\"message\": \"成功\",\"data\": {\"resourceId\": 1590}}"
    code = actSer.getRetcodeByActivityRsp(response=rsp)
    ssid = actSer.getActivityIdByRsp(rsp)
