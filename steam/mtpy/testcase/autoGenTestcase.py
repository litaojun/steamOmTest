from steam.mockhttp.flaskHttpServer import httpData
from steam.util.configIni import basePath
from opg.util.yamlOper import readYmlFile,dumpDataToYmlFile
import os
def loadCaseTmpFile():
    filepath = os.sep.join([basePath,"template","testcaseMitmproxy.template"])
    caseTmpData = readYmlFile(filePath=filepath)
    return caseTmpData

def getCaseTmpFilepath():
    filepath = os.sep.join([basePath,"template","testcaseMitmproxy.template"])
    return filepath

def getTestcasePath(usertype,modul):
    filePath = os.sep.join([basePath,"mitmproxy","steam",usertype,modul])
    return filePath

def genAutoCase(method=None,host=None,url=None,path=None,reqbody=None):
    usertype,modul = httpData[path][5],httpData[path][3]
    caseTmpDataDict = loadCaseTmpFile()
    

