from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.member.addressDefaultService import AddressDefaultService
from steam.user.member.userAddAddressService import UserAddAddressService
from steam.user.member.userDelAddressService import UserDelAddressService
from steam.user.member.memberAddressService import MemberAddressService
class AddressDefaultTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/member-service/address/default"
      @initInputService( services = [ UserAddAddressService ,
                                      UserDelAddressService ,
                                      MemberAddressService ],
                         curser   = AddressDefaultService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(AddressDefaultTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.member.userAddAddressTest import UserAddAddressTest
    from steam.user.member.userDelAddressTest import UserDelAddressTest
    from steam.user.member.memberAddressTest import MemberAddressTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserAddAddressTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserDelAddressTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    MemberAddressTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\member\\member-serviceAddressDefaults.yml" ,
                    testclse     = AddressDefaultTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )