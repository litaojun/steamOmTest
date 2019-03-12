#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: findClassifyService.py 
@time: 2018/4/18 19:04 
"""
from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService
class ClassfiySearchService(HttpUopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ClassfiySearchService, self).__init__(module       = "",
                                                 filename     = "",
                                                 sqlvaluedict = kwargs)
    @decorator(["tearDownDelEntryId"])
    def delOneEntry(self):
        self.sendHttpReq()