from steam.util.httpUopService import  HttpUopService

class MemberApplyDetailSaveService(HttpUopService):
    '''
        保存参赛队信息
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MemberApplyDetailSaveService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
