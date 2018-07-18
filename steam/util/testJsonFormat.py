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
import  os ,json
from opg.util.schemajson import loadJsonFile,Validator
from jsonschema import Draft4Validator
from functools import wraps
from jsonschema import FormatChecker
from jsonschema import ValidationError
from steam.util.reqFormatPath import homeConfigQueryRspFmt,fxt,homePositionRspFmt
def loadjson(filepath = ""):
    file = os.getcwd() + filepath
    activitiesInfoScma = loadJsonFile(file)
    return activitiesInfoScma

def compare(a,b):
    jsona = loadjson(filepath=a)
    jsonb = loadjson(filepath=b)
    validator = Validator(jsona)
    validator.validate(jsonb)

def initInput(services=[],curser=None):
    def _call(fun):
        def __call(*args,**kwargs):
            fun(*args, **kwargs)
            sf = args[0]
            for ser in services:
                ser(kwargs=sf.inputdata).setInPutData()
            sf.myservice = curser(kwargs = sf.inputdata)
            sf.setService(sf.myservice)
        return __call
    return _call

if __name__ == "__main__":
    t = fxt.join(["","steam","home","jsonfmt","homePositionRsp.json"])
    compare(a = homePositionRspFmt,b = t)