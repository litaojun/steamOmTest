from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.merchant.orderMailService import OrderMailService
from steam.user.merchant.merchantLoginService import MerchantLoginService
class OrderMailTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/merchant/order/mail"
      @initInputService( services = [ ] ,
                         curser   = OrderMailService ,sign="merchant")
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(OrderMailTest,self).__init__(methodName,param)

if __name__ == "__main__":
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\merchant\\merchantOrderMails.yml",
                    testclse     = OrderMailTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )