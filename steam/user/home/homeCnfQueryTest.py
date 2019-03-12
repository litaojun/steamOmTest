#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: homeCnfQueryTest.py 
@time: 2018/6/5 10:48 
"""
from steam.user.home.homeCnfQueryService import HomeCnfQueryService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
class HomeCnfQueryTest(SteamTestCase):
      '''
            用户进入公众号首页，获取运营位数据
      '''
      __interfaceName__ = "/featured/index/configs/queryShowConfigs"
      @initInputService( services = [ ] ,
                         curser   = HomeCnfQueryService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(HomeCnfQueryTest,self).__init__(methodName,param)
      # self.homeCnfQuerySer = HomeCnfQueryService(self.inputdata)
      # self.setService(self.homeCnfQuerySer)
      # #首页，热门推荐-配置内容
      # def queryHomeCnf(self):
      #     userHomeCnfRsp = self.homeCnfQuerySer.queryHomePageCnf()
      #     retcode        = self.homeCnfQuerySer.getRetcodeByActivityRsp(response = userHomeCnfRsp)
      #     self.assertTrue(retcode == self.expectdata["code"])
      #     self.assertTrue(self.homeCnfQuerySer.compareData(response         = userHomeCnfRsp,
      #                                                      configSqlStr     = "select_t_sku_HomePage"))
      # #发现页-今日推荐-配置内容
      # def queryFindCnf(self):
      #     userFindCnfRsp = self.homeCnfQuerySer.queryHomePageCnf()
      #     retcode        = self.homeCnfQuerySer.getRetcodeByActivityRsp(response  = userFindCnfRsp)
      #     self.assertTrue(retcode == self.expectdata["code"])
      #
      # #创新大赛-配置内容
      # def homeInovnCnf(self):
      #       userFindCnfRsp = self.homeCnfQuerySer.queryHomePageCnf()
      #       retcode        = self.homeCnfQuerySer.getRetcodeByActivityRsp(response = userFindCnfRsp)
      #       self.assertTrue(retcode == self.expectdata["code"])

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    UserVerfiyCodeTest( methodName = "compareRetcodeTest" ,
                        param      = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    UserLoginTest( methodName     = "compareRetcodeTest" ,
                   param          = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    runTestOneCls( casefilepath =  "\\steamcase\\homepage\\featuredindexconfigsqueryShowConfigss.yml",
				   testclse     =  HomeCnfQueryTest )