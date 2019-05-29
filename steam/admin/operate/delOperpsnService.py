from opg.bak.uopService import decorator
from steam.admin.operate.addOperPsnService import  OperpsnAddService
from steam.util.httpUopService import  HttpUopService
class OperpsnDelService(HttpUopService):
    '''
        删除一个运营位配置
    '''
    def __init__(self, kwargs):
        super(OperpsnDelService, self).__init__(sqlvaluedict = kwargs)
        self.operpsnAddSer = OperpsnAddService(self.inputKV)

    @decorator(["setupDelOneOperpsn","tearDownDelOneOperpsn"])
    def delOperpsn(self):
        self.sendHttpReq()

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