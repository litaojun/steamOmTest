from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.match.matchMatchPageService import MatchMatchPageService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class MatchMatchPageTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/match/matchPage"
      @initInputService( services = [  ],
                  curser   = MatchMatchPageService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MatchMatchPageTest,self).__init__(methodName,param)
      def checkTestData(self):
          return self.myservice.checkTestdataByState()

if __name__ == "__main__":
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\match\\operation-manageMatchMatchPages.yml",
                    testclse     = MatchMatchPageTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )