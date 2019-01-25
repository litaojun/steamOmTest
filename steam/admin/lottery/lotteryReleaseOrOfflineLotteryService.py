from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class LotteryReleaseOrOfflineLotteryService(HttpUopService):
    '''
        上架下架抽奖活动
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryReleaseOrOfflineLotteryService, self).__init__(module       = "",
											                        filename     = "",
												                    sqlvaluedict = kwargs )

    @decorator("setupStateToStart")
    def updateStateToStart(self):
        self.inputKV["state"],self.inputKV["startState"] = \
            self.inputKV["startState"],self.inputKV["state"]
        self.sendHttpReq()
        self.inputKV["state"], self.inputKV["startState"] = \
            self.inputKV["startState"], self.inputKV["state"]
