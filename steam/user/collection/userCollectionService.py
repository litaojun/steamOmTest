from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
#from steam.util.configurl import userCancelCollectionUrl
from opg.util.httptools import httpPost
from steam.util.httpUopService import  HttpUopService
class UserCollectionService(HttpUopService):
    '''
        用户学习列表
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = "userCollectionContentReq"):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserCollectionService, self).__init__(  module       = modul,
                                                      filename     = filename,
                                                      sqlvaluedict = kwargs ,
                                                       reqjsonfile = None )

    @decorator(["setupUserCollection"])
    def userCollectionContentReq(self):
        self.rsp =  self.sendHttpReq()
        return self.rsp

    @decorator(["preInterfaceUserCollection"])
    def userCancelCollectionReq(self):
        httpPost(
                    url         = userCancelCollectionUrl,
                    reqJsonData = { "resourceId":self.inputKV["resourceId"] },
                    headers     = self.jsonheart
                )

    #@check_rspdata(filepath=weixinUserViewActivityRspFmt)
    def getRetcodeByRsp(self,response  = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

if  __name__ == "__main__":
    kwargs = {
                "resourceId":4448,
                "materialId":15 ,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"18bcd2b48e7f4a89a5f9f5bd5d9918a6"
             }
    uvcSer    = UserCollectionService(kwargs=kwargs)
    courseRsp = uvcSer.userCollectionContentReq()
    print(courseRsp)