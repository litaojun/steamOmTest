from opg.bak.flaskRunMgr import getRunTestTokenId
from opg.unit.runtest import genDir, writeLog


def func():
	pass


class Main():
	def __init__(self):
		pass
from opg.util.timeTool import getNowTime,getTwoFmtTime

if __name__ == "__main__":
	from steam.runflask.outapi.testcaseRun import runOneTestClass
	runOneTestClass(interfaceName="/operation-manage/product/queryProducts")