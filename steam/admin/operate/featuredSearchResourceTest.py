from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.operate.featuredSearchResourceService import FeaturedSearchResourceService
class FeaturedSearchResourceTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/featured/searchResource"
      @initAdminInputService( services = [  ] ,
                         curser   = FeaturedSearchResourceService )
      def __init__( self, methodName = 'runTest',
                          param      =  None ):
          super(FeaturedSearchResourceTest,self).__init__(methodName,param)

if __name__ == "__main__":
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\operate\\operation-manageFeaturedSearchResources.yml" ,
                    testclse     = FeaturedSearchResourceTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )