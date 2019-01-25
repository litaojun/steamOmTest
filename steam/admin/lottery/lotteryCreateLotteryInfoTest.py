from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.lottery.lotteryCreateLotteryInfoService import LotteryCreateLotteryInfoService
from steam.admin.lottery.lotteryQueryLotteryListService import LotteryQueryLotteryListService
from steam.admin.lottery.lotteryQueryLotteryInfoService import LotteryQueryLotteryInfoService
class LotteryCreateLotteryInfoTest(SteamTestCase):
      """
            新增抽奖活动
      """
      __interfaceName__ = "/operation-manage/lottery/createLotteryInfo"
      @initAdminInputService( services = [ LotteryQueryLotteryInfoService ,
                                           LotteryQueryLotteryListService ] ,
                              curser   =   LotteryCreateLotteryInfoService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(LotteryCreateLotteryInfoTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.admin.lottery.lotteryQueryLotteryInfoTest import LotteryQueryLotteryInfoTest
    from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryLotteryListTest(methodName="compareRetcodeTest",
                                param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryLotteryInfoTest(methodName="compareRetcodeTest",
                                param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\lottery\\operation-manageLotteryCreateLotteryInfos.yml" ,
                    testclse     = LotteryCreateLotteryInfoTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )