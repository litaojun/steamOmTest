from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.operate.featuredMoveDownRecordService import FeaturedMoveDownRecordService
from steam.admin.operate.addOperPsnService import OperpsnAddService
from steam.admin.operate.delOperpsnService import OperpsnDelService
from steam.admin.operate.featuredSearchResourceService import FeaturedSearchResourceService
from steam.admin.operate.queryOperpsnService import OperpsnQueryService
class FeaturedMoveDownRecordTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/featured/moveDownRecord"
      @initInputService( services = [ OperpsnQueryService ,FeaturedSearchResourceService,
                                      OperpsnAddService,OperpsnDelService ],
                  curser   = FeaturedMoveDownRecordService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(FeaturedMoveDownRecordTest,self).__init__(methodName,param)

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
                    casefilepath = "\\steamcase\\admin\\operate\\operation-manageFeaturedMoveDownRecords.yml",
                    testclse     = FeaturedMoveDownRecordTest
                 )