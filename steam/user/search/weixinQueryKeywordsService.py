from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
class WeixinQueryKeywordsService(HttpUopService):
    '''
        微信端-搜索
    '''
    def __init__(self,kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(WeixinQueryKeywordsService, self).__init__(module       =  "",
                                                         filename     =  "",
                                                         sqlvaluedict =  kwargs,
                                                         reqjsonfile  =  None)


if __name__ == "__main__":
    queryJsonData = {
                         "currentPage":1,
                         "pageSize":10,
                         "resourceTypeId":12,
                         #"keyword":"早鸟价！呼伦贝尔｜私家牧场任你驰骋策马，原始森林徒步猎奇",
                         "keyword": "早鸟价",
                         "skuName":"价格（成人）",
                         "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                         "token":"e1974c2a63ab445dba7e0392b90a81bb"
                     }
    aqs = WeixinQueryKeywordsService(kwargs=queryJsonData)
    rsp =  aqs.weixinQueryKeywordsReq()
    ret = aqs.getRetcodeByRsp(response=rsp)
    print(ret)