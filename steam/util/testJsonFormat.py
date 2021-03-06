import os
from opg.util.schemajson import loadJsonFile, Validator
from steam.util.reqFormatPath import fxt, homePositionRspFmt

def loadjson(filepath=""):
    file = os.getcwd() + filepath
    activitiesInfoScma = loadJsonFile(file)
    return activitiesInfoScma


def compare(a, b):
    jsona = loadjson(filepath=a)
    jsonb = loadjson(filepath=b)
    validator = Validator(jsona)
    validator.validate(jsonb)


def initInput(services=[],
              curser=None):
    def _call(fun):
        def __call(*args, **kwargs):
            fun(*args, **kwargs)
            sf = args[0]
            print("interface=%s,ClassName = %s" %
                  (sf.__interfaceName__, sf.__class__.__name__))
            for ser in services:
                ser(kwargs=sf.inputdata).setInPutData()
            sf.myservice = curser(kwargs=sf.inputdata)
            sf.setService(sf.myservice)
        return __call
    return _call


def initInputService(services=[],curser=None,sign="weixin"):
    """
        :param services:
        :param curser:
        :param sign: 微信用户端："weixin" ，管理平台：admin , 核销小程序：merchant
        :return:
    """
    def _call(fun):
        def __call(*args, **kwargs):
            fun(*args, **kwargs)
            sf = args[0]
            # if sign == "weixin":
            #     sf.initAdminData()
            #     sf.initWeixinData()
            # elif sign == "admin":
            #     sf.initAdminData()
            # elif sign == "merchant":
            #     sf.initAdminData()
            #     sf.initWeixinData()
            #     sf.initMerchantData()
            print("interface=%s,ClassName = %s" %
                  (sf.__class__.__interfaceName__, sf.__class__.__name__))
            # 设置service __interfaceName__ 为对应URL标识
            setattr(
                curser,
                "__interfaceName__",
                sf.__class__.__interfaceName__)
            sf.myservice = curser(kwargs=sf.inputdata)
            sf.myservice.initInterfaceData()
            sf.myservice.initCompareResultFunData()
            for ser in services:
                if isinstance(ser, list):
                    opser = ser[0](kwargs=sf.inputdata)
                    opser.initInterfaceData(ser[1])
                else:
                    opser = ser(kwargs=sf.inputdata)
                    opser.initInterfaceData()
                sf.myservice.ifacedict.update(opser.ifacedict)
        return __call
    return _call


def initAdminInputService(services=[],
                          curser=None):
    def _call(fun):
        def __call(*args, **kwargs):
            fun(*args, **kwargs)
            sf = args[0]
            # sf.initAdminData()
            print("interface=%s,ClassName = %s" %
                  (sf.__class__.__interfaceName__, sf.__class__.__name__))
            # 设置service __interfaceName__ 为对应URL标识
            setattr(
                curser,
                "__interfaceName__",
                sf.__class__.__interfaceName__)
            sf.myservice = curser(kwargs=sf.inputdata)
            sf.myservice.initInterfaceData()
            sf.myservice.initCompareResultFunData()
            for ser in services:
                if isinstance(ser, list):
                    opser = ser[0](kwargs=sf.inputdata)
                    opser.initInterfaceData(ser[1])
                else:
                    opser = ser(kwargs=sf.inputdata)
                    opser.initInterfaceData()
                sf.myservice.ifacedict.update(opser.ifacedict)

        return __call

    return _call


if __name__ == "__main__":
    t = fxt.join(["", "steam", "home", "jsonfmt", "homePositionRsp.json"])
    compare(a=homePositionRspFmt, b=t)
