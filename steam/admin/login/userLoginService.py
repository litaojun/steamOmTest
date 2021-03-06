from opg.bak.uopService import UopService,decorator
from opg.util.httptools import httpPost
# from steam.util.configurl import adminLoginUrl
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
import json
class UserLoginService(UopService):
    token = None
    def __init__(self,kwargs):
        super(UserLoginService, self).__init__(module       =  "",
	                                           filename     =  "",
                                               sqlvaluedict =  kwargs,
                                               reqjsonfile  =  "userLoginReq")

    @decorator("interfaceUserLoginMobile")
    def userLogin(self):
        self.rsp = httpPost(url   = adminLoginUrl,
                            headers =  self.jsonheart,
                            reqJsonData = self.reqjsondata)
        return self.rsp

    @check_rspdata(filepath="userLoginRspFmt")
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    def getTokenByRsp(self,response = None):
        if response is None:
            response = self.userLogin()
        return query_json(json_content=json.loads(response), query="token")

    @classmethod
    def getTokenData(cls):
        if cls.token is None:
           kwgs = {
                        "username": "cuiyiming",
                        "password": "68039c0183cd34950fc57726f3b23446701c36a7898e66a61a805f4474b5a63c"
                   }
           rsp = httpPost(url         = adminLoginUrl,
                          headers     =  {},
                          reqJsonData = kwgs)
           cls.token = query_json(json_content=json.loads(rsp), query="token")
        return cls.token

if __name__ == "__main__":
   token = UserLoginService.getTokenData()
   print(token)