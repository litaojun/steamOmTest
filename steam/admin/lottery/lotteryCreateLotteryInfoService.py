from steam.util.httpUopService import  HttpUopService

class LotteryCreateLotteryInfoService(HttpUopService):
    '''
        新增抽奖活动
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(LotteryCreateLotteryInfoService, self).__init__(module       = "lottery",
												              filename     = "lotteryDb.xml",
												              sqlvaluedict = kwargs,
                                                              dbName       = "resource")

