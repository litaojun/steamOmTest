from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.course.courseModifyCourseService import CourseModifyCourseService
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
from steam.admin.course.courseQueryCourseByConditionService import CourseQueryCourseByConditionService
from steam.admin.course.courseRemoveCourseService import CourseRemoveCourseService
class CourseModifyCourseTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/course/modifyCourse"
      @initAdminInputService( services = [ CourseCreateCourseService ,
                                      CourseQueryCourseByConditionService ,
                                      CourseRemoveCourseService],
                         curser   = CourseModifyCourseService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CourseModifyCourseTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.admin.course.courseQueryCourseByConditionTest import CourseQueryCourseByConditionTest
    from steam.admin.course.courseCreateCourseTest import CourseCreateCourseTest
    from steam.admin.course.courseRemoveCourseTest import CourseRemoveCourseTest
    UserVerfiyCodeTest(methodName = "compareRetcodeTest",
                       param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName = "compareRetcodeTest",
                  param      = [1, 2, 3, 4, 5, {}, 7, 8])
    CourseQueryCourseByConditionTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    CourseCreateCourseTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    CourseRemoveCourseTest( methodName = "compareRetcodeTest",
                            param      = [1, 2, 3, 4, 5, {}, 7, 8] )
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\course\\operation-manageCourseModifyCourses.yml" ,
                    testclse     =  CourseModifyCourseTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )