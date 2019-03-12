from steam.util.httpUopService import  HttpUopService

class MaterialQueryAliyunVideoAuthService(HttpUopService):
    '''
        预览素材
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MaterialQueryAliyunVideoAuthService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
