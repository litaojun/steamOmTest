#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryOrderPayStatusService.py 
@time: 2018/11/21 13:53 
"""
from steam.util.httpUopService import  HttpUopService
from opg.util.utils import query_json
import json
class QueryOrderPayStatusService(HttpUopService):
    '''
        查询订单的支付状态
    '''
    def __init__(self, kwargs       = {},
                       module       = "",
                       filename     = "",
                       reqjsonfile  = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(QueryOrderPayStatusService, self).__init__( module    = module ,
                                                          filename  = filename ,
                                                          sqlvaluedict = kwargs  ,
                                                          reqjsonfile  = reqjsonfile )

    def getOrderPayStatus(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        return query_json( json_content = json.loads(self.rsp),
                           query        = "data.status" )


if __name__ == "__main__":
    setattr(QueryOrderPayStatusService,"__interfaceName__","QueryOrderPayStatusService")
    print(QueryOrderPayStatusService.__interfaceName__)

