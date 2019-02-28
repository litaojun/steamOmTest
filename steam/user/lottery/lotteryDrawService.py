from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
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

    @decorator(["setupUserLotterDray", "tearDownUserLotterDray"])
    def userLotterDraw(self):
        self.rsp = self.sendHttpReq()
        self.inputKV["prizeId"] = query_json(json_content=self.rsp,
                                             query="drawResult.prizeId")
        self.inputKV["resourceId"] = query_json(json_content=self.rsp,
                                                  query="drawResult.prizeId")
        self.inputKV["resourceTypeId"] = query_json(json_content=self.rsp,
                                                    query="drawResult.resourceTypeId")