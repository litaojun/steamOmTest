from steam.util.httpUopService import  HttpUopService

class MerchantQueryCertificateService(HttpUopService):
    '''
        查询订单状态
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MerchantQueryCertificateService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
