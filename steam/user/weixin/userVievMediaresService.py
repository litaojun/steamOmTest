import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService
class UserViewMediaresService(HttpUopService):
    '''
        用户端通过文章ID浏览详情页面
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
        :param kwarg:
        :param modul:
        :param filename:
        :param reqjsonfile:
        """
        super(UserViewMediaresService, self).__init__(module      = modul,
                                                      filename    = filename,
                                                      sqlvaluedict= kwargs ,
                                                      reqjsonfile = reqjsonfile)

    def userViewMediares(self):
        self.rsp = self.sendHttpReq()
        return self.rsp


    def getCollectsNumByRsp(self,response = None):
        return query_json(json_content=json.loads(response),
                          query       ="data.collects")

if  __name__ == "__main__":
    kwarg = {
                "memberId": "e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "title": "OM的诞生与发展",
                "resourceTypeId": 2,
                "token":     "ca9fb71fa3bf48879be4f0a3ecd93ed5",
                "resourceId": 5316
            }
    UserViewMediaresService.__interfaceName__ = "/steam-media/media/getMediaDetailByID"
    aqs = UserViewMediaresService(kwargs=kwarg)
    queryResultRsp = aqs.sendHttpReq()
    # rsid = aqs.getFirstResourceIdByRsp(queryRsp=queryResultRsp)
    # kwarg["resourceId"] = rsid
    # uvms = UserViewMediaresService(kwarg=kwarg)
    # rsp = uvms.userViewMediares()
    # retcode = uvms.getRetcodeByRsp(response=rsp)
    # print(retcode)
    # collNum = uvms.getCollectsNumByRsp(response=rsp)
    # print(collNum)