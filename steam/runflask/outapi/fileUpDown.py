from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import os
from flask import Blueprint
from opg.util.dbtools import  Database
bapp = Blueprint('downfile', __name__)
@bapp.route('/interface/log', methods=['GET'])
def query_planlist():
    print("query_planlist")
    # from steam.runflask.outapi.testcaseRun import logDir
    interfacename = request.args.get("interfacename")
    planId = request.args.get("planId")
    startFmtName = interfacename[29:-2].replace("/","-")
    queryLogdirSql = "select logdir from test_plan t where t.id = '%s'" % planId
    print(queryLogdirSql)
    dbManager = Database()
    idrst   = dbManager.queryAll(sql=queryLogdirSql, dbName="ltjtest")
    print(idrst)
    logtime = idrst[0][0]
    logDir = os.sep.join([os.getcwd(),"Logs",str(logtime)])
    print("interfacename=%s,planId=%s,startFmtName=%s,logDir=%s" %
          (interfacename,planId,startFmtName,logDir))
    fileDir,filename = filterFileByName(fileDir=logDir,fileNameFmt=startFmtName)
    print("fileDir=%s,filename=%s" % (fileDir,filename))
    return send_from_directory( fileDir ,
                                filename ,
                                as_attachment = True )

def filterFileByName(fileDir = "" ,fileNameFmt = ""):
    if os.path.exists(fileDir):
       for file in os.listdir(fileDir):
           if file.startswith(fileNameFmt):
              return fileDir,file
    return os.getcwd() + os.sep + "upload"  ,  "aaa.log"