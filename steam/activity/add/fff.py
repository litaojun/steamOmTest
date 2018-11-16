#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: fff.py 
@time: 2018/11/14 10:45 
"""
from opg.util.testcaseTool import tranXlsToYmlFile,creatTestCaseDataByPath,creatTestCaseDataByYmlPath
import os
if __name__ == "__main__":
   basepath = os.getcwd()
   print(basepath)
   print(type(basepath))
   #basepath = "D:\litaojun\steamyml"
   d = creatTestCaseDataByPath(path = basepath)
   # # #
   # # # #print("testdata = " + str(d))
   tranXlsToYmlFile(casedict = d)