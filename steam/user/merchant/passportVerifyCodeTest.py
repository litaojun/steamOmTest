from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.merchant.passportVerifyCodeService import PassportVerifyCodeService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class PassportVerifyCodeTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/merchant/passport/verifyCode"
      @initInputService( services=[ ],
                         curser=PassportVerifyCodeService ,
                         sign="merchant")
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(PassportVerifyCodeTest,self).__init__(methodName,param)

if __name__ == "__main__":
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\merchant\\merchantPassportVerifyCodes.yml",
                    testclse     = PassportVerifyCodeTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )