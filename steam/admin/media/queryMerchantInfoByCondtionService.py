from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService

class QueryMerchantInfoByCondtionService(HttpUopService):
    '''
        搜索素材
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(QueryMerchantInfoByCondtionService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupGetFirstMerchant","tearDownGetFirstMerchant"])
    def getFirstMerchant(self):
        self.rsp = self.sendHttpReq()
        self.inputKV["resourceId"] = self.inputKV["id"]  = int(query_json( json_content = json.loads(self.rsp) ,
                                                                             query        = "data.targets.0.id" ))
