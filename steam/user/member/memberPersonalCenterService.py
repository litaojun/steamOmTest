
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import memberPersonalCenterUrl
from opg.util.schemajson import check_rspdata
from opg.util.httptools import httpGet
class MemberPersonalCenterService(UopService):
    '''
        微信端用户个人信息页面
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(MemberPersonalCenterService, self).__init__("", "", kwargs )

    def memberPersonalCenterReq(self):
        self.rsp = httpGet(url     = memberPersonalCenterUrl,
                           headers = self.jsonheart)
        return self.rsp

    #@check_rspdata(filepath="")
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")


if __name__ == "__main__":
    kwargs = {
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "phoneNo": "18916899938",
                "token":"bb2332122d3e4ac0a15892de5e5d68e3"
             }
    mpcser = MemberPersonalCenterService(kwargs=kwargs)
    rsp = mpcser.memberPersonalCenterReq()
    retcode =  mpcser.getRetcodeByRsp(response=rsp)
    print(retcode)
    print(rsp)