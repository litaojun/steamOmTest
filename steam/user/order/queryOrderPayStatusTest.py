#!/usr/bin/env python  
# encoding: utf-8  
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
# from opg.util.uopService import decorator
from steam.user.order.queryOrderPayStatusService import QueryOrderPayStatusService
# from steam.user.order.userOrederActivityService import UserOrderActivityService
from steam.util.testJsonFormat import initInputService
class QueryOrderPayStatusTest(SteamTestCase):
      '''
            查询订单的支付状态
      '''
      __interfaceName__ = "/order-service/order/payquery"
      #UserOrderActivityService
      @initInputService(services = [] ,
                        curser   = QueryOrderPayStatusService )
      def __init__( self, methodName='runTest' , param=None ):
          super(QueryOrderPayStatusTest,self).__init__(methodName , param)

      def checkOrderStatus(self):
          self.compareRetcodeTest()
          orderPayStatus = self.myservice.getOrderPayStatus()
          self.assertTrue(orderPayStatus == self.expectdata["orderPayStatus"],
                          msg            = "expect is %s,and resule is %s " % (self.expectdata["orderPayStatus"],orderPayStatus))

if  __name__ == "__main__":
    from inspect import ismethod
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\order-service-orderpay-query.yml",
                        testclse     = QueryOrderPayStatusTest
                 )
    # print(dir(SteamTestCase))
    # for m in dir(SteamTestCase):
    #     if ismethod(getattr(SteamTestCase,m)):
    #        print("testss")
    #        if m == "userOrderActivity":
    #           print("zzz")