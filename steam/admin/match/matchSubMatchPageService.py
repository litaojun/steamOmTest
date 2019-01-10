from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class MatchSubMatchPageService(HttpUopService):
    '''
        查询赛事场次-赛事场次列表接口
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MatchSubMatchPageService, self).__init__( module       = "" ,
												        filename     = "" ,
												        sqlvaluedict = kwargs ,
                                                        dbName       = "match" )

    def findTestdataByStatus(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        dataLs = query_json( json_content = json.loads(self.rsp),
                             query        = "pageContext.targets" )
        print(self.inputKV)
        if len(dataLs) == 0 :
           return "100001"
        mthDict   = dict([(data["matchName"],data["state"]) for data in dataLs])
        matchName =  self.inputKV["matchName"]
        if matchName not in mthDict :
           return "100001"
        elif mthDict[matchName] != self.inputKV["state"]:
             return "100002"
        return "000000"