from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.user.merchant.passportVerifyCodeService import PassportVerifyCodeService

class PassportVerifyCodeTest(SteamTestCase):
      """
            商户获取登录验证码
      """
      __interfaceName__ = "/merchant/passport/verifyCode"
      @initInputService( services=[ ],
                         curser=PassportVerifyCodeService ,
                         sign="merchant")
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(PassportVerifyCodeTest,self).__init__(methodName,param)

if __name__ == "__main__":
    # runTestOneCls(
    #                 casefilepath = "\\steamcase\\user\\merchant\\merchantPassportVerifyCodes.yml",
    #                 testclse     = PassportVerifyCodeTest,
    #                 basepath     = "D:\\litaojun\\steamyml"
    #              )
    def a(sign):
        t = {}
        def b(a,b):
            if a not in t:
                t[a] = (sign,b)
            else:
                print(t)
        return b
    f = a("aaa")
    f("fff","cccc")
    f("fff1", "cccc1")
    f("fff2", "cccc2")
    f("fff3", "cccc3")
    f("fff", "ccccff")