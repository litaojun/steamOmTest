from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class MediaResetMediaStateService(HttpUopService):
    '''
        上架下架文章视频
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MediaResetMediaStateService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
