from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class FeaturedMoveDownRecordService(HttpUopService):
    '''
        运营位记录下移
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(FeaturedMoveDownRecordService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupListOrderDown"])
    def setListOrderUp(self):
        self.inputKV["listOrder"] += 1