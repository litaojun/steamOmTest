from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.merchant.orderMailService import OrderMailService


class OrderMailTest(SteamTestCase):
      """
            发送订单到商户邮箱
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