from steam.util.httpUopService import  HttpUopService
import json
from opg.util.utils import query_json
class MerchantLoginService(HttpUopService):
    '''
        商户登录
    '''
    __interfaceName__ = "/merchant-service/merchant/login"
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MerchantLoginService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    def getTokenFromRsp(self,response):
        return query_json(json_content = json.loads(response),
                          query        = "token")

