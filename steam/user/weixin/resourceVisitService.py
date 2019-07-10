from opg.util.httptools import httpPost
from steam.util.httpUopService import  HttpUopService
class ResourceVisitService(HttpUopService):
    '''
        用户浏览内容后浏览量+1
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(ResourceVisitService, self).__init__(  module       = modul,
                                                     filename     = filename,
                                                     sqlvaluedict = kwargs ,
                                                     reqjsonfile  = reqjsonfile )
