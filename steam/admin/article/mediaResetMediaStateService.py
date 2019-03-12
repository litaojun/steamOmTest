from steam.util.httpUopService import  HttpUopService

class MediaResetMediaStateService(HttpUopService):
    '''
        上架下架文章视频
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MediaResetMediaStateService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
