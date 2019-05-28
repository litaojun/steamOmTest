from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.admin.media.materialAuditService import MaterialAuditService
from steam.admin.media.materialCreateMaterialService import MaterialCreateMaterialService
from steam.admin.media.materialRemoveMaterialService import MaterialRemoveMaterialService
from steam.admin.media.queryMerchantInfoByCondtionService import QueryMerchantInfoByCondtionService
class MaterialAuditTest(SteamTestCase):
      """
            审核素材
      """
      __interfaceName__ = "/operation-manage/material/audit"
      @initInputService( services = [ MaterialCreateMaterialService,MaterialRemoveMaterialService,
                                      QueryMerchantInfoByCondtionService ],
                  curser   = MaterialAuditService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MaterialAuditTest,self).__init__(methodName,param)

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
                    casefilepath = "\\steamcase\\admin\\media\\operation-manageMaterialAudits.yml",
                    testclse     = MaterialAuditTest
                 )