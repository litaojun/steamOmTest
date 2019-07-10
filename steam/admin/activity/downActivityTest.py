from steam.admin.activity.downActivityService import ActivityUnPublishService
from steam.admin.activity.addActivityService import ActivityAddService
from steam.admin.activity.productAuditService import ProductAuditService
from steam.admin.activity.upActivityService import ActivityPublishService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
class ActivityUnPublishTest(SteamTestCase):
      '''
            根据ID下架活动
      '''
      __interfaceName__ = "/operation-manage/product/unPublish"
      @initAdminInputService(services = [ [ActivityAddService,"goodsreqjsonfile"],
                                          ProductAuditService,ActivityPublishService ],
                 curser   =   ActivityUnPublishService )
      def __init__(self, methodName = 'runTest', param = None ):
          super(ActivityUnPublishTest,self).__init__(methodName,param)

      def upPublishActivityTest(self):
          oneActRsp = self.myservice.unPublishActivitySer()
          code      = self.myservice.getRetcodeByRsp(oneActRsp = oneActRsp)
          self.assertTrue(code == self.expectdata["code"])

      def testHome_t(self):
          pass