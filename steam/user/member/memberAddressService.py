from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService
class MemberAddressService(HttpUopService):
    '''
        微信端用户新增一个地址
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(MemberAddressService, self).__init__("", "", kwargs )

    def memberAddressReq(self):
        # self.rsp = httpGet(url     = memberAddressUrl,
        #                    headers = self.jsonheart)
        self.rsp = self.sendHttpReq()
        return self.rsp

    def getMemberAddressIdFromRsp(self,response=None):
        if response is None:
            #response = self.memberAddressReq()
            response = self.sendHttpReq()
        print("memberAddRSP = %s" % response)
        return query_json(json_content = json.loads(response),
                          query        = "data.0.id")

    def getMemberAddressIdByNameOrTel(self,response = None,conName="",conTel=""):
        if response is None:
            response = self.memberAddressReq()
        id = None
        adsLs = query_json(json_content = json.loads(response),
                           query        = "data")
        for address in adsLs:
            if address["consignee"] == conName and address["phone"] == conTel:
                id = address["id"]
                break
        return id

    # @check_rspdata(filepath=memberAddressRspFmt)
    # def getRetcodeByRsp(self,response = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")
    @decorator(["setupGetUserAddressId","tearDownGetUserAddressId"])
    def setInPutData(self):
        self.inputKV["id"] = self.getMemberAddressIdFromRsp()

if __name__ == "__main__":
    kwargs = {
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4"
             }
    mass = MemberAddressService(kwargs=kwargs)
    rsp = mass.memberAddressReq()
    retcode = mass.getRetcodeByRsp(response=rsp)
    print(retcode)
    addressId = mass.getMemberAddressIdFromRsp(response=rsp)
    print(addressId)
