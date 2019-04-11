from steam.util.httpUopService import  HttpUopService

class MediaPublishService(HttpUopService):
    '''
        上架文章视频
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MediaPublishService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
