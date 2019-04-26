from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService
class UserAddAddressService(HttpUopService):
    '''
        微信端用户获取地址列表
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserAddAddressService, self).__init__("", "", kwargs)

    @decorator(["setupUserAddAddress"])
    def userAddAddressReq(self):
        self.rsp = self.sendHttpReq()
        return self.rsp

if __name__ == "__main__":
    kwargs = {
                    "consignee": "李菠萝",
                    "phone": "18916899938",
                    "address": "空空",
                    "addressCode": "110000,110100,110101",
                    "province": "北京市",
                    "city": "市辖区",
                    "county": "东城区",
                    "isDefault": "01",
                     "memberId": "e99abfeb-1ae5-41d8-a422-63bc108026d4"
                }
    mass = UserAddAddressService(kwargs=kwargs)
    rsp = mass.userAddAddressReq()
    retcode = mass.getRetcodeByRsp(response=rsp)
    print(retcode)