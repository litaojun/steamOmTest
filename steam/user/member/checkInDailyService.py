from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class CheckInDailyService(HttpUopService):
    '''
        签到获取积分
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CheckInDailyService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
