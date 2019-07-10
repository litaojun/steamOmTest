import json
from opg.util.utils import query_json
from opg.bak.uopService import decorator
from steam.util.httpUopService import HttpUopService
class ActivityAddService(HttpUopService):
    def __init__(self, kwargs):
        super(ActivityAddService, self).__init__(module="activity", filename="activityDb.xml",
                                                 sqlvaluedict=kwargs,reqjsonfile=None,dbName="resource")

    @decorator("setupGetProductResourceId")
    def getActivityIdByRsp(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        rssId = query_json(json_content=json.loads(self.rsp),
                           query="data.resourceId")
        self.inputKV["resourceId"] = self.inputKV["id"] = rssId

    @decorator("setupAddOneActivity")
    def addOneActivity(self):
        self.sendHttpReq()