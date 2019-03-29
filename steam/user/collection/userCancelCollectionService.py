from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.configurl import userCollectionUrl
from opg.util.httptools import httpPost
from steam.util.httpUopService import  HttpUopService
class UserCancelCollectionService(HttpUopService):
    '''
        用户学习列表
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = ""):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserCancelCollectionService, self).__init__(  module      = modul,
                                                           filename     = filename,
                                                      sqlvaluedict      = kwargs ,
                                                       reqjsonfile      = None )

    @decorator(["tearDownUserCancelCollection"])
    def userCancelCollectionReq(self):
        self.rsp =  self.sendHttpReq()
        return self.rsp

    @decorator(["preInterfaceUserCollection"])
    def userCollectionReq(self):
        httpPost(
                    url         = userCollectionUrl,
                    reqJsonData = { "resourceId":self.inputKV["resourceId"] },
                    headers     = self.jsonheart
                )

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
    uvcSer    = UserCancelCollectionService(kwargs=kwargs)
    courseRsp = uvcSer.userCancelCollectionReq()
    print(courseRsp)