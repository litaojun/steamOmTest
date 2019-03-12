from steam.util.httpUopService import  HttpUopService

class MemberDetailQueryService(HttpUopService):
    '''
        获取国赛详细报名信息
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MemberDetailQueryService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
