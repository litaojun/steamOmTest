import json
from opg.util.utils import query_json
#from steam.util.configurl import searchActivityurl
from steam.user.weixin.userViewActivityService import  UserViewActivityService
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
from opg.bak.uopService import decorator
class ActivitySearchService(HttpUopService):
    '''
        管理后台-搜索活动商品
    '''
    def __init__(self,kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(ActivitySearchService, self).__init__("", "", kwargs)
        self.activityQueryReqjson = self.reqjsondata

    def queryActivity(self):
        queryResult = httpGet(
                                  url     =  searchActivityurl + self.reqjsondata,
                                  headers = self.jsonheart
                             )
        return queryResult

    def getFirstActivityIdByRsp(self,queryRsp = None):
        if queryRsp is None:
           queryRsp = self.sendHttpReq()
        print("queryRsp = %s" % queryRsp)
        return query_json(json_content=json.loads(queryRsp), query="data.targets.0.resourceId")

    def getSku(self,skuName):
        if self.rsp is None:
            self.rsp  = self.queryActivity()
        actId = self.getFirstActivityIdByRsp(queryRsp=self.rsp)
        self.inputKV["resourceId"] = actId
        userViewActSer = UserViewActivityService(kwarg=self.inputKV )
        sku = userViewActSer.getSkuByName(skuName=skuName)
        return sku

    def getSkuIdBySkuName(self,skuName =""):
        return self.getSku()["skuName"]

    def getSkuPayPriceBySkuName(self,skuName=""):
        return self.getSku()["skuName"]

    @decorator("setupGetFirstProductContent")
    def setInPutData(self):
        resourceId = self.getFirstActivityIdByRsp(queryRsp=self.rsp)
        self.inputKV["resourceId"] = self.inputKV["id"] = resourceId
        # self.inputKV["id"] = resourceId

    def getRetcodeByActRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="code")

    def findTestdataByStatus(self):
        if self.rsp is None:
            self.rsp = self.sendHttpReq()
        dataLs = query_json( json_content = json.loads(self.rsp) ,
                             query        = "data.targets" )
        print(self.inputKV)
        if len(dataLs) == 0 :
            return "100001"
        self.setInPutData()
        if dataLs[0]["status"] != self.inputKV["status"] :
           return "100002"
        return "000000"

if __name__ == "__main__":
    queryJsonData = {
                         "currentPage":1,
                         "pageSize":10,
                         "resourceTypeId":12,
                         "title":"早鸟价！呼伦贝尔｜私家牧场任你驰骋策马，原始森林徒步猎奇",
                         "skuName":"价格（成人）"
                     }
    aqs = ActivitySearchService(kwargs=queryJsonData)
    queryResultRsp = aqs.queryActivity()
    rsid = aqs.getFirstActivityIdByRsp(queryRsp=queryResultRsp)
    print("rsid = %s" % rsid)
    skuid = aqs.getSkuIdBySkuName(skuName=queryJsonData["skuName"])
    print("skuid = %s" % skuid)