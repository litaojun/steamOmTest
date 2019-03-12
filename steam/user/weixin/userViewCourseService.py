#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userViewCourseService.py 
@time: 2018/10/12 14:53 
"""

import json
from opg.util.utils import query_json
from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService
class UserViewCourseService(HttpUopService):
    '''
        用户查看课程
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserViewCourseService, self).__init__(  module       = modul,
                                                      filename     = filename,
                                                      sqlvaluedict = kwargs ,
                                                      reqjsonfile  = reqjsonfile )
    @decorator("setupGetSkuId")
    def getSkuIdFromRsp(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        self.inputKV["skuId"] =  query_json( json_content = json.loads(self.rsp) ,
                                                query      = "data.skuInfo.skuId" )
        self.inputKV["payPrice"]  = query_json( json_content = json.loads(self.rsp) ,
                                                query      = "data.skuInfo.price" )

    def genChapterSectionNameDict(self,response = None):
        if response is None:
           response = self.sendHttpReq()
        chapters = query_json(json_content = json.loads(response),
                              query        = "data.courseCategory.chapters")
        return dict([(  chapter["chapterName"],
                                       dict([(secttion["sectionName"],secttion["materialId"])
                                            for secttion in chapter["sections"]])
                             )
                           for chapter in chapters ])

    @decorator(["setupgetChapterMaterialId"])
    def setInPutData(self):
        charpterSecttionDict = self.genChapterSectionNameDict()
        if "sectionName" in self.inputKV and "chapterName" in self.inputKV:
           self.inputKV["materialId"] = charpterSecttionDict[self.inputKV["chapterName"]][self.inputKV["sectionName"]]
           print(self.inputKV["materialId"])

    # def getRetcodeByRsp(self,response = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")

    def checkTestdataByChapterNameOrSectionName(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        skuDict = self.genChapterSectionNameDict()
        if "chapterName" not in self.inputKV or self.inputKV["chapterName"] in skuDict:
            allSectionName = skuDict[self.inputKV["chapterName"]]
            if "sectionName" not in self.inputKV or self.inputKV["sectionName"] in allSectionName:
                return "000000"
        return "100001"

if  __name__ == "__main__":
    kwargs = {
                "courseId":4165,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"1e660b2bb70041098125d488e8c581fd",
                "chapterName":"第一章",
                 "sectionName":"1、"
             }
    uvcSer = UserViewCourseService(kwargs=kwargs)
    uvcSer.setInPutData()
    #courseRsp = uvcSer.userViewCourse()
    #print(courseRsp)