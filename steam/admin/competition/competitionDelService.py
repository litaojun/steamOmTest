from steam.util.httpUopService import  HttpUopService
from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.admin.competition.competitionService import MatchAddService
class MatchDelService(HttpUopService):
    def __init__(self, kwargs):
        super(MatchDelService, self).__init__(
                                                  module = "",
                                                  filename = "",
                                                  sqlvaluedict = kwargs,
                                                  reqjsonfile = None
                                             )
    @decorator("preInterfaceAddOneMatch")
    def addOneMatch(self):
        matchAddSer = MatchAddService(self.inputKV)
        matchrsp    = matchAddSer.addMatch()
        matchId     = matchAddSer.getMatchIdByRsp(matchrsp)
        self.reqjsondata["matchId"] = matchId
        self.inputKV["matchId"]     = matchId

    @decorator(["tearDownDelMatchOrSession"])
    def delMatch(self):
        self.sendHttpReq()

    def getRetcodeByMatchRsp(self, matchRsp=None):
        return query_json(json_content=json.loads(matchRsp), query="code")

    def getMatchIdByRsp(self, matchRsp=None):
        return query_json(json_content=json.loads(matchRsp), query="matchId")