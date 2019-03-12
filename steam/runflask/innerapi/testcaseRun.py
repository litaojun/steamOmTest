from opg.unit.loader import genTestCaseByInterfaceOrCaseIds
from steam.runflask.util.initData import casepath
from steam.runflask.util import initData
from opg.bak.loadTestcase import runTestOneCls
def runOneTestCase(interfaceName):
    testSuite     = genTestCaseByInterfaceOrCaseIds( allTestClass  = initData.allTestClass ,
                                                     allCase       = initData.allTestCase  ,
                                                     interfaceName = interfaceName,
                                                     caseIds       = None )
    runTestOneCls(testSuite,casepath)