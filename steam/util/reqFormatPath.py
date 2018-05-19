#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: li.taojun
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006
@software: PyCharm
@file: configurl.py
@time: 2018/4/18 14:40
"""
from opg.util.isSystemType import  getfileopertr
fxt = getfileopertr()
activityAddReq    = ["", "steam", "activity", "jsonfmt","addActivityReq.txt"]
activityAlertReq  = ["", "steam", "activity", "jsonfmt","alertActivityReq.txt"]
activityUpReq     = ["", "steam", "activity", "jsonfmt","upActivityReq.txt"]
activityDownReq   = ["", "steam", "activity", "jsonfmt","downActivityReq.txt"]
activityQueryReq  = ["", "steam", "activity", "jsonfmt","queryActivityReq.txt"]
activitySearchReq = ["", "steam", "activity", "jsonfmt","searchActivityReq.txt"]
articleAddReq     = ["","steam","article","jsonfmt","addArticleReq.txt"]
articleAlertReq   = ["","steam","article","jsonfmt","alertArticleReq.txt"]
articleDelReq     = ["","steam","article","jsonfmt","delArticleReq.txt"]
articleQueryReq   = ["","steam","article","jsonfmt","queryArticleReq.txt"]