from steam.user.home.homeCnfQueryService import HomeCnfQueryService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
class HomeCnfQueryTest(SteamTestCase):
      '''
            用户进入公众号首页，获取运营位数据
      '''
      __interfaceName__ = "/featured/index/configs/queryShowConfigs"
      @initInputService( services = [ ] ,
                         curser   = HomeCnfQueryService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(HomeCnfQueryTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    UserVerfiyCodeTest( methodName = "compareRetcodeTest" ,
                        param      = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    UserLoginTest( methodName     = "compareRetcodeTest" ,
                   param          = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    runTestOneCls( casefilepath =  "\\steamcase\\homepage\\featuredindexconfigsqueryShowConfigss.yml",
				   testclse     =  HomeCnfQueryTest )