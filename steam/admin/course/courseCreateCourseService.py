from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService

class CourseCreateCourseService(HttpUopService):
    '''
        新增课程
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CourseCreateCourseService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
    @decorator(["setupAddCourse"])
    def addOneCourse(self):
        self.rsp = self.sendHttpReq()
