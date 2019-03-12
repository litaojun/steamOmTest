from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.course.courseUnpublishCourseService import CourseUnpublishCourseService
from steam.admin.course.courseRemoveCourseService import CourseRemoveCourseService
from steam.admin.course.courseQueryCourseByConditionService import CourseQueryCourseByConditionService
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
class CourseUnpublishCourseTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/course/unpublishCourse"
      @initAdminInputService( services = [ CourseCreateCourseService ,
                                      CourseQueryCourseByConditionService ,
                                      CourseRemoveCourseService],
                  curser   = CourseUnpublishCourseService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CourseUnpublishCourseTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.course.courseCreateCourseTest import CourseCreateCourseTest
    from steam.admin.course.courseQueryCourseByConditionTest import CourseQueryCourseByConditionTest
    from steam.admin.course.courseRemoveCourseTest import CourseRemoveCourseTest
    CourseCreateCourseTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    CourseQueryCourseByConditionTest(methodName = "compareRetcodeTest",
                                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    CourseRemoveCourseTest(methodName = "compareRetcodeTest",
                           param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\course\\operation-manageCourseUnpublishCourses.yml",
                    testclse     = CourseUnpublishCourseTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )