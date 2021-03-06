from steam.util.steamLog import SteamTestCase
from steam.admin.activity.searchActivityService import ActivitySearchService
from steam.util.testJsonFormat import initAdminInputService

class ActivitySearchTest(SteamTestCase):
      '''
            根据名称搜索活动
      '''
      __interfaceName__ = "/operation-manage/product/queryProducts"

      @initAdminInputService(services = [],
                             curser   = ActivitySearchService)
      def __init__(self, methodName='runTest', param=None):
          super(ActivitySearchTest,self).__init__(methodName,param)

      def checkTestData(self):
          return self.myservice.findTestDataByStatus()

if __name__ == "__main__":
   pass