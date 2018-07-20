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

#https://blog.csdn.net/u010889616/article/details/78946589
from opg.util.uopService import UopService
from opg.util.uopService import decorator
import requests,json
from opg.util.utils import query_json
import requests, os
class PicureUploadService(UopService):
    '''
        大转盘抽奖
    '''

    def __init__(self,kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(PicureUploadService, self).__init__("", "", kwargs)
        self.filepath = os.getcwd() + os.path.sep + "steamcase" + os.path.sep + "%s"
        self.url =  "https://uat-steam-api.opg.cn/steam-resource/resource/uploadImages"
        self.files = {'file': open(self.filepath % kwargs['file'], 'rb')}

    def uploadImgFile(self):
        reponse = requests.post(url=self.url, files=self.files)
        return reponse.text

    def getRetcodeByrsp(self,classfiyRsp = None):
        return query_json(json_content=json.loads(classfiyRsp),query="code")

    def getImgUrlFromRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="data.links.0")

if __name__ == "__main__":
    inputw = {"file":"1.jpg"}
    pus = PicureUploadService(kwargs = inputw)
    rsp = pus.uploadImgFile()
    urlid = pus.getImgUrlFromRsp(response=rsp)
    print(urlid)