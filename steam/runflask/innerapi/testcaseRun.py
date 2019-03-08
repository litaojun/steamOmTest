import threading
from opg.unit.flaskRunMgr import genTestCaseByInterfaceOrCaseIds,runOneTestcase
from steam.runflask.util.initData import testSuite,genAllTestCase,casepath
from steam.runflask.util import initData
from flask import Blueprint
from steam.runflask.dao.queryDbRunTestcase import queryTokenByPlanId
from opg.unit.flaskRunMgr import getRunTestTokenId
from opg.unit.loadTestcase import runAllTestCase
from opg.unit.flaskRunMgr import queryStateByTokenPro
from opg.unit.loadTestcase import runTestOneCls
def runOneTestCase(interfaceName):
    testSuite     = genTestCaseByInterfaceOrCaseIds( allTestClass  = initData.allTestClass ,
                                                     allCase       = initData.allTestCase  ,
                                                     interfaceName = interfaceName,
                                                     caseIds       = None )
    runTestOneCls(testSuite,casepath)