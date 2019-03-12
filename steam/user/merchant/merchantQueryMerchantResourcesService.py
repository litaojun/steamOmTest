from steam.util.httpUopService import  HttpUopService

class MerchantQueryMerchantResourcesService(HttpUopService):
    '''
        商户页
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MerchantQueryMerchantResourcesService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
