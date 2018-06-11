#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: steamLog.py 
@time: 2018/6/5 14:14 
"""

import logging  # 引入logging模块
import os.path
import time
from steam.util.reqFormatPath  import  fxt
from opg.unit.parametrized import ParametrizedTestCase
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
# # 第一步，创建一个logger
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)  # Log等级总开关
# # 第二步，创建一个handler，用于写入日志文件
# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# #log_path = os.path.dirname(os.getcwd()) + fxt + 'Logs' + fxt
# log_path = os.getcwd() + fxt + 'Logs' + fxt
# log_name = log_path + rq + '.log'
# logfile = log_name
# fh = logging.FileHandler(logfile, mode='w')
# fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
# # 第三步，定义handler的输出格式
# formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh.setFormatter(formatter)
# # 第四步，将logger添加到handler里面
# logger.addHandler(fh)
# # 日志
# # logger.debug('this is a logger debug message')
# # logger.info('this is a logger info message')
# # logger.warning('this is a logger warning message')
# # logger.error('this is a logger error message')
# # logger.critical('this is a logger critical message')
class SteamTestCase(ParametrizedTestCase):
    '''
          用户进入公众号首页，获取运营位数据
    '''
    __interfaceName__ = "/featured/index/configs/queryShowConfigs"
    memberIdDict = {}

    def __init__(self, methodName='runTest', param=None):
        super(SteamTestCase, self).__init__(methodName, param)

    def getInputData(self):
        inputData = super(SteamTestCase, self).getInputData()
        if "phoneNo" in inputData:
            if inputData["phoneNo"] in SteamTestCase.memberIdDict:
                inputData["memberId"] = SteamTestCase.memberIdDict[inputData["phoneNo"]]
            else:
                userVerCodeSer = WeixinUserVerfiyCodeService(kwargs=inputData)
                sedCodeRsp = userVerCodeSer.sendUserVerifyCode()
                retcode = userVerCodeSer.getRetcodeByUserLoginRsp(response=sedCodeRsp)
                if retcode == "000000":
                   verfiyCode = userVerCodeSer.getVerfiyCodeFromRedisByPhone(phoneNum=inputData["phoneNo"])
                   inputData["verfiyCode"] = verfiyCode
                   userLoginSer = WeixinUserLoginService(kwargs=inputData)
                   rsp = userLoginSer.weixinUserLogin()
                   code = userLoginSer.getRetcodeByUserLoginRsp(response=rsp)
                   if code  == "000000":
                      memberId = userLoginSer.getMemberIdFromRsp(response = rsp)
                      inputData["memberId"] = memberId
                      SteamTestCase.memberIdDict[inputData["phoneNo"]] = memberId
        return inputData

if __name__ == "__main__":
    args = {"phoneNo":"18916899938"}
    # testcase = SteamTestCase(args = )


