#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: delClassifyService.py 
@time: 2018/4/18 19:06 
"""
from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService
class ClassfiyDelService(HttpUopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ClassfiyDelService, self).__init__(module       = "",
                                                 filename     = "",
                                                 sqlvaluedict = kwargs)
    @decorator(["tearDownDelEntryId"])
    def delOneEntry(self):
        self.sendHttpReq()

if __name__ == "__main__":
	pass  