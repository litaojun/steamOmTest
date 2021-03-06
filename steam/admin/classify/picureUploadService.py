#https://blog.csdn.net/u010889616/article/details/78946589
from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
import requests, os
from steam.util.httpUopService import  HttpUopService
class PicureUploadService(HttpUopService):
    '''
        大转盘抽奖
    '''

    def __init__(self,kwargs):
        super(PicureUploadService, self).__init__("", "", kwargs)
        # self.filepath = os.getcwd() + os.path.sep + "steamcase" + os.path.sep + "%s"
        # self.url =  "https://uat-steam-api.opg.cn/steam-resource/resource/uploadImages"
        # self.files = {'file': open(self.filepath % kwargs['file'], 'rb')}

    def uploadImgFile(self):
        reponse = requests.post(url=self.url, files=self.files)
        return reponse.text

    def getRetcodeByrsp(self,classfiyRsp = None):
        return query_json(json_content=json.loads(classfiyRsp),query="code")

    @decorator(["setupAddFilePath"])
    def setFilePath(self):
        from steam.util.configIni import casepath
        self.inputKV["file"] = casepath + os.sep + "steamcase" + os.sep + self.inputKV["file"]

    def getImgUrlFromRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="data.links.0")

if __name__ == "__main__":
    inputw = {"file":"1.jpg"}
    pus = PicureUploadService(kwargs = inputw)
    rsp = pus.uploadImgFile()
    urlid = pus.getImgUrlFromRsp(response=rsp)
    print(urlid)