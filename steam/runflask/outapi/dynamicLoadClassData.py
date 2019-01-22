from steam.runflask.util import initData
from flask import Blueprint
from opg.unit.flaskRunMgr import initAllTestCase,initAllTestClass
from flask import jsonify
bapp = Blueprint('load', __name__)
@bapp.route('/prop/genTestclass', methods=['GET'])
def genTestClass():
    rtRunDt = {"code":"000000"}
    initData.allTestClass = initAllTestClass()
    return jsonify(rtRunDt)


@bapp.route('/prop/genTestdata', methods=['GET'])
def genTestData():
    rtRunDt = {"code":"000000"}
    # global allTestCase
    initData.allTestCase = initAllTestCase()
    return jsonify(rtRunDt)