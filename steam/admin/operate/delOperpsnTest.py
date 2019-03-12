from steam.admin.operate.delOperpsnService import OperpsnDelService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.operate.addOperPsnService import OperpsnAddService
from steam.admin.operate.queryOperpsnService import OperpsnQueryService
from steam.admin.article.ArticleSearchService import ArticleSearchService
class OperpsnDelTest(SteamTestCase):
      '''
            admin删除一个运营位配置
      '''
      __interfaceName__ = "/operation-manage/featured/removeIndexConfig"
      @initAdminInputService( services = [ OperpsnAddService ,
                                      OperpsnQueryService ,
                                      ArticleSearchService ] ,
                         curser   = OperpsnDelService )
      def __init__( self, methodName = 'runTest' ,
                          param      = None ):
          super(OperpsnDelTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.operate.queryOperpsnTest import OperpsnQueryTest
   from steam.admin.operate.addOperPsnTest import OperpsnAddTest
   from steam.admin.article.ArticleSearchTest import ArticleSearchTest
   OperpsnAddTest(methodName = "compareRetcodeTest",
                   param     = [ 1, 2, 3, 4, 5, {}, 7, 8])
   OperpsnQueryTest(methodName = "compareRetcodeTest",
                   param     = [ 1, 2, 3, 4, 5, {}, 7, 8])
   ArticleSearchTest(methodName = "compareRetcodeTest",
                   param     = [ 1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\operate\\steam-featuredhomeConfigremoveIndexConfigs.yml"  ,
                    testclse     = OperpsnDelTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )