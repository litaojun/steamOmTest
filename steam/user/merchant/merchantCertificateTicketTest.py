from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.merchant.merchantCertificateTicketService import MerchantCertificateTicketService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class MerchantCertificateTicketTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/ticket-service/merchant/certificateTicket"
      @initInputService( services = [ WeixinSearchService ,UserCancelCollectionService ],
                  curser   = MerchantCertificateTicketService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MerchantCertificateTicketTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.collection.userCancelCollectionTest import UserCancelCollectionTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserCancelCollectionTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\merchant\\ticket-serviceMerchantCertificateTickets.yml",
                    testclse     = MerchantCertificateTicketTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )