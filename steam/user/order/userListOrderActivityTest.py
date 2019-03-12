from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.order.userListOrderActivityService import UserListOrderActivityService
from steam.util.testJsonFormat import initInputService
class UserListOrderActivityTest(SteamTestCase):
      '''
            用户查询订单列表
      '''
      __interfaceName__ = "/order-service/order"
      @initInputService(services=[],
                        curser=UserListOrderActivityService)
      def __init__(self, methodName='runTest', param=None):
          super(UserListOrderActivityTest,self).__init__(methodName,param)

if  __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.weixin.userViewActivityTest import UserViewActivityTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.member.memberAddressTest import MemberAddressTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserViewActivityTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    MemberAddressTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\order-serviceorders.yml",
                        testclse = UserListOrderActivityTest
                 )