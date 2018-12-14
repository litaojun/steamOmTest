from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata

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
