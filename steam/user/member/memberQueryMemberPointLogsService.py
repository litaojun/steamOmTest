from steam.util.httpUopService import  HttpUopService

class MemberQueryMemberPointLogsService(HttpUopService):
    '''
        我的积分列表
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MemberQueryMemberPointLogsService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
