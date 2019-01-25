from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class LotteryCreateLotteryInfoService(HttpUopService):
    '''
        新增抽奖活动
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryCreateLotteryInfoService, self).__init__(module       = "lottery",
												              filename     = "lotteryDb.xml",
												              sqlvaluedict = kwargs,
                                                              dbName       = "resource")

