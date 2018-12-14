#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryCourseService.py 
@time: 2018/12/10 11:01 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import recommandCourseUrl
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
class QueryCourseService(HttpUopService):
    '''
        用户查看课程详情页
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(QueryCourseService, self).__init__(  module       = modul,
                                                       filename     = filename,
                                                       sqlvaluedict = kwargs ,
                                                       reqjsonfile  = reqjsonfile )

