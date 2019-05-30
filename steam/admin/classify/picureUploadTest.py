from steam.admin.classify.picureUploadService import PicureUploadService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initAdminInputService
import re
class PicureUploadTest(SteamTestCase):
    '''
          上传一个图片
    '''
    __interfaceName__ = "/steam-resource/resource/uploadImages"

    @initAdminInputService( services = [],
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
                    casefilepath = "\\steamcase\\admin\\testactivity\\steam-resourceresourceuploadImages.yml" ,
                    testclse     = PicureUploadTest,
                    basepath="D:\\litaojun\\steamyml"
                 )
    # imgurl = "http://uat-steam.opg.cn/_static/admin/images/resource/20180720142714_267655.jpg"
    # regStr = "^((https|http|ftp|rtsp|mms)?://)"
    # pattern = re.compile(pattern=regStr)
    # matcher = re.search(pattern, imgurl)
    # print(matcher.group(0))