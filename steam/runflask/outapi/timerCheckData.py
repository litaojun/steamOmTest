from flask import jsonify
import threading
from flask import Blueprint
from steam.runflask.tsdtmgr.testDataMnr import timeCheckData
from steam.runflask.tsdtmgr.tokenDataMnr import sendHttpReqByToken

bapp = Blueprint('timer', __name__)
timerSign = False
timeToken = False

def startTimer(fun=None, time=1):
    fun()
    timer = threading.Timer(time, startTimer, (fun, time))
    timer.start()

@bapp.route('/prop/timeCheckData', methods=['GET'])
def dataTimerCheck():
    """数据检查定时任务"""
    global timerSign
    rtJson = { "code": "100001", "msg": "定时任务已在运行中了" }
    if not timerSign:
        print("定时器启动....")
        # timer.setDaemon(daemonic=False)
        startTimer(fun=timeCheckData, time=900)
        timerSign = True
        rtJson = { "code": "000000", "msg": "定时任务启动成功" }
        print("定时器启动成功")
    return jsonify(rtJson)


@bapp.route('/prop/timeRefreshToken', methods=['GET'])
def timeTokeRefresh():
    """token刷新定时任务"""
    global timeToken
    rtJson = { "code": "100001", "msg": "定时任务已在运行中了" }
    if not timeToken:
        startTimer(fun=sendHttpReqByToken, time=90)
        rtJson = {"code": "000000", "msg": "定时任务启动成功"}
        timeToken = True
        print("定时器启动成功")
    return jsonify(rtJson)


def genTestClass():
    pass


if __name__ == "__main__":
    pass
