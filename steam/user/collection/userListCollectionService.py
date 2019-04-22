# from   steam.util.configurl import userListCollectionUrl
from   opg.util.httptools import httpGet
from   steam.util.httpUopService import  HttpUopService
class UserListCollectionService(HttpUopService):
    '''
        用户学习列表
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserListCollectionService, self).__init__(  module       = modul,
                                                          filename     = filename,
                                                          sqlvaluedict = kwargs ,
                                                           reqjsonfile = reqjsonfile )

    def userListCollectionReq(self):
        self.rsp =  httpGet(
                                  url         = userListCollectionUrl ,
                                  headers     = self.jsonheart
                            )
        return self.rsp

    #@check_rspdata(filepath=weixinUserViewActivityRspFmt)
    # def getRetcodeByRsp(self,response  = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")

if  __name__ == "__main__":
    kwargs = {
                "resourceId":4448,
                "materialId":15 ,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"18bcd2b48e7f4a89a5f9f5bd5d9918a6"
             }
    uvcSer    = UserListCollectionService(kwargs=kwargs)
    courseRsp = uvcSer.userListCollectionReq()
    print(courseRsp)