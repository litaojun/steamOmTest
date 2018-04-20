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

base_url = "https://uat-steam-api.opg.cn"
addentryurl = base_url + "/resource-service/resource/addEntry"
alertentryurl = base_url +"/resource-service/resource/modifyEntry"
delEntryurl = base_url + "/resource-service/resource/removeEntry"
addMatchurl = base_url + "/match-service/match/createMatch"
delMatchurl = base_url + "/match-service/match/deleteMatch"
alertMatchurl = base_url + "/match-service/match/updateMatchById"
uploadImagesurl = "/steam-resource/resource/uploadImages"
addArticleurl =  base_url + "/steam-media/media/addMedia"


if __name__ == "__main__":
	pass  