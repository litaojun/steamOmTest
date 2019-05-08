from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.admin.course.courseAuditService import CourseAuditService
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
from steam.admin.course.courseQueryCourseByConditionService import CourseQueryCourseByConditionService
from steam.admin.course.courseRemoveCourseService import CourseRemoveCourseService
class CourseAuditTest(SteamTestCase):
      """
           课程审核
      """
      __interfaceName__ = "/operation-manage/course/audit"
      @initInputService( services = [ CourseCreateCourseService,
                                      CourseQueryCourseByConditionService,
                                      CourseRemoveCourseService ],
                         curser   = CourseAuditService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CourseAuditTest,self).__init__(methodName,param)

if __name__ == "__main__":
    pass