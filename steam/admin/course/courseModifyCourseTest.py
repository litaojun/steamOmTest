from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.course.courseModifyCourseService import CourseModifyCourseService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class CourseModifyCourseTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/course/modifyCourse"
      @initInputService( services = [ WeixinSearchService ,UserCancelCollectionService ],
                  curser   = CourseModifyCourseService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CourseModifyCourseTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.collection.userCancelCollectionTest import UserCancelCollectionTest
    UserVerfiyCodeTest(methodName = "compareRetcodeTest",
                       param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName = "compareRetcodeTest",
                  param      = [1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserCancelCollectionTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\course\\operation-manageCourseModifyCourses.yml" ,
                    testclse     =  CourseModifyCourseTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )