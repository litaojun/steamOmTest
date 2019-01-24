from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.course.courseRemoveCourseService import CourseRemoveCourseService
from steam.admin.course.courseQueryCourseByConditionService import CourseQueryCourseByConditionService
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
class CourseRemoveCourseTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/course/removeCourse"
      @initAdminInputService( services = [ CourseQueryCourseByConditionService ,CourseCreateCourseService ],
                         curser   = CourseRemoveCourseService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CourseRemoveCourseTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.course.courseQueryCourseByConditionTest import CourseQueryCourseByConditionTest
    from steam.admin.course.courseCreateCourseTest import CourseCreateCourseTest
    CourseQueryCourseByConditionTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    CourseCreateCourseTest( methodName = "compareRetcodeTest",
                            param      = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\course\\operation-manageCourseRemoveCourses.yml",
                    testclse     = CourseRemoveCourseTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )