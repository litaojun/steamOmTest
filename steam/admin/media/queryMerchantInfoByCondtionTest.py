from steam.util.testJsonFormat import initInputService
from steam.util.steamLog     import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.media.queryMerchantInfoByCondtionService import QueryMerchantInfoByCondtionService
class QueryMerchantInfoByCondtionTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/material/queryMaterialByCondition"
      @initInputService( services = [  ],
                         curser   = QueryMerchantInfoByCondtionService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(QueryMerchantInfoByCondtionTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\media\\merchantQueryMerchantInfoByCondtions.yml",
                    testclse     = QueryMerchantInfoByCondtionTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )