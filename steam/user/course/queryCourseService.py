from steam.util.httpUopService import  HttpUopService
class QueryCourseService(HttpUopService):
    '''
        用户查看课程详情页
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(QueryCourseService, self).__init__(  module       = modul,
                                                       filename     = filename,
                                                       sqlvaluedict = kwargs ,
                                                       reqjsonfile  = reqjsonfile )

