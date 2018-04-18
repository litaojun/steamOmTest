#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: picureUploadService.py 
@time: 2018/4/18 15:18 
"""


from opg.util.uopService import UopService
from opg.util.uopService import decorator
import requests,json
from opg.util.utils import query_json

class PicureUploadService(UopService):
    '''
        大转盘抽奖
    '''

    def __init__(self, **kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        # sqlvaluedict= {
        #                     "entryName"      : kwargs['entryName'],
        #                     "picturePath"    : kwargs['picturePath']
        #               }
        super(PicureUploadService, self).__init__("activity", "signUpNonOpenActivities.xml", kwargs)
        self.classfiyReqjson = {
							        "entryName": kwargs['entryName'],
							        "picturePath": kwargs['picturePath']
						       }
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    @decorator("addClassfiyService")
    def addClassfiy(self):
        addclassfiyRsp = requests.post(url=self.userBigWheelurl,
	                                   json=self.classfiyReqjson,
	                                   headers=self.jsonheart,
	                                   verify=False)
        code  = self.getRetcodeByrsp(classfiyRsp=addclassfiyRsp)
        return addclassfiyRsp.text

    def getRetcodeByrsp(self,classfiyRsp = None):
        return query_json(json_content=json.loads(classfiyRsp),query="code")

if __name__ == "__main__":
	pass  