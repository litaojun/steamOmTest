from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService

class LotteryDrawService(HttpUopService):
    '''
        用户抽奖
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryDrawService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupUserLotterDray", "tearDownUserLotterDray"],userType="weixin")
    def userLotterDraw(self):
        self.rsp = self.sendHttpReq()
        self.inputKV["prizeId"] = query_json(json_content=json.loads(self.rsp),
                                             query="drawResult.prizeId")
        self.inputKV["resourceId"] = query_json(json_content=json.loads(self.rsp),
                                                  query="drawResult.prizeId")
        self.inputKV["resourceTypeId"] = query_json(json_content=json.loads(self.rsp),
                                                      query="drawResult.resourceTypeId")
        self.inputKV["title"] = query_json(json_content=json.loads(self.rsp),
                                                      query="drawResult.prizeTitle")