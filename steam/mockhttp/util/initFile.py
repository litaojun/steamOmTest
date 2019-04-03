import os
import yaml
import collections
from steam.util.configIni import basePath,cf
urldata = collections.defaultdict(lambda :{})
def loadFileData():
    filePath = os.sep.join([basePath  , "testjson-url.yml"])
    return loadYamlFileData(filePath = filePath)

def loadYamlFileData(filePath = None):
    print("filepath = %s " % filePath)
    with open(filePath, 'r',encoding="utf-8") as f:
         ymldata = yaml.load(f.read())
         # print("ymldata = %s " % ymldata)
         return ymldata

def generateUrlToFilePath():
    ymldata  = loadFileData()
    for urltype in ymldata["steam"]:
        data = traverseFileData(ymldata, urltype)
        for url in data:
            urldata[url] = data[url]
    return  urldata

def traverseFileData(ymldata,dir):
    filedata = ymldata["steam"][dir]
    rtdata = collections.defaultdict(lambda :{})
    bsdir = [basePath,"steam",dir]
    for curdir in filedata:
        for pathurl  in  filedata[curdir]:
            data     = filedata[curdir][pathurl]
            method   = data["method"]
            url      = data["url"]
            modul    = data["modul"]
            title    = data["title"]
            # format  = data["formatone"]
            # tempdir = dir + [curdir,format]
            pathdict  = {}
            for key in data:
                if key not in ( "method","url","title","modul"):
                   pathdict[key] = [os.sep.join(bsdir + [curdir, filename]) for filename in data[key]]  #key对应formatone和其它格式
            rtdata[pathurl] = [method, pathdict,url,modul,title,dir]
    return rtdata

def generateDelayTimeConfig():
    return cf["delay"]["time"]

if __name__ == "__main__":
   filePath = "D:\litaojun\steamyml\matchAppleTestCase.yml"
   ymldata = loadYamlFileData(filePath = filePath)
   print(ymldata)
   tdict = collections.defaultdict(lambda :{})
   for infsTestcases in ymldata["testcases"]:
       interfaceName = infsTestcases["interfaceName"]
       tdict[interfaceName] = collections.defaultdict(lambda :[])
       for case in infsTestcases["case"]:
           preConditions  = case.get("preConditions","")
           operationSteps = case["operationSteps"]
           testData       = case["testData"]
           expectedResult = case["expectedResult"]
           for data in case["testData"]:
               testPoint = data["testPoint"]
               caseid    = data["caseid"]
               tdict[interfaceName][operationSteps].append([caseid,interfaceName,testPoint,preConditions,operationSteps,data,expectedResult])
   print(tdict)
   print("fsdfyml".endswith(".yml"))



