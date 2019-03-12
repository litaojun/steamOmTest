from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.lottery.lotteryQueryPrizeRosterService import LotteryQueryPrizeRosterService
from steam.admin.lottery.lotteryQueryLotteryListService import LotteryQueryLotteryListService
class LotteryQueryPrizeRosterTest(SteamTestCase):
      """
            查看中奖名单
      """
      __interfaceName__ = "/operation-manage/lottery/queryPrizeRoster"
      @initAdminInputService( services = [ LotteryQueryLotteryListService ],
                              curser   = LotteryQueryPrizeRosterService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(LotteryQueryPrizeRosterTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.admin.lottery.lotteryQueryPrizeInventoryTest import LotteryQueryPrizeInventoryTest
    from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListTest

    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryLotteryListTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryPrizeInventoryTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\lottery\\operation-manageLotteryQueryPrizeRosters.yml",
                    testclse     = LotteryQueryPrizeRosterTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )