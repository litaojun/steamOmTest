from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from steam.util.testJsonFormat import initInputService
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.util.steamLog import SteamTestCase
class UserLoginTest(SteamTestCase):
      '''
            微信端用户通过手机号码登录
      '''
      __interfaceName__   = "/member/login/memberLogin"
      @initInputService( services = [ WeixinUserVerfiyCodeService ] ,
                         curser   =   WeixinUserLoginService )
      def __init__( self, methodName = 'runTest',
                          param      = None ):
          super(UserLoginTest,self).__init__(methodName,param)

if  __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\memberloginmemberLogins.yml",
                        testclse     = UserLoginTest
                 )