from steam.util.httpUopService import  HttpUopService

class MediaUnpublishService(HttpUopService):
    '''
        下架文章视频
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MediaUnpublishService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
