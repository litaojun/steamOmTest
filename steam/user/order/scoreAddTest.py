from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.order.scoreAddService import ScoreAddService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.order.userOrederActivityService import UserOrderActivityService
from steam.user.weixin.userViewCourseService import UserViewCourseService
class ScoreAddTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/order-service/score/add"
      @initInputService( services = [ WeixinSearchService ,
                                      UserOrderActivityService ,
                                      UserViewCourseService ] ,
                         curser   = ScoreAddService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(ScoreAddTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.order.userOrderActivityTest  import UserOrderActivityTest
    from steam.user.weixin.userViewCourseTest import UserViewCourseTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserOrderActivityTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserViewCourseTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\order\\order-serviceScoreAdds.yml" ,
                    testclse     = ScoreAddTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )