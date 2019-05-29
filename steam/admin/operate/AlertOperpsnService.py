
from opg.bak.uopService import decorator
import requests,json
from opg.util.utils import query_json
#from steam.util.configurl import alertOperpositionurl,delOperpositionurl
from steam.admin.operate.addOperPsnService import  OperpsnAddService
from steam.util.httpUopService import  HttpUopService
class OperpsnAlertService(HttpUopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        super(OperpsnAlertService, self).__init__(sqlvaluedict = kwargs)
        self.operpsnAddSer = OperpsnAddService(self.inputKV)

    @decorator(["setupSetAlertResource"])
    def getFirstSearchAlertResource(self):
        self.inputKV["alertTitle"] , \
        self.inputKV["title"] = self.inputKV["alertTitle"] ,\
                                 self.inputKV["title"]
    # @decorator("preInterfaceAddOneOperpsn")
    # def addOneOperpsn(self):
    #     operpsnAddRsp = self.operpsnAddSer.addOperPosition()
    #     self.rsp      = operpsnAddRsp
    #     self.reqjsondata["id"] = self.operpsnAddSer.getOperpsnIdByTitle()

    # def getRetCodeOperpsnRsp(self,rsp):
    #     return query_json(json_content=json.loads(rsp), query="code")

if __name__ == "__main__":
   alertjson = {
					"title"         :  "Makeblock 2017 品牌视频",
					"picPath"       : "http://uat-steam.opg.cn/_static/admin/images/resource/20180425112224_258421.jpg",
					"position"      : "03",
					"oldListOrder"  : 1,
					"listOrder"     : 1,
					"displayType"   : "1",
                    "resourceId"    : 121,
					"itemId"         : 121,
					"id"              :  52,
                    "token"          :  "69a42b2f9ebd4275a04a602648d857c1"
			    }
   operAlertSer = OperpsnAlertService(alertjson)
   addrsp = operAlertSer.addOneOperpsn()
   alertRsp = operAlertSer.alertOperpsn()
   print(alertRsp)
   code = operAlertSer.getRetCodeOperpsnRsp(alertRsp)
   print("code=%s" % code)
   delRsp = operAlertSer.delOperpsn()
   print("delRsp=%s" % delRsp)