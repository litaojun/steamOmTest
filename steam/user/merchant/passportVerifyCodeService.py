from opg.util.redisUtil import RedisOper
from steam.util.httpUopService import  HttpUopService
from opg.bak.uopService import decorator
class PassportVerifyCodeService(HttpUopService):
    '''
        商户获取登录验证码
    '''
    __interfaceName__ = "/merchant/passport/verifyCode"
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(PassportVerifyCodeService, self).__init__(module       = "",
												        filename     = "",
												        sqlvaluedict = kwargs )

    @decorator(["setupGetSendVercode"])
    def sendVerCode(self):
        self.rsp = self.sendHttpReq()
        verfCode = self.getVerfiyCodeFromRedisByPhone()
        self.inputKV["verfiyCode"],self.inputKV["code"] = verfCode,verfCode

    def getVerfiyCodeFromRedisByPhone(self,phoneNum = "",scenes = "MER"):
        if phoneNum is None or phoneNum == "":
           phoneNum = self.inputKV["phoneNo"]
        if scenes is None or scenes == "":
           scenes = self.inputKV["scenes"]
        curRedis   = RedisOper()
        verfiyCode = curRedis.getSteamVerCodeByPhone(phone  = phoneNum,
                                                     scenes = scenes)
        return verfiyCode