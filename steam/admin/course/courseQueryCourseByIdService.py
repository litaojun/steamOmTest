from steam.util.httpUopService import  HttpUopService

class CourseQueryCourseByIdService(HttpUopService):
    '''
        根据ID查询课程详情
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CourseQueryCourseByIdService, self).__init__(module       = "",
											             filename       = "",
												          sqlvaluedict  = kwargs )
