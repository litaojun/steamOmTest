from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.merchant.merchantQueryMerchantResourcesService import MerchantQueryMerchantResourcesService
class MerchantQueryMerchantResourcesTest(SteamTestCase):
      """
            商户页
      """
      __interfaceName__ = "/merchant-service/merchant/queryMerchantResources"
      @initInputService( services = [  ],
                         curser   = MerchantQueryMerchantResourcesService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MerchantQueryMerchantResourcesTest,self).__init__(methodName,param)

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
                    casefilepath = "\\steamcase\\user\\merchant\\merchant-serviceMerchantQueryMerchantResourcess.yml",
                    testclse     = MerchantQueryMerchantResourcesTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )