from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.merchant.merchantLoginService import MerchantLoginService
from steam.user.merchant.passportVerifyCodeService import PassportVerifyCodeService
class MerchantLoginTest(SteamTestCase):
      """
            商户登录
      """
      __interfaceName__ = "/merchant-service/merchant/login"
      @initInputService( services = [ PassportVerifyCodeService ],
                         curser   = MerchantLoginService ,sign="merchant")
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MerchantLoginTest,self).__init__(methodName,param)

if __name__ == "__main__":
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\merchant\\merchant-serviceMerchantLogins.yml" ,
                    testclse     = MerchantLoginTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )