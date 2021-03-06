from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.weixin.resourceVisitService import ResourceVisitService
from steam.util.testJsonFormat import initInputService
from steam.user.search.weixinSearchService import WeixinSearchService
class ResourceVisitTest(SteamTestCase):
      '''
            用户浏览视频文章
      '''
      __interfaceName__   = "/steam-resource/product/detail"
      @initInputService( services = [ WeixinSearchService ],
                         curser   = ResourceVisitService )
      def __init__(self, methodName = 'runTest',
                         param      = None      ):
          super(ResourceVisitTest,self).__init__(methodName,param)

      # def userVisitResourceNor(self):
      #     articlersp = self.myservice.sendInterfaceUrlReq()
      #     rspcode    = self.myservice.getRetcodeByRsp(response = articlersp)
      #     self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   from steam.user.search.weixinSearchTest import WeixinSearchTest
   WeixinSearchTest(methodName="compareRetcodeTest",param = [1,2,3,4,5,{},7,8])
   from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
   from steam.user.login.userLoginTest import UserLoginTest
   UserVerfiyCodeTest(methodName="compareRetcodeTest",
                      param=[1, 2, 3, 4, 5, {}, 7, 8])
   UserLoginTest(methodName="compareRetcodeTest",
                 param=[1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\steam-resourceproductdetails.yml",
                    testclse     = ResourceVisitTest
                )