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

if __name__ == "__main__":
    t = fxt.join(["","steam","home","jsonfmt","homePositionRsp.json"])
    compare(a = homePositionRspFmt,b = t)