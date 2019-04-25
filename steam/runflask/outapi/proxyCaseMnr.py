from steam.mockhttp.flaskHttpServer import httpData
from steam.util.configIni import basePath, casepath
import os
import glob
from flask import Blueprint
from flask import send_from_directory, request,jsonify
bapp = Blueprint('proxy', __name__)


def genCaseOrFmtPath(oneDir, twoDir):
    return os.sep.join([basePath, "mitmproxy", "steamcase", oneDir, twoDir]), \
        os.sep.join([basePath, "mitmproxy", "steam", oneDir, twoDir])


def genFilePrefixByUrlSuf(urlSuffix):
    return "".join([name if index == 0 else name.capitalize()
                    for index, name in enumerate(urlSuffix.split("/")[-2:])])


@bapp.route("/prop/caselist", methods=['GET'])
def getInterfaceProxyTscase():
    interfaceProxyTscase = []
    for urlSign in httpData:
        caseData = {}
        data = httpData[urlSign]
        oneDir, twoDir, url, urlSuffix, fileEnd = data[5], data[7],\
            data[2], data[2][28:],\
            data[8]
        caseData["interfaceName"]= url
        filePrefix = genFilePrefixByUrlSuf(urlSuffix=urlSuffix)
        casePath, fmtPath = genCaseOrFmtPath(oneDir, twoDir)
        data = []
        fmtReqPath = fmtPath + os.sep + filePrefix + "Req.json"
        fmtRspPath = fmtPath + os.sep + filePrefix + "Rsp.json"
        if fileEnd is None:
            filePathName = casePath + os.sep + filePrefix + "s.yml"
            data.append({"title": None,
                         "casePath": filePathName,
                         "interfacename": urlSuffix,
                         "fmtReqPath": fmtReqPath,
                         "fmtRspPath": fmtRspPath,
                         "localName": filePrefix + "s.yml"})
        else:
            filePathName = casePath + os.sep + filePrefix + "*" #+ "*s.yml"
            data = genTitleFilepathDict(
                filePathName, urlSuffix, fmtReqPath, fmtRspPath)
            print("data=%s" % data)
        caseData["result"] = data
        interfaceProxyTscase.append(caseData)
    return jsonify({"code": "000000", "caseDataList": interfaceProxyTscase})


def genTitleFilepathDict(filePathName, urlSuffix, fmtReqPath, fmtRspPath):
    print("filePathName=%s,urlSuffix=%s,fmtReqPath=%s,fmtRspPath=%s" % (filePathName,urlSuffix,fmtReqPath,fmtRspPath))
    fileList = glob.glob(pathname=filePathName)
    print("fileList=%s" % fileList )
    data = []
    for filePath in fileList:
        fileName = os.path.basename(filePath)
        title = fileName.split("-")[1][0:-4]
        print("fileName=%s ,title=%s" %(fileName,title))
        data.append({"title": title,
                     "casePath": filePath,
                     "interfacename": urlSuffix,
                     "fmtReqPath": fmtReqPath,
                     "fmtRspPath": fmtRspPath,
                     "localName": fileName })
    return data


@bapp.route("/prop/downfile", methods=['POST'])
def downFile():
    filePathName = request.args.get("filePath")
    fileName, filePath = os.path.dirname(
        filePathName), os.path.basename(filePathName)
    send_from_directory(filePath, fileName)


def downFmtFile():
    pass
