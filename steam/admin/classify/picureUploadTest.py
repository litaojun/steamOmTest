#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: picureUploadTest.py 
@time: 2018/7/19 18:03 
"""
from steam.admin.classify.picureUploadService import PicureUploadService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initInputService
import re
class PicureUploadTest(SteamTestCase):
    '''
          新增活动
    '''
    __interfaceName__ = "/steam-resource/resource/uploadImages"

    @initInputService( services = [],
                       curser   = PicureUploadService )
    def __init__(self, methodName='runTest', param=None):
        super(PicureUploadTest, self).__init__(methodName, param)

    def userPicureUpload(self):
        rsp = self.myservice.uploadImgFile()
        retcode = self.myservice.getRetcodeByrsp(classfiyRsp = rsp)
        self.assertTrue(retcode == self.expectdata["code"])
        imgurl = self.myservice.getImgUrlFromRsp(response=rsp)
        regStr = "^((https|http|ftp|rtsp|mms)?://)"
        pattern = re.compile(pattern=regStr)
        matcher = re.search(pattern ,imgurl)
        self.assertTrue(matcher is not None)


if  __name__ == "__main__":
    runTestOneCls(
                    casefilepath = "\\steamcase\\testactivity\\steam-resourceresourceuploadImages.yml" ,
                    testclse     = PicureUploadTest
                 )
    imgurl = "http://uat-steam.opg.cn/_static/admin/images/resource/20180720142714_267655.jpg"
    regStr = "^((https|http|ftp|rtsp|mms)?://)"
    pattern = re.compile(pattern=regStr)
    matcher = re.search(pattern, imgurl)
    print(matcher.group(0))