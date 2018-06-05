#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userLoginService.py 
@time: 2018/3/2 17:00 
"""
from opg.util.uopService import UopService,decorator

class UserLoginService(UopService):
    def __init__(self):
	    super(UserLoginService, self).__init__(module = "collection",
	                                           filename = "usercollect.xml",
	                                           sqlvaluedict = {
	                                                              "memberId"      : "18916899938",
	                                                              "openid"        : "",
	                                                              "activitiesId"  : "fff"
                                                              }
	                                           )
    @decorator("interfaceUserLoginMobile")
    def userLoginMobile(self,name):
        print("input name is %s" % name)

if __name__ == "__main__":
   a = UserLoginService()
   userLoginMbe = getattr(UserLoginService,"userLoginMobile")
   userLoginMbe(a,"litaojun")
