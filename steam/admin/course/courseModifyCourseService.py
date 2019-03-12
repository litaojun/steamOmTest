from steam.util.httpUopService import  HttpUopService

class CourseModifyCourseService(HttpUopService):
    '''
        修改课程
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CourseModifyCourseService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
