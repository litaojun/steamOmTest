from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.lottery.lotteryDetailService import LotteryDetailService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListService
class LotteryDetailTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/steam-lottery/lottery/detail"
      @initInputService( services = [ LotteryQueryLotteryListService ],
                         curser   = LotteryDetailService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(LotteryDetailTest,self).__init__(methodName , param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.admin.lottery.lotteryQueryLotteryListTest import LotteryQueryLotteryListTest
    # from steam.user.collection.userCancelCollectionTest import UserCancelCollectionTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    LotteryQueryLotteryListTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\lottery\\steam-lotteryLotteryDetails.yml" ,
                    testclse     = LotteryDetailTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )