from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.media.materialQueryAliyunVideoAuthService import MaterialQueryAliyunVideoAuthService
from steam.admin.media.queryMerchantInfoByCondtionService import QueryMerchantInfoByCondtionService
class MaterialQueryAliyunVideoAuthTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/material/queryAliyunVideoAuth"
      @initAdminInputService( services = [ QueryMerchantInfoByCondtionService ],
                         curser   = MaterialQueryAliyunVideoAuthService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MaterialQueryAliyunVideoAuthTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.media.queryMerchantInfoByCondtionTest import QueryMerchantInfoByCondtionTest
    QueryMerchantInfoByCondtionTest( methodName = "compareRetcodeTest" ,
                                     param      = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\media\\operation-manageMaterialQueryAliyunVideoAuths.yml",
                    testclse     = MaterialQueryAliyunVideoAuthTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )