from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService
class CompetitionAlertService(HttpUopService):
      '''
          admin修改赛事场次
      '''
      def __init__(self, kwargs):
          super(CompetitionAlertService, self).__init__( module     = "",
                                                       filename     = "",
                                                       sqlvaluedict = kwargs,
                                                       reqjsonfile  = None)

      @decorator(["setupSetMatchNameToAlertMatchName"])
      def addOneCourse(self):
          self.inputKV["matchName"] = self.inputKV["alertMatchName"]

if __name__ == "__main__":
   pass