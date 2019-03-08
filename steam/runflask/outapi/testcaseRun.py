from flask import jsonify,request
import sys
sys.path.append("/home/nicepy/testhome/unittestExBaseb")

import threading
from opg.unit.flaskRunMgr import genTestCaseByInterfaceOrCaseIds,runOneTestcase
from steam.runflask.util.initData import testSuite,genAllTestCase
from steam.runflask.util import initData
from flask import Blueprint
from steam.runflask.dao.queryDbRunTestcase import queryTokenByPlanId
from opg.unit.flaskRunMgr import getRunTestTokenId
from opg.unit.loadTestcase import runAllTestCase
from opg.unit.flaskRunMgr import queryStateByTokenPro
# from steam.runflask.tsdtmgr.testDataMnr import timeCheckData
bapp = Blueprint('tsrun', __name__)
timerSign = False
@bapp.route("/prop/interfacelist", methods=['GET'])
def runOneTestCase():
    """
    执行一个指定的用例
    :return:
    """
    planId        = int(request.args.get("planId"))
    projectName   = request.args.get("projectname")
    caseId        = request.args.get("caseId")
    interfaceName = request.args.get("interfaceName")
    print("planId=%s,projectName=%s,caseId=%s,interfaceName=%s" %(planId,projectName,caseId,interfaceName))
    token         = queryTokenByPlanId(planId      = planId,
                                       projectName = projectName)
    testSuite     = genTestCaseByInterfaceOrCaseIds( allTestClass  = initData.allTestClass ,
                                                     allCase       = initData.allTestCase  ,
                                                     interfaceName = interfaceName,
                                                     caseIds       = [caseId] )
    runOneTestcase(suites      = testSuite,
                   planId      = planId,
                   token       = token,
                   title       = projectName,
                   description = "%s-用例测试情况" % projectName)

    return jsonify({
                        "code" : "000000",
                        "token": token
                   })

@bapp.route('/prop/runTestPro', methods=['GET'])
def start_steam_tasks():
    """
    执行所有用例
    :return:
    """
    projectName = request.args.get("projectname")
    retdata     = getRunTestTokenId(projectname = projectName)
    testSuite   = genAllTestCase(allCase        = initData.allTestCase,
                                 allTestClass   = initData.allTestClass)
    # SteamTestCase.memberIdDict  = {}
    t = threading.Thread(target = runAllTestCase,
                         kwargs = {
                                        "suites" : testSuite,
                                        "title"  : projectName,
                                        "description" : "%s-用例测试情况" % projectName,
                                        "token"        :  retdata[0]
                                  }
                         )
    t.start()
    return jsonify({
                        'sign'  : "000000",
                        "token" : retdata[0],
                        "starttime" : retdata[1]
                   })

@bapp.route('/prop/queryRunProcess', methods=['GET'])
def query_run_state():
    """
    查询用例执行是否完成了
    :return:
    """
    """
        根据token查询用例执行是否完成
        :return:
    """
    token       = request.args.get("token")
    projectName = request.args.get("projectname")
    rtRunDt     = queryStateByTokenPro(projectName = projectName,
                                       token       = token)
    return jsonify(rtRunDt)



if __name__ == "__main__":
    from opg.util.dbtools import Database
    # sqlstr = "delete o.* from tb_order o where o.id = '11111fffffff'"
    sqlstr = """select m.passport_id,m.MEMBER_NAME,m.NICK_NAME from t_member m where m.passport_id = 'd4662b02-b75f-4eda-b796-f7e16d04044d';"""
    db = Database()
    # num = db.deleteData(sql=sqlstr,dbName= "allin")
    rst = db.queryAll(sql=sqlstr,dbName="allin")
    print(rst)
    # print(str(num))





