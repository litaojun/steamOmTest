from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.activity.upActivityService import ActivityPublishService
from steam.admin.activity.searchActivityService import ActivitySearchService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
class ActivityPublishTest(SteamTestCase):
      '''
            根据ID搜索活动
      '''
      __interfaceName__ = "/operation-manage/product/publish"

      @initAdminInputService(services = [ ActivitySearchService ],
                             curser   =  ActivityPublishService)
      def __init__(self, methodName='runTest', param=None):
          super(ActivityPublishTest,self).__init__(methodName,param)

      def publishActivityTest(self):
          oneActRsp = self.myservice.publishActivitySer()
          code      = self.myservice.getRetcodeByUpactRsp(oneActRsp = oneActRsp)
          self.assertTrue(code == self.expectdata["code"])


if __name__ == "__main__":
    from steam.admin.activity.searchActivityTest import ActivitySearchTest
    ActivitySearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
				     casefilepath = "\\steamcase\\activity\\operation-manageproductpublishs.yml",
				     testclse     = ActivityPublishTest
			      )