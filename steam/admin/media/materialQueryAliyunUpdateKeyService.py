from steam.util.httpUopService import  HttpUopService

class MaterialQueryAliyunUpdateKeyService(HttpUopService):
    '''
        获取阿里云视频上传凭证
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MaterialQueryAliyunUpdateKeyService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
