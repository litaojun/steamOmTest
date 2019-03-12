from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.match.matchMatchPageService import MatchMatchPageService


class MatchMatchPageTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/match/matchPage"
      @initAdminInputService( services = [  ],
                  curser   = MatchMatchPageService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MatchMatchPageTest,self).__init__(methodName,param)
      def checkTestData(self):
          return self.myservice.checkTestdataByState()

if __name__ == "__main__":
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\match\\operation-manageMatchMatchPages.yml" ,
                    testclse     = MatchMatchPageTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )