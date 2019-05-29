
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.operate.queryOperpsnService import OperpsnQueryService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
class OperpsnQueryTest(SteamTestCase):
      '''
            admin查询一个运营位配置
      '''
      __interfaceName__ = "/operation-manage/featured/queryShowConfigs"
      @initAdminInputService( curser = OperpsnQueryService )
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnQueryTest,self).__init__(methodName,param)

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\operate\\steam-featuredhomeConfiglistDatas.yml",
                    testclse     = OperpsnQueryTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )