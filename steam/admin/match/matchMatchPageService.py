from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class MatchMatchPageService(HttpUopService):
    '''
        分页查询赛事
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MatchMatchPageService, self).__init__( module       = "" ,
												     filename     = "" ,
												     sqlvaluedict = kwargs ,
                                                     dbName       = "match" )

    def findTestdataByStatus(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        dataLs = query_json( json_content = json.loads(self.rsp),
                             query        = "data.targets" )
        if len(dataLs) == 0 :
            return "100001"
        if dataLs[0].state != self.inputKV["state"] :
           return "100002"
        return "000000"