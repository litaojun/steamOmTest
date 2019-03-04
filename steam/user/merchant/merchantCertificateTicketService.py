from steam.util.httpUopService import  HttpUopService

class MerchantCertificateTicketService(HttpUopService):
    '''
        商户核销订单
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MerchantCertificateTicketService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
