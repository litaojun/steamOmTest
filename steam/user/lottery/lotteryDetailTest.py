from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.lottery.lotteryDetailService import LotteryDetailService
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

