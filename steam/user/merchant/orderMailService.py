from steam.util.httpUopService import  HttpUopService

class OrderMailService(HttpUopService):
    '''
        商户获取订单邮件
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(OrderMailService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
