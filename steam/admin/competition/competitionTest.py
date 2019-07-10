from steam.admin.competition.competitionService import MatchAddService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.competition.competitionDelService import MatchDelService
class MatchAddTest(SteamTestCase):
      '''
            admin新增赛事场次
      '''
      __interfaceName__ = "/operation-manage/match/createMatch"
      @initAdminInputService( curser   = MatchAddService,
                              services = [ [MatchDelService,"delReqjsonfile"] ] )
      def __init__(self, methodName='runTest', param=None):
          super(MatchAddTest,self).__init__(methodName,param)
