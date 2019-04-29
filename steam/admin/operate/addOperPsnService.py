from opg.bak.uopService import decorator
from steam.admin.operate.queryOperpsnService import OperpsnQueryService
from steam.util.httpUopService import  HttpUopService
class OperpsnAddService(HttpUopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(OperpsnAddService, self).__init__(sqlvaluedict = kwargs)

    @decorator(["setupAddOperPosition"])
    def addOperPosition(self):
        self.sendHttpReq()

    # def getRetcodeByOperpsnRsp(self,operpsnRsp = None):
    #     return query_json(json_content = json.loads(operpsnRsp),
    #                       query        = "code")
    #
    def getOperpsnIdByTitle(self,title = "",position = ""):
        operQuerySer = OperpsnQueryService(self.inputKV)
        rsplistdataRsp = operQuerySer.queryOperpsnListdata()
        rssid = operQuerySer.getFirstResourceIdByRsp(rsplistdataRsp)
        return rssid

if __name__ == "__main__":
   addOperPsnReqjson = {
							"title"        :   "风靡全球的少儿编程",
							"picPath"      : "http://uat-steam.opg.cn/_static/admin/images/resource/20180425150543_430837.jpg",
							"listOrder"    :  3,
							"resourceId"   :  2027,
	                        "position"     : "03",
	                        "displayType"  : "2",
	                        "oldListOrder" : 0,
                            "token": "69a42b2f9ebd4275a04a602648d857c1"
					   }
   operpsnSer = OperpsnAddService(addOperPsnReqjson)
   rsp = operpsnSer.addOperPosition()
   code = operpsnSer.getRetcodeByOperpsnRsp(operpsnRsp=rsp)
   print("code = %s" % code)
   id = operpsnSer.getOperpsnIdByTitle(rsp)
   print("id = %s" % id)
   operpsnSer.delOperPosition()