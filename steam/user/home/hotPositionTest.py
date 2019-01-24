from steam.user.home.hotPositionService import HomeHotPositionService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
class HotPositionTest(SteamTestCase):
      '''
            计算内容
      '''
      __interfaceName__ = "/featured/index/configs/pageQueryPositionShows"
      @initInputService(services=[] ,
                        curser  =HomeHotPositionService)
      def __init__(self, methodName='runTest', param=None):
          super(HotPositionTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest

    UserVerfiyCodeTest( methodName="compareRetcodeTest" ,
                        param=[1, 2, 3, 4, 5, {}, 7, 8] )
    UserLoginTest( methodName="compareRetcodeTest" ,
                   param=[1, 2, 3, 4, 5, {}, 7, 8] )
    runTestOneCls(
					casefilepath =  "\\steamcase\\homepage\\featuredindexconfigspageQueryPositionShowss.yml",
					testclse     =  HotPositionTest
				 )