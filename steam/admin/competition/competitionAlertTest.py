from steam.util.testJsonFormat import initAdminInputService
from steam.admin.competition.competitionAlertService import CompetitionAlertService
from steam.admin.competition.competitionService import MatchAddService
from steam.admin.competition.competitionDelService import MatchDelService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class CompetitionAlertTest(SteamTestCase):
      '''
            admin修改赛事场次
      '''
      __interfaceName__ = "/operation-manage/match/updateMatchById"
      @initAdminInputService(curser = CompetitionAlertService,
                        services = [ MatchAddService,
                                   [ MatchDelService , "delReqjsonfile" ]])
      def __init__(self, methodName='runTest', param=None):
          super(CompetitionAlertTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.competition.competitionDelTest import MatchDelTest
   MatchDelTest(methodName = "compareRetcodeTest", param = [1, 2, 3, 4, 5, {}, 7, 8])
   from steam.admin.competition.competitionTest import MatchAddTest
   MatchAddTest(methodName = "compareRetcodeTest", param = [1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\competition\\match-servicematchupdateMatchByIds.yml" ,
                    testclse     = CompetitionAlertTest
                )