from steam.util.testJsonFormat import initAdminInputService
from steam.admin.competition.competitionAlertService import CompetitionAlertService
from steam.admin.competition.competitionService import MatchAddService
from steam.admin.competition.competitionDelService import MatchDelService
from steam.util.steamLog import SteamTestCase
class CompetitionAlertTest(SteamTestCase):
      '''
          admin修改赛事场次
      '''
      __interfaceName__ = "/operation-manage/match/updateMatchById"
      @initAdminInputService(curser   = CompetitionAlertService,
                             services = [ MatchAddService,
                                        [ MatchDelService , "delReqjsonfile" ]])
      def __init__(self, methodName='runTest', param=None):
          super(CompetitionAlertTest,self).__init__(methodName,param)
