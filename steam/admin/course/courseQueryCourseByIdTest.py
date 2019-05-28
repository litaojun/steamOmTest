from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
from steam.admin.course.courseQueryCourseByIdService import CourseQueryCourseByIdService
from steam.admin.course.courseRemoveCourseService import CourseRemoveCourseService
from steam.admin.course.courseQueryCourseByConditionService import CourseQueryCourseByConditionService
class CourseQueryCourseByIdTest(SteamTestCase):
      """
            根据课程ID查询课程详情
      """
      __interfaceName__ = "/operation-manage/course/queryCourseById"
      @initAdminInputService( services = [ CourseCreateCourseService, CourseQueryCourseByConditionService,
                                           CourseRemoveCourseService],
                         curser   = CourseQueryCourseByIdService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CourseQueryCourseByIdTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.course.courseQueryCourseByConditionTest import CourseQueryCourseByConditionTest
    CourseQueryCourseByConditionTest( methodName = "compareRetcodeTest",
                                      param      = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\course\\operation-manageCourseQueryCourseByIds.yml",
                    testclse     = CourseQueryCourseByIdTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )