from opg.unit.loader import genTestCaseByInterfaceOrCaseIds
from steam.runflask.util.initData import casepath
from steam.runflask.util import initData
# from opg.bak.loadTestcase import runTestOneCls
from steam.runflask.outapi.testcaseRun import runTestOneCls,runOneTestClass
from opg.bak.flaskRunMgr import getRunTestTokenId
from opg.unit.runtest import genDir, writeLog
from opg.unit.runtest import runOneCls
from opg.util.timeTool import getNowTime,getTwoFmtTime
def runOneTestCase(interfaceName):
    starttime,longtime = getTwoFmtTime()
    global writeDir
    logDir = genDir(str(longtime))
    writeDir = writeLog(wtrDir=logDir)
    testSuite     = genTestCaseByInterfaceOrCaseIds( allTestClass  = initData.allTestClass ,
                                                     allCase       = initData.allTestCase  ,
                                                     interfaceName = interfaceName,
                                                     caseIds       = None )
    runOneCls(testSuite,casepath)