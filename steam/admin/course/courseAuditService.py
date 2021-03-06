from opg.bak.uopService import decorator
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class CourseAuditService(HttpUopService):
    '''
        审核课程
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CourseAuditService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
    @decorator(["setupGetAuditCourse"])
    def optAuditCourse(self):
        self.sendHttpReq()
