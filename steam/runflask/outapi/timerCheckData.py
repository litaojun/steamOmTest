from flask import jsonify
import threading
from flask import Blueprint
from steam.runflask.tsdtmgr.testDataMnr import timeCheckData
bapp = Blueprint('timer', __name__)
timerSign = False
def startTimer():
    timeCheckData()
    timer = threading.Timer(900 , startTimer)
    timer.start()

@bapp.route('/prop/timeCheckData', methods=['GET'])
def dataTimerCheck():
    global timerSign
    rtJson = {"code":"100001" ,"msg":"定时任务已在运行中了"}
    if not timerSign :
       print("定时器启动....")
       # timer.setDaemon(daemonic=False)
       startTimer()
       timerSign = True
       rtJson    = {"code": "000000","msg": "定时任务启动成功"}
       print("定时器启动成功")
    return jsonify(rtJson)


if __name__ == "__main__":
    pass