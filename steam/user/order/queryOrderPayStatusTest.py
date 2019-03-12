#!/usr/bin/env python  
# encoding: utf-8  
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
# from opg.util.uopService import decorator
from steam.user.order.queryOrderPayStatusService import QueryOrderPayStatusService
# from steam.user.order.userOrederActivityService import UserOrderActivityService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userViewActivityService import  UserViewActivityService
from steam.util.testJsonFormat import initInputService
from steam.user.order.userOrederActivityService import UserOrderActivityService
from steam.user.member.memberAddressService import MemberAddressService
class QueryOrderPayStatusTest(SteamTestCase):
      '''
            查询订单的支付状态
      '''
      __interfaceName__ = "/order-service/order/payquery"
      #UserOrderActivityService
      @initInputService(services = [WeixinSearchService      ,
                                    UserOrderActivityService ,
                                    MemberAddressService ,UserViewActivityService ] ,
                        curser   = QueryOrderPayStatusService )
      def __init__( self, methodName='runTest' , param=None ):
          super(QueryOrderPayStatusTest,self).__init__(methodName , param)

      def checkOrderStatus(self):
          self.compareRetcodeTest()
          orderPayStatus = self.myservice.getOrderPayStatus()
          self.assertTrue(orderPayStatus == self.expectdata["orderPayStatus"],
                          msg            = "expect is %s,and resule is %s " % (self.expectdata["orderPayStatus"],orderPayStatus))

if  __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.weixin.userViewActivityTest import UserViewActivityTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.member.memberAddressTest import MemberAddressTest
    from steam.user.order.userOrderActivityTest import UserOrderActivityTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserViewActivityTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    MemberAddressTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserOrderActivityTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\order-service-orderpay-query.yml",
                        testclse     = QueryOrderPayStatusTest
                 )