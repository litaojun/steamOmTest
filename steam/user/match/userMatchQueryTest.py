from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.match.userMatchQueryService import UserMatchQueryService
from steam.util.testJsonFormat import initInputService
class UserMatchQueryTest(SteamTestCase):
      '''
            微信端用户进入报名页面，获取到赛事，场次，赛题相关信息
      '''
      __interfaceName__   = "/match-service/member/wa/query"
      @initInputService( services = [] ,
                         curser   = UserMatchQueryService )
      def __init__(self, methodName='runTest', param=None):
          super(UserMatchQueryTest,self).__init__(methodName,param)

      def userMatchQueryTest(self):
          rsp     = self.myservice.userMatchQuery()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\match-servicememberwaquerys.yml",
                        testclse     = UserMatchQueryTest,
                        basepath     = "D:\\litaojun\\steamyml"
                 )