from steam.admin.competition.competitionDelService import MatchDelService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.competition.competitionService import MatchAddService
class MatchDelTest(SteamTestCase):
      '''
           admin删除赛事场次
      '''
      __interfaceName__ = "/operation-manage/match/deleteMatch"
      @initAdminInputService( curser   = MatchDelService ,
                              services = [ [ MatchAddService,"addReqjsonfile" ] ] )
      def __init__(self, methodName='runTest', param=None):
          super(MatchDelTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.competition.competitionTest import MatchAddTest
   MatchAddTest(methodName = "compareRetcodeTest", param = [1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(casefilepath = "\\steamcase\\competition\\match-servicematchdeleteMatchs.yml",
                 testclse     = MatchDelTest)