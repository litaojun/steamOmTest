from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.lottery.lotteryDrawService import LotteryDrawService
from steam.admin.lottery.lotteryQueryLotteryListService import LotteryQueryLotteryListService
from steam.user.lottery.lotteryDetailService import LotteryDetailService
class LotteryDrawTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/steam-lottery/lottery/draw"
      @initInputService(services = [LotteryQueryLotteryListService , LotteryDetailService],
                        curser   =  LotteryDrawService)
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(LotteryDrawTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.lottery.lotteryDetailTest import LotteryDetailTest
    from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListTest
    from steam.user.login.queryMemberIdTest import QueryMemberIdTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    QueryMemberIdTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryLotteryListTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    LotteryDetailTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\lottery\\steam-lotteryLotteryDraws.yml" ,
                    testclse     = LotteryDrawTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )