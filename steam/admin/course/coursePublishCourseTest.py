from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.course.coursePublishCourseService import CoursePublishCourseService
from steam.admin.course.courseRemoveCourseService import CourseRemoveCourseService
from steam.admin.course.courseQueryCourseByConditionService import CourseQueryCourseByConditionService
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
from steam.admin.course.courseAuditService import CourseAuditService
class CoursePublishCourseTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/course/publishCourse"
      @initInputService( services = [ CourseCreateCourseService ,
                                      CourseQueryCourseByConditionService ,
                                      CourseRemoveCourseService ,CourseAuditService],
                         curser     = CoursePublishCourseService ,sign="admin")
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CoursePublishCourseTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.runflask.outapi.testcaseRun import runOneTestClass
    runOneTestClass(interfaceName="/operation-manage/course/publishCourse")