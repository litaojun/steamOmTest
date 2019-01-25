from steam.util.testJsonFormat import initInputService,initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.lottery.lotteryReleaseOrOfflineLotteryService import LotteryReleaseOrOfflineLotteryService
from steam.admin.lottery.lotteryQueryLotteryListService import LotteryQueryLotteryListService
class LotteryReleaseOrOfflineLotteryTest(SteamTestCase):
      """
            上下架抽奖活动
      """
      __interfaceName__ = "/operation-manage/lottery/releaseOrOfflineLottery"
      @initAdminInputService( services = [ LotteryQueryLotteryListService  ],
                              curser   = LotteryReleaseOrOfflineLotteryService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(LotteryReleaseOrOfflineLotteryTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListTest
    from steam.user.login.queryMemberIdTest import QueryMemberIdTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryLotteryListTest(methodName = "compareRetcodeTest",
                                param      = [1, 2, 3, 4, 5, {}, 7, 8])
    QueryMemberIdTest(methodName = "compareRetcodeTest",
                      param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\lottery\\operation-manageLotteryReleaseOrOfflineLotterys.yml",
                    testclse     = LotteryReleaseOrOfflineLotteryTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )