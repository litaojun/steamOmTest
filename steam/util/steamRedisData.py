from opg.util.redisUtil import RedisOper
from steam.util.configIni import redisCf
ip = redisCf.get("uat","ip")
port = redisCf.get("uat","port")
steamRedis = RedisOper(ip,port)
#从redis中获取CMS登录的验证码
def getVerifyCodeByUserType(userType="",phoneNum=""):
    """eBy
    :param userType:
            admin  CMS登录 STEAM_PERMISSION:SMS_CODE_INFO:18916899938_819195;
            weixin 微信用户登录 PASSPORT_VERIFY_CODE:OTP:18916899938_000000；
            merchants  核销商户登录小程序 steam-merchant:SMS:18916899938_572842  steam-merchant:SMS:18916899938_COUNT
            weixinReg  微信用户注册
    :param phoneNum  手机号码
    :return:
    """
    data = (phoneNum,"*")
    d = { "admin":"STEAM_PERMISSION:SMS_CODE_INFO:%s_%s" % data,
          "weixin":"PASSPORT_VERIFY_CODE:OTP:%s_%s" % data,
          "merchants":"steam-merchant:SMS:%s_%s" % data ,
          "weixinReg":"PASSPORT_VERIFY_CODE:MLN:%s%s" }
    keyls = RedisOper.curRedis.keys(d[userType])
    code = b'ss'
    if len(keyls) > 0:
        key = keyls[0]
        code = key[-6:]
        print(type(code))
    return str(code, encoding="utf-8")

