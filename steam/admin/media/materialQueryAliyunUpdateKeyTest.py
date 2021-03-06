from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.media.materialQueryAliyunUpdateKeyService import MaterialQueryAliyunUpdateKeyService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class MaterialQueryAliyunUpdateKeyTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/material/queryAliyunUpdateKey"
      @initAdminInputService( services = [ WeixinSearchService ,UserCancelCollectionService ],
                              curser   = MaterialQueryAliyunUpdateKeyService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MaterialQueryAliyunUpdateKeyTest,self).__init__(methodName,param)

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
                    casefilepath = "\\steamcase\\admin\\media\\operation-manageMaterialQueryAliyunUpdateKeys.yml" ,
                    testclse     = MaterialQueryAliyunUpdateKeyTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )