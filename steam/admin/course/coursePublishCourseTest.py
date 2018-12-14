from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.course.coursePublishCourseService import CoursePublishCourseService
from steam.admin.course.courseRemoveCourseService import CourseRemoveCourseService
from steam.admin.course.courseQueryCourseByConditionService import CourseQueryCourseByConditionService
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
class CoursePublishCourseTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/course/publishCourse"
      @initInputService( services = [ CourseCreateCourseService ,
                                      CourseQueryCourseByConditionService ,
                                      CourseRemoveCourseService ],
                         curser     = CoursePublishCourseService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CoursePublishCourseTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.course.courseCreateCourseTest import CourseCreateCourseTest
    from steam.admin.course.courseQueryCourseByConditionTest import CourseQueryCourseByConditionTest
    from steam.admin.course.courseRemoveCourseTest import CourseRemoveCourseTest
    CourseCreateCourseTest(methodName = "compareRetcodeTest",
                                param = [1, 2, 3, 4, 5, {}, 7, 8])
    CourseQueryCourseByConditionTest(methodName = "compareRetcodeTest",
                                          param = [1, 2, 3, 4, 5, {}, 7, 8])
    CourseRemoveCourseTest(methodName = "compareRetcodeTest",
                           param      = [ 1, 2, 3, 4, 5, {}, 7, 8 ])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\course\\operation-manageCoursePublishCourses.yml",
                    testclse     = CoursePublishCourseTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )