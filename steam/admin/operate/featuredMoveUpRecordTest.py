from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.operate.featuredMoveUpRecordService import FeaturedMoveUpRecordService
from steam.admin.operate.addOperPsnService import OperpsnAddService
from steam.admin.operate.delOperpsnService import OperpsnDelService
from steam.admin.operate.featuredSearchResourceService import FeaturedSearchResourceService
from steam.admin.operate.queryOperpsnService import OperpsnQueryService
class FeaturedMoveUpRecordTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/featured/moveUpRecord"
      @initAdminInputService( services = [ OperpsnQueryService ,FeaturedSearchResourceService,
                                      OperpsnAddService,OperpsnDelService ],
                  curser   = FeaturedMoveUpRecordService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(FeaturedMoveUpRecordTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.operate.addOperPsnTest import OperpsnAddTest
    from steam.admin.operate.delOperpsnTest import OperpsnDelTest
    from steam.admin.operate.featuredSearchResourceTest import FeaturedSearchResourceTest
    from steam.admin.operate.queryOperpsnTest import OperpsnQueryTest
    OperpsnAddTest(methodName="compareRetcodeTest",
                   param=[1, 2, 3, 4, 5, {}, 7, 8])
    OperpsnDelTest(methodName="compareRetcodeTest",
                   param=[1, 2, 3, 4, 5, {}, 7, 8])
    FeaturedSearchResourceTest(methodName="compareRetcodeTest",
                               param=[1, 2, 3, 4, 5, {}, 7, 8])
    OperpsnQueryTest(methodName="compareRetcodeTest",
                     param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\operate\\operation-manageFeaturedMoveUpRecords.yml",
                    testclse     = FeaturedMoveUpRecordTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )