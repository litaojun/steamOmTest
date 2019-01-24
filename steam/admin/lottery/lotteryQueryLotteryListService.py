from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class LotteryQueryLotteryListService(HttpUopService):
    '''
        抽奖活动列表
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryQueryLotteryListService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    def genNameIdDict(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        lotteryList = query_json(json_content=json.loads(self.rsp) ,
							     query="data.targets")
        return dict((lttery["lotteryTitle"],lttery["resourceId"])
                    for lttery in lotteryList)

    @decorator("setupGetResourceIdByLotyTitle")
    def getRsidByLotyName(self):
        lotyDict  = self.genNameIdDict()
        self.inputKV["resourceId"] = lotyDict[self.inputKV["lotyName"]]