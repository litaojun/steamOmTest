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
activityUpReq     = ["", "steam", "activity", "jsonfmt","publishActivityReq.txt"]
activityDownReq   = ["", "steam", "activity", "jsonfmt","unPublishActivityReq.txt"]
activityQueryReq  = ["", "steam", "activity", "jsonfmt","queryActivityReq.txt"]
activitySearchReq = ["", "steam", "activity", "jsonfmt","searchActivityReq.txt"]
articleAddReq     = ["","steam","article","jsonfmt","addArticleReq.txt"]
articleAlertReq   = ["","steam","article","jsonfmt","alertArticleReq.txt"]
articleDelReq     = ["","steam","article","jsonfmt","delArticleReq.txt"]
articleQueryReq   = ["","steam","article","jsonfmt","queryArticleReq.txt"]
activityAddRspFmt    = ["", "steam", "activity", "jsonfmt","addActivityRspFmt.json"]
activityAlertRspFmt  = ["", "steam", "activity", "jsonfmt","alertActivityRspFmt.json"]
activityUpRspFmt     = ["", "steam", "activity", "jsonfmt","publishActivityRspFmt.json"]
activityDownRspFmt   = ["", "steam", "activity", "jsonfmt","unPublishActivityRspFmt.json"]
activityQueryRspFmt  = ["", "steam", "activity", "jsonfmt","queryActivityRspFmt.json"]
activitySearchRspFmt = ["", "steam", "activity", "jsonfmt","searchActivityRspFmt.json"]
articleAddRspFmt     = ["","steam","article","jsonfmt","addArticleRspFmt.json"]
articleAlertRspFmt   = ["","steam","article","jsonfmt","alertArticleRspFmt.json"]
articleDelRspFmt     = ["","steam","article","jsonfmt","delArticleRspFmt.json"]
articleQueryRspFmt   = ["","steam","article","jsonfmt","queryArticleRspFmt.json"]
homeConfigQueryReq = fxt.join(["","steam","home","jsonfmt","homeCnfQueryReq.txt"])
homeConfigQueryRspFmt = fxt.join(["","steam","home","jsonfmt","homeCnfQueryRspFmt.json"])
homePositionReq = fxt.join(["","steam","home","jsonfmt","homePositionReq.txt"])
homePositionRspFmt = fxt.join(["","steam","home","jsonfmt","homePositionRspFmt.json"])
weixinUserLoginReq = fxt.join(["","steam","user","jsonfmt","weixinUserLoginReq.txt"])
weixinUserLoginRspFmt = fxt.join(["","steam","user","jsonfmt","weixinUserLoginRspFmt.json"])
weixinUserVerfiyCodeReq = fxt.join(["","steam","user","jsonfmt","weixinUserVerifyCodeReq.txt"])
weixinUserVerfiyCodeRspFmt = fxt.join(["","steam","user","jsonfmt","weixinUserVerifyCodeRspFmt.json"])
weixinUserThumbUpReq = fxt.join(["","steam","user","jsonfmt","weixinUserThumbUpReq.txt"])
weixinUserThumbUpRspFmt = fxt.join(["","steam","user","jsonfmt","weixinUserThumbUpRspFmt.json"])
weixinUserViewMediaresReq = fxt.join(["","steam","user","jsonfmt","weixinUserViewMediaresReq.txt"])
weixinUserViewMediaresRspFmt = fxt.join(["","steam","article","jsonfmt","weixinUserViewMediaresRspFmt.json"])