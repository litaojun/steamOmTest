from steam.util.httpUopService import  HttpUopService

class MaterialModifyMaterialService(HttpUopService):
    '''
        修改素材
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MaterialModifyMaterialService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
