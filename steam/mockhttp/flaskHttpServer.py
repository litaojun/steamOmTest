#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: flaskHttpServer.py 
@time: 2018/11/7 11:25 
"""
import time
from flask import Flask, jsonify,request
from steam.mockhttp.util.initFile import generateDelayTimeConfig,generateUrlToFilePath
from opg.util.uopService import loadStrFromFile
from werkzeug.routing import BaseConverter

httpData  = generateUrlToFilePath()
delayData = generateDelayTimeConfig()
print("httpdata = %s" % httpData)
print("delayData = %s" % delayData)
app = Flask(__name__,template_folder='templates',static_url_path='/static/')

class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]
app.url_map.converters['regex'] = RegexConverter
def postprocessor():
    """
    http请求后置处理器
    :return:
    """
    def __callFun__(fun):
        def __delayTime__(**kargs):
            rtjsData = fun(**kargs)
            if delayData["sign"]:
               time.sleep(delayData["time"])
            return rtjsData
        return __delayTime__
    return __callFun__

@app.route('/<regex(".*"):url>', methods=['GET','POST','PUT','DELETE'])
@postprocessor()
def mockHttpService(url):
    """
        处理所有请求
        :param url:
        :return:
    """
    httpMethod = request.method.lower()
    httpPath   = request.path
    rspjsonPath= httpData[httpMethod].get(httpPath)
    if rspjsonPath is None:
       return("rsp data is not exist")
    print("http request method is %s ,http request path is %s" % (httpMethod,httpPath))
    if request.method  == "POST":
       reqJsonData = request.data.decode('utf-8')
       print("http req data is %s" % reqJsonData)
    else:
        if request.method == "GET":
           httpReqData = request.args
           print("http req data is %s" % httpReqData)
    return loadStrFromFile(filepath=rspjsonPath)
    # return render_template("pytestlocal.html", content="hello flask ")



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8282)
    #testResult = runTest(title=u"steam亲子教育", description=u"用例测试情况",token="ssssss")