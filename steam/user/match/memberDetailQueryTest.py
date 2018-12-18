from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.match.memberDetailQueryService import MemberDetailQueryService
from steam.user.match.userMatchAppleService import UserMatchAppleService
from steam.user.match.userCancelMatchAppleService import UserCancelMatchAppleService
from steam.user.match.userMatchQueryService import UserMatchQueryService
from steam.user.match.userMatchAppleQueryService import UserMatchAppleQueryService
class MemberDetailQueryTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/match-service/member/detail/query"
      @initInputService( services = [ [ UserMatchAppleService , "guosReqjsonfile" ]  ,
                                        UserCancelMatchAppleService ,
                                        UserMatchQueryService ,UserMatchAppleQueryService ] ,
                         curser   = MemberDetailQueryService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MemberDetailQueryTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.match.userMatchAppleTest import UserMatchAppleTest
    from steam.user.match.userCancelMatchAppleTest import UserCancelMatchAppleTest
    from steam.user.match.userMatchQueryTest import UserMatchQueryTest
    from steam.user.match.userMatchAppleQueryTest import UserMatchAppleQueryTest
    UserVerfiyCodeTest(methodName = "compareRetcodeTest",
                       param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserCancelMatchAppleTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserMatchAppleTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserMatchQueryTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserMatchAppleQueryTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\match\\match-serviceMemberDetailQuerys.yml",
                    testclse     = MemberDetailQueryTest  ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )