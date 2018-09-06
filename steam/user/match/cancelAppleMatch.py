#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: cancelAppleMatch.py 
@time: 2018/9/6 13:17 
"""
from steam.user.match.appleResetTools import userCancelAppleMatchByMatchId
if __name__ == "__main__":
    userCancelAppleMatchByMatchId(appleMatchId=5855047)