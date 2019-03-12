from steam.util.httpUopService import  HttpUopService

class CheckInDailyService(HttpUopService):
    '''
        签到获取积分
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CheckInDailyService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
