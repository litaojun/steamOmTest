import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService
class MatchFindService(HttpUopService):
      def __init__(self, kwargs):
          super(MatchFindService, self).__init__(module  = "",
                                                 filename = "",
                                                 sqlvaluedict = kwargs)

      def getRetcodeByMatchRsp(self,matchRsp = None):
          return query_json(json_content = json.loads(matchRsp), query = "code")

      def getMatchFromRspByName(self,matchRsp = None,matchName = ""):
          if matchRsp is None:
             matchRsp = self.sendHttpReq()
             matchList = query_json(json_content = json.loads(matchRsp),
                                    query        = "pageContext.targets")
             curMatch = [ match  for match in matchList if match["matchName"] == matchName ]
             return curMatch[0] if len(curMatch) > 0 else None

      def setInPutData(self):
          pass
