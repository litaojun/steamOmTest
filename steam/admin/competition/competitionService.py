from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService
class MatchAddService(HttpUopService):
    def __init__(self, kwargs):
        super(MatchAddService, self).__init__(module       = "" ,
                                              filename     = "" ,
                                              sqlvaluedict = kwargs ,
                                              reqjsonfile  = None)

    @decorator(["tearDownDelMatchSession"])
    def delMatch(self):
        self.sendHttpReq()

    @decorator(["setupAddMatchOrSession"])
    def addMatch(self):
        self.sendHttpReq()

    def getRetcodeByMatchRsp(self,matchRsp = None):
        return query_json(json_content = json.loads(matchRsp),
                          query        = "code")

    @decorator(["setupGetMatchOrSessionId","tearDownGetMatchOrSessionId"])
    def getMatchIdByRsp(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        self.inputKV["matchId"] =  query_json(json_content  = json.loads(self.rsp),
                                                 query       = "matchId")