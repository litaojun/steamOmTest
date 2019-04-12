from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.admin.activity.productAuditService import ProductAuditService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class ProductAuditTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/product/audit"
      @initInputService( services = [ WeixinSearchService ,UserCancelCollectionService ],
                  curser   = ProductAuditService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(ProductAuditTest,self).__init__(methodName,param)

if __name__ == "__main__":
    pass