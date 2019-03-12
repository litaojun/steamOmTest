from opg.bak.uopService import decorator

from steam.util.httpUopService import  HttpUopService

class CourseRemoveCourseService(HttpUopService):
    '''
        删除课程
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CourseRemoveCourseService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupRemoveCourse","tearDownRemoveCourse"])
    def removeOneCourse(self):
        self.rsp = self.sendHttpReq()
