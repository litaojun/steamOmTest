#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: materialQueryAliyunVideoAuthTest.py 
@time: 2018/12/10 11:16 
"""
from steam.util.steamLog       import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService         import WeixinSearchService
from steam.user.weixin.userViewCourseService       import UserViewCourseService
from steam.user.course.queryAliyunVideoAuthService import QueryAliyunVideoAuthService
from steam.util.testJsonFormat import initInputService
class MaterialQueryAliyunVideoAuthTest(SteamTestCase):
      '''
            用户获取观看权限字符串
      '''
      __interfaceName__ = "/steam-course/course/queryAliyunVideoAuth"
      @initInputService( services = [ WeixinSearchService , UserViewCourseService ],
                         curser   = QueryAliyunVideoAuthService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MaterialQueryAliyunVideoAuthTest,self).__init__(methodName , param)

if __name__ == "__main__":
   from steam.user.search.weixinSearchTest import WeixinSearchTest
   from steam.user.weixin.userViewCourseTest import UserViewCourseTest
   WeixinSearchTest(methodName="compareRetcodeTest",param = [1,2,3,4,5,{},7,8])
   UserViewCourseTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
   from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
   from steam.user.login.userLoginTest import UserLoginTest
   UserVerfiyCodeTest( methodName = "compareRetcodeTest",
                       param      = [1, 2, 3, 4, 5, {}, 7, 8] )
   UserLoginTest(methodName="compareRetcodeTest",
                 param=[1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\steam-coursecoursequeryAliyunVideoAuths.yml",
                    testclse     = MaterialQueryAliyunVideoAuthTest,
                    basepath     = "D:\\litaojun\\steamyml"
                )