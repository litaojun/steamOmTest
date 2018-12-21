from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class FeaturedMoveUpRecordService(HttpUopService):
    '''
        运营位记录上移
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(FeaturedMoveUpRecordService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
    @decorator(["setupListOrderUp"])
    def setListOrderUp(self):
        if self.inputKV["listOrder"] > 1:
           self.inputKV["listOrder"] -= 1
