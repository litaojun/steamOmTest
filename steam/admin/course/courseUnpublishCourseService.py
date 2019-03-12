from steam.util.httpUopService import  HttpUopService

class CourseUnpublishCourseService(HttpUopService):
    '''
        下架课程
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CourseUnpublishCourseService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
