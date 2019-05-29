import requests,json
from opg.bak.uopService import decorator
from opg.util.utils import query_json
#from steam.util.configurl import alertMatchurl
from opg.util.timeTool import getTimeIntByInPut
from steam.util.httpUopService import  HttpUopService
class CompetitionAlertService(HttpUopService):
    '''
        admin修改赛事场次
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CompetitionAlertService, self).__init__( module       = "",
                                                       filename     = "",
                                                       sqlvaluedict = kwargs,
                                                       reqjsonfile  = None)

    def getRetCodeAlertRsp(self,rsp):
        return query_json(json_content=json.loads(rsp), query="code")

    @decorator(["setupSetMatchNameToAlertMatchName"])
    def addOneCourse(self):
        self.inputKV["matchName"] = self.inputKV["alertMatchName"]

    def alertMatchTime(self,s=1,e=1):
        starttime = getTimeIntByInPut(s)
        endtime   =  getTimeIntByInPut(e)
        self.reqjsondata["applyStartTime"] = starttime
        self.reqjsondata["applyEndTime"] = endtime
        print("set - starttime = %s,endtime=%s" % (starttime, endtime))
        self.alertMatch()


if __name__ == "__main__":
   pass