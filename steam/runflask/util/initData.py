from opg.unit.loader import initAllTestCase,initAllTestClass,genAllTestCase
from steam.util.configIni import casepath
sign      = True
testSuite = None
if sign :
    allTestClass = initAllTestClass()
    allTestCase  = initAllTestCase( casePath     = casepath )
    tokenList    = []
    sign         = False