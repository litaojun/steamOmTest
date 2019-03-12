from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService

class LotteryQueryLotteryInfoService(HttpUopService):
    '''
        查看抽奖活动详情信息
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryQueryLotteryInfoService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupGetLotteryIdByRsp","tearDownGetLotteryIdByRsp"])
    def getLotteryidByRsp(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
           self.inputKV["lotteryId"] = query_json(json_content=json.loads(self.rsp),
                                                   query="ffLotteryInfo.id")