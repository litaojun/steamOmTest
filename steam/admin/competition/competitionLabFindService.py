from opg.bak.uopService import UopService
import json
from opg.util.utils import query_json
class MatchLabFindService(UopService):
    '''
         admin查询赛事
    '''
    def __init__(self, kwargs):
        super(MatchLabFindService, self).__init__(module  = "",
                                              filename = "",
                                              sqlvaluedict = kwargs,
                                              reqjsonfile  = "competitionFindReq")

    def getRetcodeBySubMatchRsp(self,matchRsp = None):
        return query_json(json_content = json.loads(matchRsp), query = "code")

    def getSubMatchFromRspByName(self,matchRsp = None,matchName = ""):
        if matchRsp is None:
           matchRsp = self.findSubMatchReq()
        matchList = query_json(json_content = json.loads(matchRsp),
                               query        = "pageContext.targets")
        curMatch = [ match  for match in matchList if match["matchName"] == matchName ]
        return curMatch[0] if len(curMatch) > 0 else None
