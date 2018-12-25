from opg.util.uopService import decorator,UopService,resultData
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
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
        self.inputKV["resourceId"]  = int(query_json( json_content = json.loads(self.rsp) ,
                                                        query        = "data.targets.0.resourceId" ))
        self.inputKV["skuId"]        = int(query_json( json_content  = json.loads(self.rsp) ,
                                                         query        = "data.targets.0.skuId" ))