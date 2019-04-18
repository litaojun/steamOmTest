from steam.mockhttp.flaskHttpServer import httpData
from steam.util.configIni import basePath
from opg.util.yamlOper import readYmlFile,dumpDataToYmlFile
from steam.util.formatJsonFile import writeStrToJsonFile
import os

from mitmproxy import ctx

#获取用例模板
def loadCaseTmpFile():
    filepath = os.sep.join([basePath,"template","testcaseMitmproxy.yml"])
    caseTmpData = readYmlFile(filePath=filepath)
    ctx.log.info("loadCaseTmpFile - caseTmpData=%s" % caseTmpData)
    return caseTmpData

#写yaml测试用例到文件
def dumpYmalCaseToFile(path,usertype,modul,testcase):
    filePath = getTestcasePath(usertype=usertype,modul=modul,path=path)
    dumpDataToYmlFile(filePath=filePath,data=testcase)

#获取测试用例的路径OR请求响应数据格式路径
def getTestcasePath(usertype,modul,path,dirType="steamcase",fileType="s.yml"):
    """
    :param usertype: 用户类型，一级目录，admin,weixin,merchants
    :param modul: 二级目录，模块级别，与testjson-url.yml配置一致
    :param path:  请求URL标识
    :param dirType: steamcase:测试用例目录， steam:请求响应数据目录
    :return:
    """
    fileName = "".join([ name.capitalize() if index>1 else name for index,name in enumerate(path.split("/"))]) + fileType
    filePath = os.sep.join([basePath,"mitmproxy",dirType,usertype,modul,fileName])
    print("filePath = %s" % filePath)
    return filePath

#生成自动化测试用例
def genAutoCase(method=None,host=None,url=None,path=None,reqbody=None):
    ctx.log.info("genAutoCase,path=%s" % path)
    if path not in httpData:
        print("path=%s is not exist in testjson-url.yml" % path)
        return
    testData = {
                 "caseid":"activity_alert_1",
                 "testPoint":"修改活动正常",
                 "reqjsonfile":"formatone"
               }
    usertype,modul,title = httpData[path][5],httpData[path][7],httpData[path][4]
    caseTmpDataDict = loadCaseTmpFile()
    caseTmpDataDict["testcases"][0]["interfaceName"] = path
    caseTmpDataDict["testcases"][0]["case"][0]["testPoint"] = title
    ctx.log.info("reqbody=%s,type=%s" % (reqbody,type(reqbody)))
    testData.update(reqbody)
    ctx.log.info("testData=%s" % testData)
    caseTmpDataDict["testcases"][0]["case"][0]["testData"] = [ testData ]
    filePath = getTestcasePath(usertype=usertype,modul=modul,path=path)
    ctx.log.info("filePat=%s,caseData=%s" %(filePath,caseTmpDataDict))
    dumpDataToYmlFile(filePath=filePath,data=caseTmpDataDict)

#生成请求数据
def genReqData(method=None,host=None,url=None,path=None,bodydata=None,bodyType="request"):
    if bodyType == "request":
        jsonFileType = "Req.json"
        ymlFileType  = "Req.yml"
    elif bodyType == "response":
        jsonFileType = "Rsp.json"
        ymlFileType  = "Rsp.yml"
    else:
        return
    ctx.log.info("genReqData,path=%s" % path)
    if path not in httpData:
        print("path=%s is not exist in testjson-url.yml" % path)
        return
    usertype, modul, title = httpData[path][5], httpData[path][7], httpData[path][4]
    reqFilePath = getTestcasePath(usertype=usertype,modul=modul,path=path,dirType="steam",fileType=jsonFileType)
    writeStrToJsonFile(filePath=reqFilePath,jsonStr=bodydata,rwmode="a+")
    reqFilePath = getTestcasePath(usertype=usertype, modul=modul, path=path, dirType="steam", fileType=ymlFileType)
    dumpDataToYmlFile(filePath=reqFilePath,data=bodydata)



if __name__ == "__main__":
    testData = {
                 "caseid":"activity_alert_1",
                 "testPoint":"修改活动正常",
                 "reqjsonfile":"formatone"
               }
    reqbody = {"phoneNo": "18916899938"}
    testData.update(reqbody)
    print(testData)
    

