from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class LotteryDetailService(HttpUopService):
    '''
        微信用户浏览抽奖活动详情
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryDetailService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
    @decorator("setupGetLotteryIdByRsp")
    def getLotteryidByRsp(self):
        if self.rsp is None:
            self.rsp = self.sendHttpReq()
        self.inputKV["lotteryId"] = query_json(json_content=json.loads(self.rsp) ,
							                     query="data.lotteryId")
