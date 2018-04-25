#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: testTools.py 
@time: 2018/4/24 17:31 
"""
import requests

def func():
	pass


class Main():
	def __init__(self):
		pass


if __name__ == "__main__":
	data = {"Content-Disposition": "form-data; name=\"token\""}
	jsonheart = {
					"x-token": "admin",
					"content-type":"multipart/form-data"
				}
	files = {
				"file": open("Parameterizedfilter.jpg", "rb").read()
			}
	r = requests.post("https://uat-steam-api.opg.cn/steam-resource/resource/uploadImages",
	                  #data,
	                  #headers = jsonheart ,
	                  files=files)
	rsp = r.text
	print(rsp)