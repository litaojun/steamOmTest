from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.member.checkInDailyService import CheckInDailyService
class CheckInDailyTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/member-service/checkIn/daily"
      @initInputService( services = [ ],
                         curser   = CheckInDailyService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(CheckInDailyTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.login.queryMemberIdTest import QueryMemberIdTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    QueryMemberIdTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\member\\member-serviceCheckInDailys.yml",
                    testclse     = CheckInDailyTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )