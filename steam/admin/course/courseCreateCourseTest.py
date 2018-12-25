from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
from steam.admin.course.courseRemoveCourseService import CourseRemoveCourseService
from steam.admin.course.courseQueryCourseByConditionService import CourseQueryCourseByConditionService
from steam.admin.course.courseCreateCourseService import CourseCreateCourseService
class CourseCreateCourseTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/course/createCourse"
      @initInputService( services = [ CourseQueryCourseByConditionService ,
                                      CourseRemoveCourseService ],
                         curser   =  CourseCreateCourseService )
      def __init__( self, methodName = 'runTest',
                          param      =  None ):
          super(CourseCreateCourseTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.course.courseQueryCourseByConditionTest import CourseQueryCourseByConditionTest
    from steam.admin.course.courseRemoveCourseTest import CourseRemoveCourseTest
    CourseQueryCourseByConditionTest( methodName = "compareRetcodeTest",
                                      param      = [1, 2, 3, 4, 5, {}, 7, 8] )
    CourseRemoveCourseTest( methodName = "compareRetcodeTest" ,
                            param      = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\course\\operation-manageCourseCreateCourses.yml",
                    testclse     = CourseCreateCourseTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )