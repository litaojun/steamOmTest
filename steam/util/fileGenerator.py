#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: fileGenerator.py 
@time: 2018/12/10 12:55 
"""
from steam.mockhttp.util.initFile import loadFileData
from string import Template
def generateFile( filePath = None,templateTypePath = "",dataDict= {} ):
    # tableName = 'students'
    # className = '%sRedisDao' %  tableName.capitalize()
    # filePath = r'include/%s.cpp' % className
    class_file = open(filePath,'w',encoding="utf-8")
    lines = []
    #模版文件
    template_file = open(templateTypePath,'r',encoding="utf-8")
    tmpl = Template(template_file.read())
    #模版替换
    lines.append(tmpl.substitute(dataDict))
    # 0.将生成的代码写入文件
    class_file.writelines(lines)
    class_file.close()
    print('generate %s over. ~ ~' % filePath)
def genServiceFile():
    templateTypePath = "D:\\litaojun\\steamyml\\template\\service.template"
    filePath         = "D:\\litaojun\\workspace\\steamOmTest\\steam\\admin\\activity\\orderAdminResourceIdService.py"
    dataDict = {
                 "serviceName":"OrderAdminResourceIdService",
                 "subTitle":"sss"
                }
    generateFile(filePath=filePath,templateTypePath=templateTypePath,dataDict=dataDict)

def pathSignTranCasePathOrClassName(pathSign = "/order-service/order/admin/resourceId"):
    pathArray = pathSign.split("/")
    tmpName   = "".join([name[0].upper() + name[1:] for name in pathArray[2:]])
    casePath  = pathArray[1] + tmpName
    className = tmpName
    pyFileName = tmpName[0].lower() + tmpName[1:]
    return className,casePath,pyFileName

def baseDictTranDataDict(bsDict = None ):
    serviceTemplatePath = "D:\\litaojun\\steamyml\\template\\service.template"
    testTemplatePath    = "D:\\litaojun\\steamyml\\template\\test.template"
    caseTemplatePath    = "D:\\litaojun\\steamyml\\template\\testcase.template"
    testFilePath        = "D:\\litaojun\\workspace\\steamOmTest\\steam\\%(oneDir)s\\%(twoDir)s\\%(pyFileName)sTest.py"
    serviceFilePath     = "D:\\litaojun\\workspace\\steamOmTest\\steam\\%(oneDir)s\\%(twoDir)s\\%(pyFileName)sService.py"
    testcaseFilePath    = "D:\\litaojun\\steamyml\\steamcase\\%(oneDir)s\\%(twoDir)s\\%(casePath)ss.yml"
    ymlData    = loadFileData()
    urlYmldata = ymlData["steam"][bsDict["oneDir"]][bsDict["twoDir"]][bsDict["pathSign"]]
    bsDict["subTitle"]   = urlYmldata["title"]
    casefile              = pathSignTranCasePathOrClassName(pathSign = bsDict["pathSign"])
    bsDict["pyFileName"] = casefile[2]
    bsDict["casePath"]   = casefile[1]
    bsDict["className"]  = casefile[0]
    bsDict["testFilePath"]    = testFilePath  % bsDict
    bsDict["serviceFilePath"] = serviceFilePath % bsDict
    bsDict["testcaseFilePath"]   = testcaseFilePath % bsDict
    bsDict["testTemplatePath"]    = testTemplatePath
    bsDict["serviceTemplatePath"] = serviceTemplatePath
    bsDict["caseTemplatePath"]    = caseTemplatePath

def genAllFile(bsDict = None):
    baseDictTranDataDict(bsDict)
    generateFile( filePath         = bsDict["testcaseFilePath"] ,
                  templateTypePath = bsDict["caseTemplatePath"] ,
                  dataDict         = bsDict )
    generateFile( filePath         = bsDict["serviceFilePath"] ,
                  templateTypePath = bsDict["serviceTemplatePath"] ,
                  dataDict         = bsDict )
    generateFile( filePath         = bsDict["testFilePath"] ,
                  templateTypePath = bsDict["testTemplatePath"] ,
                  dataDict         = bsDict )

if __name__ == "__main__":
    bsDict = {
                "oneDir" :  "admin" ,
                "twoDir" :  "article" ,
                "pathSign" : "/operation-manage/media/resetMediaState"
             }
    genAllFile(bsDict = bsDict)