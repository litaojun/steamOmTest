class Main():
	def __init__(self):
		pass
from opg.util.timeTool import getNowTime,getTwoFmtTime

if __name__ == "__main__":
	from steam.runflask.outapi.testcaseRun import runOneTestClass
	runOneTestClass(interfaceName="/featured/index/configs/queryShowConfigs")