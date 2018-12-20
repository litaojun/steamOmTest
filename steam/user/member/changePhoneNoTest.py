from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.member.changePhoneNoService import ChangePhoneNoService
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
class ChangePhoneNoTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/member-service/changePhoneNo"
      @initInputService( services = [ [WeixinUserVerfiyCodeService,"alterPhoneReqFile"] ] ,
                         curser   = ChangePhoneNoService )
      def __init__(self, methodName = 'runTest',
                          param      =  None):
          super(ChangePhoneNoTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\member\\member-serviceChangePhoneNos.yml",
                    testclse     = ChangePhoneNoTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )