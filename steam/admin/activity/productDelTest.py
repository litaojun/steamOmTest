from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.admin.activity.productDelService import ProductDelService
from steam.admin.activity.addActivityService import ActivityAddService
class ProductDelTest(SteamTestCase):
      """
            删除活动商品
      """
      __interfaceName__ = "/operation-manage/product/del"
      @initInputService( services = [ [ActivityAddService,"goodsreqjsonfile"]  ],
                         curser   = ProductDelService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(ProductDelTest,self).__init__(methodName,param)

if __name__ == "__main__":
    pass