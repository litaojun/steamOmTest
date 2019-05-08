from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.admin.activity.productAuditService import ProductAuditService
from steam.admin.activity.searchActivityService import ActivitySearchService
from steam.admin.activity.queryActivityService import ActivityQueryService
class ProductAuditTest(SteamTestCase):
      """
            商品活动审核
      """
      __interfaceName__ = "/operation-manage/product/audit"
      @initInputService( services = [ ActivitySearchService ,ActivityQueryService ],
                         curser   = ProductAuditService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(ProductAuditTest,self).__init__(methodName,param)

if __name__ == "__main__":
    pass