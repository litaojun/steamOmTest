from steam.util.httpUopService import  HttpUopService

class LotteryQueryPrizeInventoryService(HttpUopService):
    '''
        查看奖品库存
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryQueryPrizeInventoryService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
