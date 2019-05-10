import requests,json
from opg.util.utils import query_json
from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService
class ActivityPublishService(HttpUopService):
    '''
        活动新增
    '''
    def __init__(self, kwargs):
        super(ActivityPublishService, self).__init__("", "", kwargs)

    def getRetcodeByUpactRsp(self,oneActRsp = None):
        return query_json(json_content=json.loads(oneActRsp), query="code")

    @decorator(["setupUpActivity"])
    def upActivity(self):
        self.sendHttpReq()

if __name__ == "__main__":
   reqdata = {
	            "resourceId": "22",
                "title": "QUEENS PALACE高级定制馆C-自动化",
	            "resourceTypeId":12
              }
   pubActSer = ActivityPublishService(kwargs=reqdata)
   searchRsp = pubActSer.searchActSer.queryActivity()
   ssid = pubActSer.searchActSer.getFirstActivityIdByRsp(queryRsp=searchRsp)
   pubActSer.activityUpReqjson["resourceId"] = ssid
   pubActRsp = pubActSer.publishActivitySer()
   print(pubActRsp)