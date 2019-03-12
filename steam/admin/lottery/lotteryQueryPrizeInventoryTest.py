from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.lottery.lotteryQueryPrizeInventoryService import LotteryQueryPrizeInventoryService
from steam.admin.lottery.lotteryQueryLotteryListService import LotteryQueryLotteryListService
class LotteryQueryPrizeInventoryTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/lottery/queryPrizeInventory"
      @initAdminInputService( services = [ LotteryQueryLotteryListService  ],
                  curser   = LotteryQueryPrizeInventoryService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(LotteryQueryPrizeInventoryTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListTest
    LotteryQueryLotteryListTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\lottery\\operation-manageLotteryQueryPrizeInventorys.yml",
                    testclse     = LotteryQueryPrizeInventoryTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )