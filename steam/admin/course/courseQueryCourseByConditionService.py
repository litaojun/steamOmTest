from opg.bak.uopService import decorator, resultData
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService

class CourseQueryCourseByConditionService(HttpUopService):
    '''
        搜索课程
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CourseQueryCourseByConditionService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
    @resultData("getQryRstCount")
    def getQueryResultCount(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        return len(query_json(json_content=json.loads(self.rsp),query="data.targets"))

    @decorator(["setupGetFrsIdFromQryRst","tearDownGetFrsIdFromQryRst"])
    def getFirstIdFromQueryRst(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        self.inputKV["resourceId"] = self.inputKV["id"]  = int(query_json( json_content = json.loads(self.rsp) ,
                                                                             query        = "data.targets.0.resourceId" ))
        self.inputKV["skuId"]        = int(query_json( json_content  = json.loads(self.rsp) ,
                                                         query        = "data.targets.0.skuId" ))

    def findTestdataByStatus(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        dataLs = query_json( json_content = json.loads(self.rsp) ,
                             query        = "data.targets"       )
        print(self.inputKV)
        if len(dataLs) == 0 :
           return "100001"
        self.getFirstIdFromQueryRst()
        if dataLs[0]["status"] != self.inputKV["status"] :
           return "100002"
        return "000000"