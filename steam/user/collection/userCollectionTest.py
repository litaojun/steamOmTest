from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.collection.userCollectionService import UserCollectionService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class UserCollectionTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__ = "/resource-service/resource/collect"
      @initInputService( services = [ WeixinSearchService ,UserCancelCollectionService ],
                  curser   = UserCollectionService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(UserCollectionTest,self).__init__(methodName,param)

      def userCollectTest(self):
          rsp        = self.myservice.userCollectionContentReq()
          rspcode    = self.myservice.getRetcodeByRsp( response = rsp )
          self.assertTrue(rspcode == self.expectdata["code"],
                          msg      = "rspcode=%s,expectcode=%s" % (rspcode,self.expectdata["code"]))

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.collection.userCancelCollectionTest import UserCancelCollectionTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                  param=[1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName = "compareRetcodeTest",
                     param      = [1, 2, 3, 4, 5, {}, 7, 8])
    UserCancelCollectionTest(methodName = "compareRetcodeTest",
                             param      = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\resource-serviceresourcecollects.yml",
                    testclse     = UserCollectionTest
                )