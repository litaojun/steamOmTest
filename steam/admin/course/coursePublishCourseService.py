from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService

class CoursePublishCourseService(HttpUopService):
    '''
        发布课程
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CoursePublishCourseService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupPublishCourse"])
    def publishCourse(self):
        self.rsp = self.sendHttpReq()
