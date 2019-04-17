from steam.mockhttp.flaskHttpServer import httpData
from steam.util.configIni import basePath
from opg.util.yamlOper import readYmlFile,dumpDataToYmlFile
import os
from mitmproxy import ctx

#获取用例模板
def loadCaseTmpFile():
    filepath = os.sep.join([basePath,"template","testcaseMitmproxy.yml"])
    caseTmpData = readYmlFile(filePath=filepath)
    ctx.log.info("loadCaseTmpFile - caseTmpData=%s" % caseTmpData)
    return caseTmpData

def dumpYmalCaseToFile(path,usertype,modul,testcase):
    filePath = getTestcasePath(usertype=usertype,modul=modul,path=path)
    dumpDataToYmlFile(filePath=filePath,data=testcase)


def getTestcasePath(usertype,modul,path):
    fileName = "".join([ name.capitalize() if index>0 else name for index,name in enumerate(path.split("/"))])
    filePath = os.sep.join([basePath,"mitmproxy","steam",usertype,modul,fileName])
    print("filePath = %s" % filePath)
    return filePath

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
    usertype,modul,title = httpData[path][5],httpData[path][3],httpData[path][4]
    caseTmpDataDict = loadCaseTmpFile()
    caseTmpDataDict["testcases"][0]["interfaceName"] = path
    caseTmpDataDict["testcases"][0]["case"][0]["testPoint"] = title
    ctx.log.info("reqbody=%s,type=%s" % (reqbody,type(reqbody)))
    testData.update(reqbody)
    ctx.log.info("testData=%s" % testData)
    caseTmpDataDict["testcases"][0]["case"][0]["testData"] = [ testData.update(reqbody) ]
    filePath = getTestcasePath(usertype=usertype,modul=modul,path=path)
    ctx.log.info("filePat=%s,caseData=%s" %(filePath,caseTmpDataDict))
    dumpDataToYmlFile(filePath=filePath,data=caseTmpDataDict)

if __name__ == "__main__":
    testData = {
                 "caseid":"activity_alert_1",
                 "testPoint":"修改活动正常",
                 "reqjsonfile":"formatone"
               }
    reqbody = {"phoneNo": "18916899938"}
    testData.update(reqbody)
    print(testData)
    

