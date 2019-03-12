from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.lottery.lotteryQueryLotteryInfoService import LotteryQueryLotteryInfoService
from steam.admin.lottery.lotteryQueryLotteryListService import LotteryQueryLotteryListService
class LotteryQueryLotteryInfoTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/lottery/queryLotteryInfo"
      @initAdminInputService( services = [ LotteryQueryLotteryListService ],
                  curser   = LotteryQueryLotteryInfoService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(LotteryQueryLotteryInfoTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryLotteryListTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\lottery\\operation-manageLotteryQueryLotteryInfos.yml",
                    testclse     = LotteryQueryLotteryInfoTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )