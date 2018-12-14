#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: testJsonFormat.py 
@time: 2018/6/6 16:29 
"""
import  os
from opg.util.schemajson import loadJsonFile,Validator
from steam.util.reqFormatPath import fxt,homePositionRspFmt
def loadjson(filepath = ""):
    file = os.getcwd() + filepath
    activitiesInfoScma = loadJsonFile(file)
    return activitiesInfoScma

def compare(a,b):
    jsona = loadjson(filepath=a)
    jsonb = loadjson(filepath=b)
    validator = Validator(jsona)
    validator.validate(jsonb)

def initInput(services = [],
              curser   = None):
    def _call(fun):
        def __call(*args,**kwargs):
            fun(*args, **kwargs)
            sf = args[0]
            print("interface=%s,ClassName = %s" % (sf.__interfaceName__,sf.__class__.__name__))
            for ser in services:
                ser(kwargs = sf.inputdata).setInPutData()
            sf.myservice = curser(kwargs = sf.inputdata)
            sf.setService(sf.myservice)
        return __call
    return _call

def initInputService(services = [],
                     curser   = None):
    def _call(fun):
        def __call(*args,**kwargs):
            fun(*args, **kwargs)
            sf = args[0]
            print("interface=%s,ClassName = %s" % (sf.__class__.__interfaceName__,sf.__class__.__name__))
            #设置service __interfaceName__ 为对应URL标识
            setattr(curser,"__interfaceName__",sf.__class__.__interfaceName__)
            sf.myservice = curser(kwargs = sf.inputdata)
            sf.myservice.initInterfaceData()
            sf.myservice.initCompareResultFunData()
            # sf.setService(sf.myservice)
            for ser in services:
                if isinstance(ser,list):
                   opser = ser[0](kwargs = sf.inputdata)
                   opser.initInterfaceData(ser[1])
                else:
                   opser = ser(kwargs = sf.inputdata)
                   opser.initInterfaceData()
                # {}.update()
                sf.myservice.ifacedict.update(opser.ifacedict)
                # for name in opser.ifacedict:
                #     sf.myservice.ifacedict[name] = opser.ifacedict[name]
        return __call
    return _call

if __name__ == "__main__":
    t = fxt.join(["","steam","home","jsonfmt","homePositionRsp.json"])
    compare(a = homePositionRspFmt , b = t)