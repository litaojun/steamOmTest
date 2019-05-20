from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initInputService
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from steam.util.steamLog import SteamTestCase
class UserVerfiyCodeTest(SteamTestCase):
      '''
            微信端用户通过手机号码登录
      '''
      __interfaceName__ = "/passport/verifyCode"
      @initInputService(services = [],
                        curser   = WeixinUserVerfiyCodeService)
      def __init__( self, methodName = 'runTest',
                          param      = None ):
          super(UserVerfiyCodeTest,self).__init__(methodName,param)


if  __name__ == "__main__":
    from steam.user.login.userLoginTest import UserLoginTest
    UserLoginTest(methodName="compareRetcodeTest",
                   param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\passportverifyCodes.yml",
                        testclse     = UserVerfiyCodeTest
                  )