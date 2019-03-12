from steam.util.httpUopService import  HttpUopService

class LotteryQueryPrizeRosterService(HttpUopService):
    '''
        查看中奖名单
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryQueryPrizeRosterService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
