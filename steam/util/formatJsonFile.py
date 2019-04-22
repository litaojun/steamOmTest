from steam.util.fileGenerator import baseDictTranDataDict
import json
import os
from opg.util.httptools import httpPost,httpGet

def loadJsonFromFile(filePath=""):
    if filePath  is not None and os.path.exists(filePath):
        with open(filePath) as f:
            try:
              jsonData = json.load(f)
            except Exception as e:
              print(e)
              raise e
            return jsonData

# 读json文件，并格式化indent=3后写入
def formatJsFile(filePath=""):
    if os.path.exists(filePath):
        jsonDict = loadJsonFromFile(filePath)
        json.dump(
            obj=jsonDict,
            fp=open(
                filePath,
                "w",
                encoding="utf-8"),
            indent=3,
            ensure_ascii=False)

# post请求响应数据，get响应数据，读取指定行数据并格式化indent=3写入
def readSpdLineAndFormatJsWtr(filePath="", lineNum=-2, dealFun=None):
    if os.path.exists(filePath):
        with open(filePath, "r", encoding="utf-8") as f:
            alllines = f.readlines()
            while "\n" in alllines:
                alllines.remove("\n")
            jsonStr = alllines[lineNum]
            print(jsonStr)
        dealFun(filePath=filePath, jsonStr=jsonStr)

# 获取http地址？后部分并写入文件
def writeUrlLowDataToFile(filePath="", jsonStr=""):
    """
        :param filePath: 文件路径
        :param jsonStr:  http get请求url地址全称
        :return:
    """
    if jsonStr is not None and jsonStr != "":
        httpUrlStr = jsonStr.split()[1]
        if httpUrlStr is not None and httpUrlStr != "":
            if httpUrlStr.find("?") > 0:
                wtrData = "?" + httpUrlStr.split("?")[1]
            else:
                wtrData = ""
            with open(filePath, "w") as f:
                f.write(wtrData)


# 格式化字符串为indent=3格式并写入json文件
def writeStrToJsonFile(filePath="", jsonStr=None,rwmode = "w"):
    retCode = "jsonfmt100001"
    jsonDict = fmtStrToJson(jsonStr)
    if jsonDict is None:
        return retCode
    try:
        json.dump(
            obj=jsonDict,
            fp=open(
                filePath,
                rwmode,
                encoding="utf-8"),
            indent=3,
            ensure_ascii=False)
        retCode = "jsonfmt000000"
    except Exception as ex:
        print(ex)
        retCode = "jsonfmt100002"
    finally:
        return retCode


def fmtStrToJson(jsonStr=None):
    if jsonStr is not None and type(jsonStr) != dict:
        try:
            jsonDict = json.loads(jsonStr, encoding="utf-8")
            retCode = "jsonfmt000000"
        except Exception as ex:
            print(ex)
            jsonDict = None
            retCode = "jsonfmt100001"
        return jsonDict
    elif type(jsonStr) == dict:
         return jsonStr

def formatAllFile(bsDict={}):
    baseDictTranDataDict(bsDict)
    formatReqJsonFile = bsDict["formatReqJsonFile"]
    formatRspJsonFile = bsDict["formatRspJsonFile"]
    if bsDict["method"] == "post":
        readSpdLineAndFormatJsWtr(filePath=formatReqJsonFile,
                                  lineNum=-1,
                                  dealFun=writeStrToJsonFile)
    elif bsDict["method"] == "get":
        readSpdLineAndFormatJsWtr(filePath=formatReqJsonFile,
                                  lineNum=0,
                                  dealFun=writeUrlLowDataToFile)
    readSpdLineAndFormatJsWtr(filePath=formatRspJsonFile,
                              lineNum=-2,
                              dealFun=writeStrToJsonFile)

def writeHttpReqRspDataToFile(bsDict = None,reqHeaderData = {},reqBodyData = {},httpUrl = ""):
    baseDictTranDataDict(bsDict)
    method  = bsDict["method"]
    url = bsDict["url"]
    formatReqJsonFile = bsDict["formatReqJsonFile"]
    formatRspJsonFile = bsDict["formatRspJsonFile"]
    # os.mknod(formatReqJsonFile)
    # os.mknod(formatRspJsonFile)
    if method == "post":
       rsp = httpPost(url=httpUrl,headers=reqHeaderData,reqJsonData=reqBodyData)
       writeStrToJsonFile(filePath=formatReqJsonFile,jsonStr=reqBodyData,rwmode="a+")
       writeStrToJsonFile(filePath=formatRspJsonFile,jsonStr=rsp,rwmode="a+")
    elif method == "get":
        writeUrlLowDataToFile(filePath=formatReqJsonFile,jsonStr="top " + httpUrl)
        rsp = httpGet(url=httpUrl,headers=reqHeaderData)
        writeStrToJsonFile(filePath=formatRspJsonFile, jsonStr=rsp , rwmode="a+")


if __name__ == "__main__":
    bsDict = {
                    "oneDir": "admin",
                    "twoDir": "media",
                    "pathSign": "/operation-manage/material/audit"
                }
    # formatAllFile(bsDict=bsDict)
    httpReqUrl = "https://uat-steam-api.opg.cn/operation-manage/material/audit"
    httpHeader = {
                    "login_type":"CMS",
                    "token":"5a33f2eda53749e9bb542308b4f81e8f"
                    #"memberId":"68a30b8e-7dc2-46f5-89c4-c0894c0c3e68"
                  }
    httpReqBody = { "pass": True , "auditReason": None , "id": 354 }
    writeHttpReqRspDataToFile(bsDict=bsDict,
                              reqHeaderData=httpHeader,
                              reqBodyData=httpReqBody,
                              httpUrl=httpReqUrl)