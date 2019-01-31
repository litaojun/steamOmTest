from opg.unit.parametrized import ParametrizedTestCase
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from steam.admin.login.userLoginService import UserLoginService
from steam.user.login.QueryMemberIdService import QueryMemberIdService

class SteamTestCase(ParametrizedTestCase):
    '''
          用户进入公众号首页，获取运营位数据
    '''
    __interfaceName__ = "/featured/index/configs/queryShowConfigs"
    memberIdDict      = {}

    def __init__(self, methodName='runTest', param=None):
        super(SteamTestCase, self).__init__(methodName, param)

    def getInputDataInit(self):
        inputData = self.getInputData()
        if "phoneNo" in inputData:
            if inputData["phoneNo"] in SteamTestCase.memberIdDict :
               inputData["token"]    = SteamTestCase.memberIdDict[inputData["phoneNo"]][0]
               inputData["memberId"] = SteamTestCase.memberIdDict[inputData["phoneNo"]][1]
            else:
               inputData["scenes"] = "OTP"
               userVerCodeSer = WeixinUserVerfiyCodeService(kwargs = inputData)
               sedCodeRsp     = userVerCodeSer.sendUserVerifyCode()
               retcode        = userVerCodeSer.getRetcodeByRsp(response = sedCodeRsp)
               if retcode == "000000":
                  verfiyCode               = userVerCodeSer.getVerfiyCodeFromRedisByPhone(phoneNum=inputData["phoneNo"])
                  inputData["verfiyCode"] = verfiyCode
                  userLoginSer             = WeixinUserLoginService(kwargs=inputData)
                  rsp  = userLoginSer.weixinUserLogin()
                  code = userLoginSer.getRetcodeByUserLoginRsp(response=rsp)
                  if code  == "000000":
                     token = userLoginSer.getTokenFromRsp(response=rsp)
                     self.inputdata["token"] = token
                     qmIdSer = QueryMemberIdService(kwargs=inputData)
                     rsp = qmIdSer.sendHttpReq()
                     memberId               = qmIdSer.getMemberIdFromRsp(response=rsp)
                     self.inputdata["memberId"] = memberId
                     SteamTestCase.memberIdDict[inputData["phoneNo"]] = (token,memberId)
        else:
             token                    = UserLoginService.getTokenData()
             self.inputdata["token"] = token
        return inputData

    def initWeixinData(self):
        inputData = self.getInputData()
        if "phoneNo" in inputData:
            if inputData["phoneNo"] in SteamTestCase.memberIdDict :
               inputData["token"]    = SteamTestCase.memberIdDict[inputData["phoneNo"]][0]
               inputData["memberId"] = SteamTestCase.memberIdDict[inputData["phoneNo"]][1]
            else:
               inputData["scenes"] = "OTP"
               userVerCodeSer = WeixinUserVerfiyCodeService(kwargs = inputData)
               sedCodeRsp     = userVerCodeSer.sendUserVerifyCode()
               retcode        = userVerCodeSer.getRetcodeByRsp(response = sedCodeRsp)
               if retcode == "000000":
                  verfiyCode               = userVerCodeSer.getVerfiyCodeFromRedisByPhone(phoneNum=inputData["phoneNo"])
                  inputData["verfiyCode"] = verfiyCode
                  userLoginSer             = WeixinUserLoginService(kwargs=inputData)
                  rsp  = userLoginSer.weixinUserLogin()
                  code = userLoginSer.getRetcodeByUserLoginRsp(response=rsp)
                  # code = userLoginSer.getRetcodeByRsp()
                  if code  == "000000":
                     token = userLoginSer.getTokenFromRsp(response=rsp)
                     self.inputdata["token"] = token
                     qmIdSer = QueryMemberIdService(kwargs=inputData)
                     # rsp     = qmIdSer.userMemberIdReq()
                     rsp = qmIdSer.sendHttpReq()
                     memberId               = qmIdSer.getMemberIdFromRsp(response=rsp)
                     self.inputdata["memberId"] = memberId
                     SteamTestCase.memberIdDict[inputData["phoneNo"]] = (token,memberId)


    def initAdminData(self):
        token = UserLoginService.getTokenData()
        self.inputdata["token"] = token


if __name__ == "__main__":
    args = {
                "phoneNo":"18916899938"
           }
    # testcase = SteamTestCase(args = )
    print(dir(SteamTestCase))


