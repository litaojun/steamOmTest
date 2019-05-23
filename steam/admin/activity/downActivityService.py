import requests
#from steam.util.configurl import downActivityurl

from steam.util.httpUopService import HttpUopService


class ActivityUnPublishService(HttpUopService):
    '''
        活动下线
    '''
    def __init__(self, kwargs):
        """ 初始化代码 """
        super(ActivityUnPublishService, self).__init__(module="",
                                                       filename="",
                                                       sqlvaluedict=kwargs,
                                                       reqjsonfile=None)

    # def unPublishActivitySer(self):
    #     pubActivityRsp = requests.post(
    #         url=downActivityurl,
    #         json=self.reqjsondata,
    #         headers=self.jsonheart,
    #         verify=False
    #     )
    #     return pubActivityRsp.text

if __name__ == "__main__":
    reqdata = {
        "resourceId": "22",
        "title": "QUEENS PALACE高级定制馆C-自动化",
        "resourceTypeId": 12
    }
    pubActSer = ActivityUnPublishService(kwargs=reqdata)
    searchRsp = pubActSer.searchActSer.queryActivity()
    ssid = pubActSer.searchActSer.getFirstActivityIdByRsp(queryRsp=searchRsp)
    pubActSer.activityDownReqjson["resourceId"] = ssid
    pubActRsp = pubActSer.unPublishActivitySer()
    print(pubActRsp)
