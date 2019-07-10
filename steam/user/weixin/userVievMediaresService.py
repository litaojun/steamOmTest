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

